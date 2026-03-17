# 1 Introdução a Banco de Dados Relacionais (SQL)

## 1.1 Introdução aos Bancos de Dados Relacionais

### 1.1.1 Apresentação pessoal

...

### 1.1.2 Apresentação do curso

...

### 1.1.3 Conceitos Básicos e Estruturas do Banco de Dados Relacional

O que é um banco de dados

Coleção organizada de dados de forma estruturadas, normalmente armazenadas de forma eletrônica.

Tipos de banco de dados:

* Relacionais
* Não Relacionais
* Orientados a Objetos
* Hierárquico

O que é SGBD?

Sistema de gerenciamento de banco de dados, fornece conjunto de ferramentas e recursos para gerenciar, administrar e manipular os banco de dados.

CRUD

* Create
* Read
* Update
* Delete

Estrutura de um BD Relacional

Composto por um DB que armazena tabelas estruturadas

Uma tabela é composta por colunas, que definem os títulos de dados

O Registro, conhecido como linha ou tupla, são os conjunto de informações.

Relacionamento são compostas por chaves primárias e chaves estrangeiras

Características

* Relacionamento entre tabelas
* Linguagem de consulta estruturada (SQL)
* Integridade referencial
* Normalização de dados
* Segurança
* Flexibilidade e extensibilidade
* Suporte a transações ACID

Transaçoes ACID

* Atomocidade (todas as operações sejam executadas com sucesso ✅ ou nenhuma seja executada ❌ )
* Consistência (transações saem de um estado consistente para outro estado consistente respeitando todas as regras)
* Isolamento (todas as transações independem das outras transações, não interferindo às outras concorrentes)
* Durabilidade (Uma vez que a transação seja confirmada, ela permanece permanente)

### 1.1.4 Introdução e Conceitos Básicos de SQL

SQL ou *Structured Query Language*, surgiu 1970.

Organização da SQL

* DQL - Linguagem de Consulta de Dados `SELECT`
* DML - Linguagem de Manipulação de Dados `INSERT`, `UPDATE` e `DELETE`
* DDL - Linguagem de Definição de Dados `CREATE`, `ALTER` e `DROP`
* DCL - Linguagem de Controle de Dados `GRANT`, `REVOKE`
* DTL - Linguagem de Transação de Dados `BEGIN`, `COMMIT` e `ROLLBACK`

Sintaxe Básica: Nomenclatura (Regras gerais)

* Os nomes devem começar com um a letra com um caratere sublinhado `_`
* Os nome podem conter letras, números e caracteres de sublinhados
* Sensibilidade a maiúscula e minúsculas

### 1.1.5 MER e DER: Modelagem de Banco de Dados

Modelo Entidade-Relacionamento (MER) é representado de diagramas chamados Diagramas Entidade-Relacionamento (DER)

#### Entidades

* As entidades são nomeada com substantivos concretos ou abstratos que representem de forma clara sua função dentro do domínio
* representados por retângulos
* Ex: usuarios, destino e reserva

#### Atributos

* São caracterísitcas ou propriedades das entidades
Descrevem informações específicas sobre uma entidade
* Representados por elipses ou por uma tabela de uma coluna (lista).

<https://app.creately.com/> - para elaborar diagramas

#### Relacionamentos

* Representam as associações entre entidades
* Representado por um losango, ligado por uma linha entre as entidades
* Representado por um verbo

#### Cardinalidade

Refere a forma como as entidades relacionam uma com as outras

* Relacionamento `1..1` (um para um)
* Relacionamento `1..n` ou `1..*` (um para muitos)
* Relacionamento `n..n` ou `*..*` (muitos para muitos)

<https://app.quickdatabasediagrams.com> - realiza um diagrama a partir da IA

```txt
usuarios
-
id PK int
nome string
dataNascimento Date
endereco string

Reservas
-
id PK int
isUsuario int FK >- Usuarios.id
```

### 1.1.6 Configuração do Ambiente

<https://clients.cloudclusters.io> - 7 dias gratuito, é possível configurar e fazer o deploy de um banco de dados na nuvem. Tem o phpMyAdmin para acessar o banco de dados.

## 1.2 Modelagem de Dados Relacionais

### 1.2.1 Tabelas, Colunas e Registros

**Tabelas** - é usado para armazenar dados de forma organizada, cada tabela tem um nome único e é dividida em colunas e linhas

