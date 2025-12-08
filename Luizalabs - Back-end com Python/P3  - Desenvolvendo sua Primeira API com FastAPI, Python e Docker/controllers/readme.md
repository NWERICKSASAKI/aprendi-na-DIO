# Controllers

Camada responsável por receber a requisição, chamar o service adequado e retornar a resposta.

## Propósito

* Interpretar parâmetros da requisição (body, query, params).
* Controlar o fluxo da API (ex.: qual service deve ser chamado).
* Formatar a resposta HTTP.
* Tratar erros e enviar códigos de status adequados.

## Quando usar

Em qualquer endpoint — cada rota costuma ter um controller associado.
