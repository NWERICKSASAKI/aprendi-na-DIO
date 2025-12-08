# Services

Camada que contém a lógica de negócio da aplicação.

## Propósito

* Processar os dados antes de salvar/buscar.
* Executar regras de negócio (ex.: cálculo, validação complexa, integrações externas).
* Coordenar operações entre vários models.
* Reduzir a responsabilidade dos controllers.

## Quando usar

Sempre que houver regra de negócio que não deve ficar nem no controller nem no model.
