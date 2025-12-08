# Models

Representam estruturas de dados e regras de negócio diretamente ligadas ao banco de dados.

## Propósito

* Definir o formato dos dados (ex.: User, Product, Order).
* Mapear tabelas (em ORMs como Sequelize, Prisma, etc.).
* Centralizar validações relacionadas ao domínio dos dados.
* Encapsular operações CRUD básicas (dependendo do ORM).

## Quando usar

Sempre que algo representar um recurso persistido no banco.
