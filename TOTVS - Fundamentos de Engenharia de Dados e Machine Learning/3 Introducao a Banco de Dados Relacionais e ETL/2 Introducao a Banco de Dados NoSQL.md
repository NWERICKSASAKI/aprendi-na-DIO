# 1 Introdução a Banco de Dados NoSQL

## 1.1 Introdução aos Bancos de Dados Não Relacionais

### 1.1.1 Apresentação pessoal

...

### 1.1.2 Conceitos básicos dos bancos de dados não relacionais

* Termo correto: *NOT Only SQL*
* Não seguem modelo de tabelas e relacionamentos
* Projetados para lidar com **alto volume de dados**, alta escalabilidade
* Alta **flexibilidade** na estrutura de dados
* Eles são amplamento utilizados em cenários onde a consistência imediata dos dados não é crítica - ou seja, se há 3 espelhos ele só vai gravar a informação caso seja garantido que seja replicado em todas as instâncias.

Tabela de diferenças:

SQL | NoSQL
--- | -----
Modelos de dados fixo| Modelos de dados flexível
Escalabilidade vertical (hardware) | Escalabilidade horizontal
Transações ACID 100% | Transações ACID ausentes total ou parcial
Linguagem de consulta SQL | Cada SGBD tem sua própria

Vantagens dos bancos de dados NoSQL

* Flexibilidade na modelagem
* Alta escalabilidade
* Melhor desempenho em cenário de consulta intensiva
* Tolerância a falhas

Desvantagens 

* Menor consistência de dados imediata
* Menor suporte a consultas completas (depende do SGBD)

### 1.1.3 Visão geral dos tipos de NoSQL

Tipos de armazenamento:

* Key-Value
* Documento
* Coluna
* Grafos
* Entre outros...

#### 1.1.1.3.1 Key-Value

Armazena dados como pares de chave e valor, onde cada chave é um identificador único para acessar o valor correspondente.  

**Exemplo de SGBD**: Redis, Riak, Amazon DynamoDB  

**Uso**: Um site pode usar um banco de dados Redis para armazenar informaçõs de sessão de usuário.

#### 1.1.1.3.2 Documento

Armazenram dados em documentos semiestruturados, geralmente em formato JSON, BSON, XML, etc.  

**Exemplo de SGBD**: MongoDB, Couchbase, Apache CouchDB  

**Uso**: Um catálogo de e-commerce pode usar o MongoDB para armazenar informações de produtos, como nome, descrição, preço e atributos adicionais.

#### 1.1.1.3.3 Coluna

Armazenam dados em formato de colunas, o que permite alta escalabilidade e eficiência em determinados tipos de consultas.  

**Exemplo de SGBD**: Apache Cassandra, ScyllaDB, HBase.  

**Uso**: Um sistema de registro de aplicativos pode usar o Apache Cassandra para armazenar registros de log.

#### 1.1.1.3.4 Grafos

Armazerar e consulta dados interconectados, onde os relacionamentos entre os dados são tão importantes quando os próprios dados  

**Exemplo de SGBD**: Neo4j, Amazon Neptune, JanusGraph  

**Uso**: Uma rede social pode usar o Neo4j para armazenar os perfis dos usuários e suas conexões, permitindo consultas eficientes para encotnrar amigos em comum.

## 1.2 Introdução ao MongoDB

## 1.3 Operação no MongoDB