**Colunas** - é uma estrutura dentro de uma tabela que representa um *atributo específico* dos dados armazenadas. Cada coluna tem um nome único e um tipo de dado associado que define o tipo de informação que pode ser armazenado nela, como números, textos, datas e etc.

**Registros** - Conhecido como linha ou tupla.

```SQL
CREATE TABLE {{nome}}
    ({{coluna}} {{tipo}} {{opções}} COMMENT
{{'COMENTARIO'}});
```

#### Tipos de dados

* Integer (inteiro)
* Decimal / Numeric
* Character / Varchar
* Date/Time
* Boolean
* Text

#### Opções

* Restrições de valor:
* * NOT NULL
* * UNIQUE
* * DEFAULT
* Chaves primárias e estrangeiras
* Auto incremento

#### Mãos na massa

```SQL
CREATE TABLE usuarios (
    id INT, 
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULLL UNIQUE COMMENT 'E-mail do usuário',
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereco do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento');
```

É possível pré-definir em qual Database será criado a tabela:

```SQL
CREATE TABLE viagens.destinos (
    id INT, 
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino');

CREATE TABLE viagens.reservas (
    id INT COMMENT 'Identificador da reserva', 
    id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
    id_destino INT COMMENT 'Referência ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc.)'
);
```

### 1.2.2 Operações CRUD: Insert e Select

#### Modelo: INSERT

```SQL
INSERT INTO
    {{nome-tabela}}
    ([coluna1, coluna2, ...]) COMMENT 'você pode ocultar as colunas'
VALUES
    ([valor-coluna1, valor-coluna2, ...])
```

Exemplo:

```SQL
INSERT INTO
    usuarios (id, nome, email, data_nascimento, endereco) VALUES (1, 'Erick', 'erick@email.com', '1999-09-09', 'Rua tanto faz, 999')
```

```SQL
INSERT INTO
    destinos (id, nome, descricao) VALUES (1, 'Praia da Rosa', 'Linda praia');
```

```SQL
INSERT INTO
    reservas (id, id_usuario, id_destino,  status, data) VALUES (1, 1, 1, 'pendente', '2026-11-11');
```

Lembrando que ainda não estamos usando chave estrangeira, logo é possível passar ID que não existem de reserva ou destino.

#### Comando: SELECT

```SQL
SELECT {{lista_colunas}}
FROM tabela;
```

Pode colocar `*` para retornar todas as colunas.

#### Comando: SELECT com Where

```SQL
SELECT {{lista_colunas}}
FROM tabela
WHERE {{condicao}};
```

#### Comando: SELECT - Operadores

* `=` igualdade
* `<>` ou `!=` desigualdade
* `>` maior que
* `<` menor que
* `>=` maior ou igual que
* `<=` menor ou igual que
* `LIKE` comparação de padrões (ex: todos destinos com "praia")
* `IN` pertence a uma lista de valores (ex: todas as reservas com "pendentes" ou "confirmada")
* `BETWEEN` dentro de um intervalo de datas ou numéricos (ex: todas as reservas feitas na última semana)
* `AND` e lógico
* `OR` ou lógico

#### Exemplos práticos

Através do INSERT foi inserido mais 3 entradas em cada uma das tabelas

```SQL
SELECT * FROM usuarios
```

```SQL
SELECT * FROM usuarios WHERE id = 1;
```

```SQL
SELECT * FROM usuarios
WHERE id = 1 AND nome LIKE "%Erick%";
```

### 1.2.3 Operações CRUD: Update e Delete

Geralmente vem com o WHERE

```SQL
UPDATE {{tabela}}
SET
    {{coluna_1}} = {{novo_valor_1}},
    {{coluna_2}} = {{novo_valor_2}}
WHERE
    {{condicao}};
```

```SQL
DELETE FROM 
    {{tabela}}
WHERE
    {{condicao}};
```

Exemplo:

```SQL
UPDATE usuarios
SET id = 4
WHERE email = "email_fake_id_1@email.com"
```

```SQL
DELETE FROM destinos
WHERE nome = 'Praia do Rosa"
```

### 1.2.4 Alterando e Excluindo Tabelas

Problema hipotético:  

Usuários com endereços muito longos, estão causando lentidão no cadastro.  

Opções:  

* Recriar a tabela migrando os dados
* Alterar a estrutura da tabela

#### Drop Table

Remover uma tabela existente de um banco de dados relacional.

