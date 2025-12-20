# P4 Criando sua API Bancária Assíncrona com FastAPI

Referência: <https://github.com/digitalinnovationone/trilha-python-dio/tree/main/13%20-%20APIs%20Ass%C3%ADncronas%20com%20FastAPI/desafio>

## Desafio: API Bancária Assíncrona com FastAPI

O desafio conssitem em projetar e implementar uma API RESTful assíncrona usando **FastAPI** para gerenciar operações bancárias de **depósitos** e **saques**, vinculadas a **contas correntes**. Este desafio irá lhe proporcionar a experiência de construir uma aplicação backend moderna e eficiente que utiliza **autenticação JWT** e práticas recomendadas de design de APIs.

### Objetivos e Funcionalidades

Objetivo do desafio é desenvolver uma API com as seguintes funcionalidades:

- **Cadastro de Transações:** Permita o cadastro de transações bancárias, como depósitos e saques.
- **Exibição de Extrato:** Implemente um endpoint para exibir o extrato de uma conta, mostrando todas as transações realizadas.
- **Autenticação com JWT:** Utilize JWT (JSON Web Tokens) para garantir que apenas usuários autenticados possam acessar os endpoints que exigem autenticação.

### Requisitos Técnicos

Para a realização deste desafio, deve ser atendido aos seguintes requisitos técnicos:

- **FastAPI:** Utilize FastAPI como framework para criar sua API. Aproveite os recursos assíncronos do framework para lidar com operações de I/O de forma eficiente.
- **Modelagem de Dados:** Crie modelos de dados adequados para representar contas correntes e transações. Garanta que as transações estão relacionadas a uma conta corrente, e que contas possam ter múltiplas transações.
- **Validação das operações:** Não permita depósitos e saques com valores negativos, valide se o usuário possui saldo para realizar o saque.
- **Segurança:** Implemente autenticação usando JWT para proteger os endpoints que necessitam de acesso autenticado.
- **Documentação com OpenAPI:**  Certifique-se de que sua API esteja bem documentada, incluindo descrições adequadas para cada endpoint, parâmetros e modelos de dados.
