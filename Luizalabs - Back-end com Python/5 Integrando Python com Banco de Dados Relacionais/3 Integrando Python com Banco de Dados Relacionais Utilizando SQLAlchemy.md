# 3 Integrando Python com Banco de Dados Relacionais Utilizando SQLAlchemy

## Explorando a Biblioteca SQLAlchemy

Framework - Open source
Mapeamento Objeto Relacional

Suporta: *Microsoft SQL Server*, *MySQL / MariaDB*, *Oracle*, *PostreSQL* e *SQLite*.

### Dialetos externos

| Database | Dialect |
| -------- | ------- |
| Amazon Redshift | `sqalchemy-redshift` |
| Apache Drill | `sqalchemy-drill` |
| Apache Druid | `pydruid` |
| Apache Hive | `PyHive` |
| Apache Solr | `sqlalchemy-solr` |
| CrateDB | `crate-python` |
| Elasticsearch | `elasticsearch-dbapi` |

### Recursos

* ORM (método com orientado a objeto) e CORE (utilizar os *statements* do SQL)
* Suporte a dialetos
* Manipulação do BD por meio de Transações (por conjunto, se houver erro pode reverter)
* Suporte a Queries complexas via ORM (pode usar *join* e outros comandos)
* Config: relações e relacionamentos (pode fazer um mapeamento pelo métodos e classes do SQLAlchemy)
* Sessões, eventos ...

### Extensões

* I/O Assíncrono
* Associação com proxy
* Indexação
* APIs especiais

## Entendendo o modelo ORM - Object Relational Mapping

* ORM - Object Relational Mapping
* Ojeto -> Modelo Relacional
* Mais fácil par ao programador

### Vantagens

* Menos código
* Melhor manutenção
* Utilização de conectores (dialeto) - desnecessita conhecimento de linguaguens de Banco de Dados
* Indicado para CRUDs

### Entidade

*Entidade é a tabela do MER (Modelo de Entidades Relacionais).*  

PS: *DER - Diagrama de Entidade-Relacionamento* -> é a imagem em si do MER.

É um objeto,  
E há relacionamento entre objetos  

### Desvantagens

* Complexidade das queries X ORM (pois as vezes precisa fazer vários JOIN quando só usar SQL seria mais simples)
* Dependência do ORM
* Depende do projeto
* Retorno das consultas sem necessidade de programar na "mão"
* Perda de performance
* Deixa de estudar SQL e perde a eficiência na construção
* Número de instâncias x velocidade

OBS: ORM foi projetado para ser usado em um banco bem definido.

## Considerações sobre o uso do ORM

### Por que usar?

* Troca de SGBD mais facilitada
* Modelo MVC (*Model-View-Controller*)
* Diminuição do DRY (Don't Repeat Yourself)
* Evita problemas de segurança

### ORM & SQL

* Melhor dos dois mundos
Exemplo: fazer SELECT em cima de uma VIEW

## Criando as entidades com declarative_base

```py
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    id = Column(Interger, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Interger, primary_key=True)
    email_address = Column(String(30), nullable=False) # não permite valor nulo
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email_address})"


print(User.__tablename__)
```






## Executando consultas com ORDER BY, JOIN Statement e Função COUNT

```py
# SELECT FROM User BY
order_stmt = select(User).order_by(User.fullname.desc())

print(order_stmt)
# SELECT user_account.id, user_account.name, user_account.fullname
# FROM user_account ORDER BY user_account.fullname DESC

for result in session.scalars(order_stmt):
    print(result)

# User(id=1, name=juliana, fullname=Juliana Mascarenhas)
# User(id=2, name=sandy, fullname=Sandy Cardoso)
# Address(id=2, email_address=sandyc@email.br)
# Address(id=3, email_address=sandyc@email.org)
# User(id=2, name=sandy, fullname=Sandy Cardoso)
# User(id=3, name=patrick, fullname=Patrick Cardoso)
# User(id=1, name=juliana, fullname=Juliana Mascarenhas)
```

```py
# JOIN
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print(stmt_join)
# SELECT user_account.fullname, address.email_address
# FROM address JOIN user_account ON user_account.id = address.user_id

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("Executando statemente a partir da connection")
for result in results:
    print(result)

#User(id=2, name=sandy, fullname=Sandy Cardoso)
#User(id=3, name=patrick, fullname=Patrick Cardoso)
#User(id=1, name=juliana, fullname=Juliana Mascarenhas)
```

````py
# COUNT
stmt_count = select(func.count('*')).select_from(User)
print(stmt_count)
# SELECT count(:count_2) AS count_1
# FROM user_account

for result in session.scalars(stmt_count):
    print(result)
# 3
```

## Criando esquema com SQLAlchemy Metadata