```SQL
DROP TABLE {{tabela}}
```

#### Alter Table

Usada para modificar a estrutura de uma tabela já existente, permite:

* Adicionar, alterar ou excluir colunas
* Modificar as restrições, índices
* Renomar a tabela entre outras alterações

#### Praticando

Criando a tabela nova

```SQL
CREATE TABLE usuarios_nova (
    id INT, 
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuario',
    email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de email do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
    endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do cliente'
);
```

Migrando os dados

```SQL
INSERT INTO usuarios_nova (id, nome, email, data_nascimento, endereco)
SELECT id, nome, email, endereco, data_nascimento
FROM usuarios;
```

Excluindo a tabela antiga

```SQL
DROP TABLE usuarios;
```

Renomeando a nova tabela

```SQL
ALTER TABLE usuarios_nova RENAME usuarios;
```

Agora a solução simples:

```SQL
ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);
```

### 1.2.5 Chaves Primárias e Estrangeiras

#### Chaves Primárias

* Identifica exclusivamente
* Não pode conter valores nulos (NULL)
* Uma tabela pode ter apenas uma chave primária.

```SQL
CREATE TABLE {{tabela}}
( id PRIMARY KEY AUTO_INCREMENT, ...);

ALTER TABLE {{tabela}}
MODIFY COLUMN id INT PRIMARY KEY;
```

#### Chaves Estrangeira

Usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas

* Pode ser nula (NOT NULL); conhecido como registro órfão
* É possível ter mais de uma (ou nenhuma) em uma tabela.

```SQL
CREATE TABLE {{tabela}}(
    id INT PRIMARY KEY,
    chave_estrangeira INT,
FOREIGN KEY (chave_estrangeira) REFERENCES {{outra tabela}} (id)
);
```

Se for para alterar na tabela, a gente adiciona uma CONSTRAINT:

```SQL
ALTER TABLE {{tabela}}
ADD CONSTRAINT {{nome_constraint}}
FOREIGN KEY (id_)
REFERENCES {{tabela_destino}} (id_destino)
```

#### Restrições

Mantem a intregridade referencial de nossos dados, existem algumas claúsulas que causa efeito nas suas exclusões ou edição.

* `ON DELETE` especifica o que acontece com os registros dependentes quando um registro pai é excluído.
* `ON UPDATE` define o comportamento dos registros dependentes quando um registro pai é atualizado.
* `CASCADE`, `SET NULL`, `SET DEFAULT` e `RESTRICT`

#### Exemplos

Vamos acrescentar as chaves primárias e estrangeiras nas nossas tabelas.

```SQL
ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);
```

```SQL
ALTER TABLE reservas
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);
```

Definindo as chaves estrangeiras

```SQL
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuarios) REFERENCES usuarios (id);
```

```SQL
ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destinos) REFERENCES destinos (id);
```

Quando excluir o pai, excluir os filhos:

```SQL
ALTER TABLE reservas
ADD CONSTRAINT fk_usuarios
FOREIGN KEY (id_usuarios) REFERENCES usuarios (id)
ON DELETE CASCADE;
```

Mas opa, ficou com duas `constraint`, vamos remover a anterior:

```SQL
ALTER TABLE reservas DROP CONSTRAINT fk_reservas_usuarios
```

Agora ao deletar o *usuario*, vai apagar as *reservas* que contém o id do usuário.

## 1.3 Normalização de Dados

### Problema

id | nome | endereco
-- | ---- | --------
1  | João | Rua A, 123, Cidade X, estado Alfa
2  | Ana  | Rua B, 456, Cidade Y, estado Alfa
3  | Bob  | Avenida C, 1, Cidade X, estado Beta

Como buscar todos os usuários da Cidade X ?

### Normalização de Dados

É um processo na etapa de modelagem, para eliminar redundância de dados, garantindo a consistência de dados.

### 1.3.1 Formas Normais

Inicial surgiu 3 formas normais (e principais)

#### 1.3.1.1 1FN: Atomocidade de dados

Cada valor na nossa tabela deve ser indivisivel. Nenhum campo deve conter múltiplos valores.  

Exemplo: *DDD e Número* ou endereço por completo com *Rua, Número, Cidade, Estado, País*

```SQL
ALTER TABLE usuarios
ADD rua VARCHAR(100),
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(20),
```

Como as informações estavam separadas por vírgula `,` é possível extrair as informações através de `substring`:  

