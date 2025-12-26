# Explorando Banco de Dados Relacionais com Python DB API

## Introdução aos Banco de Dados Relacionais - parte 1

Em uma tabela, cada *linha* é um *registro* distinto, uma *coluna* é um tipo de informação.
Cada tabela em um banco de dados relacionais deve ter uma **chave primária**, cujo valor é único, para garantir a **unicidade**.

## Introdução aos Banco de Dados Relacionais - parte 2

**Chaves estrangeiras**, permite que associe uma tabela com outra através da chave primária.
Tabela 1 - Cliente: `ID`, `Nome`, `email`, `telefone`
Tabela 2 - Pedidos: `ID`, `Valor`, `Cliente ID`

Relacionamento entre tabelas, permite estabelecer relações entre tabelas.  
Podendo ser `1 - 1`, `1 - n` ou `n - n`.  
Estas relações permitem efetuar consultas complexas que unem dados de várias tabelas.  

Para relacionar `n - n` é utilzado uam terceira tabelas para relacioná-los.

|ID_Usuários|ID_Pets|
|-----------|-------|
|1|1|
|1|2|
|2|1|
|2|2|

## Introdução aos Banco de Dados Relacionais - parte 3

**SQL**, utilziada para interagir com dados relacionais. Podemos criar tabela, inserir, atualiza e deleta registros assim como realizar consultas para buscar dados.

## Conectando com o Banco de Dados

Estabelecer conexão com o Banco de Dados usando BD API

```py
import sqlite3
con = sqlite3.connect('meu_banco_de_daos.db')
```

```py
import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'clientes.db') # se não existe, cria
print(conexao)
```

## Criando uma Tabela

```py
import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'clientes.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
```

## Inserindo Registros

```py
import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'clientes.db')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

# até dá pra usar f-string, mas não é seguro
data = ("Guilherme", "gui@email.com")
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)' data)

conexao.commit() # executa todos as alterações dos dados
```

## Atualizando Registros

Sempre utilize `WHERE` para evitar de atualizar a tabela inteira

```py
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / '2 clientes.sqlite')
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "Eldrich", "erick@email.com", 1)
```

## Removendo Registros

```py
data = (id,)
cursor.execute("DELETE FROM clientes WHERE id=?;", data)
conexao.commit()
```

## Inserindo Registros em Lote

Operações em lote, evitando `while`s ou `for`s

```py
lista_dados = [
    ("Guilherme","gui@email"),
    ("Chappie","cha@email"),
    ("Melanie","mel@email"),
]

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', lista_dados)
conexao.commit()
```

## Consultando Registros

`cursor.fetchone()` retonar 1 registro, (sempre o próximo) ou vazio caso não houver.
`cursor.fetchall()` retonar uma lista de resultados de todos os resultados

```py
def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome')

print(recuperar_cliente(cursor, 5))
print(list(listar_clientes(cursor)))
```

## Alterando o Row Factory

Se a tupla não nos atender, podemos personalziar com `row factory`.

```py
def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor, 5)
print(dict(cliente))
```

## Boas Práticas

Para garantir segurança e eficiência.

* Evitar concatenação de string

```py
id_cliente = input('informar o id do cliente:') # 1 OR 1=1
cursor.execute('SELECT * FROM clientes WHERE='+id_cliente)
clientes = cursor.fetchall()
print(clientes)
```

Se a pessoa der um input com `1 OR 1=1` vai exibir todos os usuários.

## Gerenciando transações

O `commit()` finaliza a transação.
Mas se caso algo der errado, convém desfazer todas as alterações com `rollback()`

```py
try:
    cursor.execute('INSERT INTO minha_tabela VALUES (?,?)', (1,'abc'))
    conexao.commit()
except Exception as e:
    print('Ocorreu um erro: ' + e)
    conn.rollback()
```

```py
with sqlite3.connection(ROOT_PATH  / "clientes.sqlite") as conexao:
    cursor = conexao.cursor()
    # todas as alterações
    try:
        conexao.commit()
    except Exception as e:
        print('Ocorreu um erro: ' + e)
        conn.rollback()
```
