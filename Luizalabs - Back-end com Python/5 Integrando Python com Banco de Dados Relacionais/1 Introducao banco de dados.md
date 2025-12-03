# Introdução banco de dados

## Introdução à banco de dados

### Banco de dados

É uma coleção organizada de informações (ou dados) estruturadas, normalmente armazenadas eletronicamente em um sistema de computador.

Dado estruturado é um dado organizado.

**Banco de Dados** é um servidor com software de banco de dados, não apenas um repositório de dados, com mecanismo de segurança, como autenticação e controle de acesso de pessoas autorizadas, e também fica disponibilizado para outros sistemas (API, Nuvem, clientes via web) de forma inteligente (atendendo todos de forma rápida e eficiente, sem gargalos).

## Tipos de bancos de dados

**Banco de dados relacional** - o tipo mais usado atualmente, composto por dados estruturados e organizados em tabelas, com colunas e linhas, que se relacionam entre si.

* MySQL - Gratuito
* Microsoft SQL Server , Oracle Database - maior segurança e disponibilidade

## Entendendo uma tabela

Tabelas de Clientes e Endereços.  
Poderia deixar tudo numa tabela só? Sim, mas separar é uma boa prática.  
Separe a tabela por contextos.  
Elas se relacionam através de uma chave que aponta pra outra tabela.  

## Banco de dados não relacional

**Banco de dados nçao relacional** -  Banco de dados onde os dados *não são armazenados em tabelas*, e sim em armazenamento de maneira não estruturadas ou semi-estruturadas.
Exemplo `preço`, em que pode ser valor `float`, `str` ou até mesmo `nulo`  
Não segue regras rígidas, é mais rápido que banco de dados estruturados.

Existem vários tipos: *document databases*, *key-value database*, *wide-column stores* e *graph databases*.
mongoDB - pode inserir

## Tipos de dados

* **Estruturado** - se remover/adicionar uma coluna da tabela, afeta todos os itens; não aceita outros valores além do esperado (`float` por `int` ou `string`). Obecede regra rígidas de inserção.
* **Semi-estruturado** - tem uma estrutura/padrão, pode haver campos a mais ou a menos em cada um dos itens, seus valores podem armazenar diferentes tipo de dados.  

## Entendendo o DBMS

**DataBase Management System** ou **SGBD (Sistema de Gerenciamento de Banco de Dados)** é um software utilizado para acessar, manipular e monitorar um sistema de banco de dados.  
O Banco de dados em sí não tem tela, então é necessário visualiza-lo e acessar via DBMS.

## Instalando o SQL Server

...