`"Rua A, 123, Cidade X, estado Alfa"`

```SQL
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',' -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',' -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',' -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);
```

Agora apagando a coluna `endereco`:

```SQL
ALTER TABLE usuarios
DROP COLUMN endereco;
```

#### 1.3.1.2 2FN (2° Forma Normal)

* A 2FN estabelece que uma tabela deve estar na 1FN
* Todos os atributos não chave dem depender totalmente da chave primária

Dica se sua tabela tem uma **chave primária simples** não existe a possibilidade de termos dependência parcial e por tanto ela já se encontra na 2FN.  

Evita dependências parciais  

#### 1.3.1.3 3FN (3° Forma Normal)

* Uma tabela deve estar na 2FN
* Nenhuma coluna não-chave deve depender de outra coluna não-chave

Exemplo: ❌ Estado → Cidade. Infezlimente a Cidade é dependente do Estado.  

Mas para o nosso sistema não é relevante no momento e não afetará nosso banco.  

Evita dependência indiretas.  

## 1.4 Consultas Avançadas

### 1.4.1 Consultas com junções e subconsultas

#### 1.4.1.1 JOIN

São usadas no SQL para combinar dados de duas ou mais tabelas relacionadas em uma única consulta.  

* `INNER JOIN`
* `LEFT JOIN` ou `LEFT OUTER JOIN`
* `RIGHT JOIN` ou `RIGHT OUTER JOIN`
* `FULL JOIN` ou `FULL OUTER JOIN`

##### 1.4.1.1.1 INNER JOIN

Retorna apenas as linhas que têm **correspondência em ambas as tabelas** envolvidas na junção.  

A junção é feita com base em uma condição de igualdade especificada na cláusula `ON`.

```SQL
SELECT *
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

Exemplo:

```SQL
SELECT * FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuarios
INNER JOIN destino ds ON rs.destino = ds.id;
```

Exemplo: se fizermos um `SELECT` de **usuarios** com a tabela **reservas**, retorna apenas os usuários que tem reserva e mostra suas informações.

#### 1.4.1.2 LEFT JOIN

Retorno todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita.  

Se não houver correspondência, os valores da tabela à direita serão `NULL`.

```SQL
SELECT *
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

Similiar ao `INNER JOIN`, só que este aparece todas as linhas, porém aquele que não tem correspondência retorna como `NULL`.

Exemplo: se fizermos um `SELECT` de **usuarios** com a tabela **reservas**, retorna todos os usuários e quem não tem reserva aparece `NULL`.

#### 1.4.1.3 RIGHT JOIN

Basicamente como o LEFT JOIN, porém o contrário...

```SQL
SELECT * FROM reservas rs
RIGHT JOIN destinos ds
ON rs.id_destino = ds.id;
```

Exemplo: Vamos supor que tenhamos um **destino** que não tenha reserva. Se fizermos um `SELECT` nas **reservas** com a tabela **destinos**, retorna todos os **destinos** e aquelas dados faltantes em relação a **reserva** retornam como `NULL`.

#### 1.4.1.4 FULL JOIN

Retorna todas as linhas de ambas as tabelas envolvidas na junçao, combinando-as com base em uma condição de igualdade.  

Se não houver correspondência, os valores ausentes serão preenchidos como `NULL`.

#### 1.4.1.5 Sub Consultas

Elas permitem realizar consultas mais complexas permitindo que você usa o resultado de uma consulta como entrada para outra consulta.  

Onde podemos usar?

* `SELECT`
* `FROM`
* `WHERE`
* `HAVING`
* `JOIN`

**Exemplo**: Precisamos trazer todos os destino que não temos reservas.

```SQL
SELECT * FROM destinos
WHERE id NOT IN (SELECT id_destino FROM reservas);
```

**Traduzindo**: Consulta de todos os ID de destino dentro da tabela reserva → depois retornar todoso os destino que estavam ausentes.

**Exemplo**: Precisamos trazer aquele usuário que não fez nenhuma reserva.

```SQL
SELECT * FROM usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas);
```

**Exemplo**: Retornar a quantidade de reserva que um usuário tem no sistema.

```SQL
SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reserva FROM usuarios;
```

nome | total_reservas
---- | --------------
João Silva | 1
Maria Santos | 1
Pedro Souza | 1
Seu Madruga | 0

### 1.4.2 Fynções agregadas e agrupamento de resultados

#### 1.4.2.1 Funções Agregadas (agregadoras)

