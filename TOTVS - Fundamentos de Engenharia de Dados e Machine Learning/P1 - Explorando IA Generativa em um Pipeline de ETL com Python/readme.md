# Projeto 1 - Explorando IA Generativa em um Pipeline de ETL com Python

Este projeto foi proposto no **Santander Dev Week 2023 (ETL com Python)**, nele havia o seguinte descritivo:

## Santander Dev Week 2023 (ETL com Python)

**Contexto:**  
Você é um cientista de dados no Santander e recebeu a tarefa de envolver seus clientes de maneira mais personalizada. Seu objetivo é usar o poder da IA Generativa para criar mensagens de marketing personalizadas que serão entregues a cada cliente.

**Condições do Problema:**  

1. Você recebeu uma planilha simples, em formato CSV ('SDW2023.csv'), com uma lista de IDs de usuário do banco: 

```txt
UserID,
1,
2,
3,
4,
5,
```

2. Seu trabalho é consumir o endpoint `GET https://sdw-2023-prd.up.railway.app/users/{id}` (API da Santander Dev Week 2023) para obter os dados de cada cliente.
3. Depois de obter os dados dos clientes, você vai usar a API do ChatGPT (OpenAI) para gerar uma mensagem de marketing personalizada para cada cliente. Essa mensagem deve enfatizar a importância dos investimentos.
4. Uma vez que a mensagem para cada cliente esteja pronta, você vai enviar essas informações de volta para a API, atualizando a lista de \"news\" de cada usuário usando o endpoint `PUT https://sdw-2023-prd.up.railway.app/users/{id}`.

## Atual Contexto

A API para consumo e carregamento de dados deste projeto era um ambiente público de demonstração e foi descontinuada.

### Extract

Então para a resolução deste projeto foi proposte duas alternativas:

1. Criar os dados dos usuários diretamento no código, ou
2. Adotar um arquivo csv e usá-la como fonte de dados

### Transform

Originalmente a proposta era enriquecer os dados adicionando uma mensagem personalizada gerado pela IA, utilizando uma chamade para API da OpenAI utilizando o GPT-4.

### Load

Devido não ter mais a API, a nova proposta se resumiu em gerar um novo arquivo CSV, JSON ou até mesmo plotar em tela o resultado.

## Minha Resolução

Resolvi gerar um arquivo CSV com dados aleatórios (incluindo dados faltantes) através do :<https://www.mockaroo.com/>.

Para gerar os dados foi utilizado as configurações abaixo:

| Field Name | Type | Options |
| ---------- | ---- | ------- |
| id | Row Number | blank: 0 % |
| first_name | First Name | blank: 0 % |
| last_name | Last Name | blank: 5 % |
| email | Email Address | blank: 5 % |
| gender | Gender | blank: 5 % |
| money | Money | between: 0 and 10000 in $ blank: 0 %|
| allow_ads | Boolean | blank: 5 % |

Salvando o CSV localmente neste repositório, vou acessar o arquivo simulando como se estivesse na internet.

No caso o CSV se localiza na seguinte url: <https://github.com/NWERICKSASAKI/aprendi-na-DIO/raw/refs/heads/main/TOTVS%20-%20Fundamentos%20de%20Engenharia%20de%20Dados%20e%20Machine%20Learning/P1%20-%20Explorando%20IA%20Generativa%20em%20um%20Pipeline%20de%20ETL%20com%20Python/MOCK_DATA.csv>