* `COUNT`: Conta o número de registros.
* `SUM`: Soma os valores de uma coluna numérica.
* `AVG`: Calcula a média dos valores de uma coluna numérica.
* `MIN`: Retorna o valor mínimo de uma coluna.
* `MAX`: Retorna o valor máximo de uma coluna.

**Exemplo**: Contar todos os usuários cadastrados

```SQL
SELECT COUNT(*) as total_usuarios FROM usuarios;
```

**Exemplo**: Contar todos os usuários cadastrados que tem reserva!

```SQL
SELECT COUNT(*) as total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario;
```

**Exemplo**: Qual o usuário mais velho?

```SQL
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios;
```

#### 1.4.2.2 Agrupamento de Resultados

Usado para dividir os dados em grupos com base em algum critério.

```SQL
SELECT ...
FROM ...
GROUP BY
```

**Exemplo**: Quantas reservas tem para cada destino?

```SQL
SELECT COUNT (*), id_destino FROM reservas
GROUP BY id_destino;
```

COUNT(*) | id_destino
-------- | ----------
1 | 1
1 | 2
2 | 3

#### 1.4.2.3 Ordenação de Resultados

Serve para ordenar uma coluna, seja de forma numérica, alfabética, seja de forma ascendente (ou descendente).

```SQL
SELECT ...
FROM ...
ORDER BY
```

No caso abaixo estamos quantificando a quantidade de reservas por destino, mas ordenando de forma decrescente a *quantidade de reserva* e pelo *id*

```SQL
SELECT COUNT (*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas, id_destino DESC
```

### 1.4.3 Índices de Busca

São estruturas de dados que aceleram as pesquisas nos bancos de dados, sendo criado a uma ou mais colunas.

#### Análise do Plano de Execução

```SQL
EXPLAIN
    SELECT *
    FROM {{tabela}}
```

Esse comando é responsável por retornar os dados da análise da execução da nossa query.

Tipos de campo que ele pode retornar:

* **select_type**: `SIMPLE`, `SUBQUERY`, `JOIN`
* **table**
* **type**: `ALL`, `INDEX` entre outros
* **possible_keys**: Os índices possíveis que podem ser utilizados na operação.
* **key**: O índice utilizado na operação, se aplicável
* **key_len**: O comprimento do índice utilizado
* **ref**: As colunas ou constantes usadas para acessar o índice
* **rows**: Quantas linhas o banco precisou olhar para encontrar a nossa busca

É importante olhar o **rows** para certificar que o banco não esteja fazendo um *full scan*.

Exemplo:

```SQL
EXPLAIN
    SELECT * FROM usuarios where email = 'joao.silva@example.com'
```

id | select_type | table | type | possivel_leys | key | key_len | ref | rows | Extra
-- | ------ | --- | -- | ------- | -- | ---- | -- | -- | ---
1 | SIMPLE | usuarios | const | email | email | 1022 | const | 1 |  

Nessa consulta só percorreu **uma única row**, isso ocorre porque foi definido anteriormente um índice de coluna, que foi o e-mail é com *unique*.

```SQL
EXPLAIN
    SELECT * FROM usuarios where nome = 'João Silva'
```

id | select_type | table | type | possivel_leys | key | key_len | ref | rows | Extra
-- | ------ | --- | -- | ------- | -- | ---- | -- | -- | ---
1 | SIMPLE | usuarios | ALL | NULL | NULL | NULL | NULL | 34 | Using where

Vamos criar um índice para a coluna de nome e avaliar como fica a comparação na nova consulta.

```SQL
CREATE INDEX idx_nome ON usuarios (nome);
```

```SQL
EXPLAIN
    SELECT * FROM usuarios where nome = 'João Silva'
```

id | select_type | table | type | possivel_leys | key | key_len | ref | rows | Extra
-- | ------ | --- | -- | ------- | -- | ---- | -- | -- | ---
1 | SIMPLE | usuarios | ref | idx_nome | idx_nome | 1022 | const | 2 | Using index condition

Agora ele leu 2 linhas, isso porque no nosso banco há 2 João Silva.

## 1.5 Mapa Mental dos Tópicos do Curso e Revisão

Mapa mental: <https://mindmeister.com/app/map/282937668>

É muito comum também o **ORM**, vem do conceito de fazer uma mapeamento do objeto com o relacional, sem precisar fazer consultas query na unha.
