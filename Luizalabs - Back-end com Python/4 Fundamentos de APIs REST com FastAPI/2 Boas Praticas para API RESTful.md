# Boas Práticas para API RESTful

Referência: <https://aline-antunes.gitbook.io/boas-praticas-para-apis-restful>

## Contextualizando as APIs RESTful

API RESTful usam arquitetura REST (Transferencia Representacional de Estado),  
é uma API que está conformidade com a arquitetura REST: boas práticas, restrições

**Arquitetura REST**: É um conj de princípios e restrições que promovem uma comunicação eficaz entre sistemas distribuídos.

API RESTful utilizam protocolo HTTP.

*Stateless*: cada chamada independe de outras chamadas, o servidor não armazena sobre o estado do cliente entre as requisições.

SOAP - Usa XML, permite segurança maior

### Por que seguir as boas práticas

É crucial garantir Consistência, Legibilidade e Escaláveis.  

* **Consistência**, uso uniforme, adotar padrões e convenções para ser previsível e fácil de entender.
* **Legibilidade**, de fácil compreensão (para humanos e computadores), com documentações intuitiva
* **Escaláveis**, capacidade da API se adaptar ao crescimento do projeto.

A utilização das **APIs RESTful** facilita integração entre sistemas (interobilidade), manutenção & evolução (escalabilidade), compreesão entre as equipes.

## As 7 Melhores Boas Práticas para APIs RESTful

### 1 Utilização de Substantivos em Rotas

Para deixar clara e intuitiva para outros humanos e máquinas, definindo **Rotas**.

* Utilizar termos no plural para definição de rotas, assim define que está definindo um conjunto de recursos.

`GET /users`

### 2 Utilização de Métodos HTTP

São fundamentais para a comunicação entre clientes e servidores na web.  
São padronizados e possuem finalidades específicas

Exemplos de *endpoints*:  

* `GET /products` - recupera uma lista de produtos  
* `GET /products/{id}` - recupera detalhes de um produto específico  
* `POST /products` - adiciona um novo produto ao catálogo  
* `PUT /products/{id}` - atualiza as informações de um produto existente  
* `DELETE /products/{id}` - remove um produto ao catálogo  

`GET` - recupera dados e não altera nada no servidor.  
`POST` - cria novos recursos para o servidor.  
`PATCH` - substitui completamente um recurso existente no servidor.  
`PUT` -  realiza a atualização parcial, alterando apenas os campos especificados.  
`DELETE` - remove um recurso do servidor.

### 3 Hierarquia e Aninhamento Em Rotas

**Aninhamento de rotas** é uma práticas de criar URL que segue uma estrutura **hierárquica** para representar a relação entre diferentes recursos.  
Isso faz com que as URL sejam intuitivas e reflita como os dados estão organizados.  

* Documentos/
* * Trabalhos/
* * * Relatórios/

`Documentos/Trabalhos/Relatórios/Relatorio1.docx`

URL: `/users/{userId}/orders`

### 4 Nome de Ações

Para garantir que as endpoints sejam intuitivas e fácil de entender, evitando o uso de verbos/ações nas URLs.  
Assim devemos usar os substantivos do HTTP.

Os métodos HTTP foram projetadas para atender as operações que queremos realizar em um recurso.

❌ `POST /createUser`  
✅ `POST /user`

### 5 Versionamento de Rotas

Permite manter múltiplas versões da da API em paralelo, atendendo clientes novos e antigos.

`GET /v1/users`  
`GET /v2/users`

### 6 Parâmetros de Consulta

São parte de uma URL que permite que informações adicionais sejam enviadas para um servidor.  
Eles são usadas para filtrar, paginar e ordenar dados, entre outras funções.  
Esses parâmetros são anexados à URL após um ponto de interrogação (`?`), e múltiplos parâmetros são separados por um E comercial (`&`).  

### 7 Tratamentos de Erros

Códigos de status HTTP são mensagens enviadas pelo servidor para o cliente após o processamento de uma requisição.  
Eles indicam se a requisição foi bem-sucedida, se houve um erro ou se algo precisa ser corrigido.  

| Código | Tipo de Código | Descrição|
|--------|----------------|----------|
| `1xx` | *Informational Codes* | O servidor reconhece e está processando a solicitação. | 
| `2xx` | *Success Codes* | O servidor recebeu e processou com sucesso a solicitação. |
| `3xx` | *Redirection Codes* | O servidor recebeu a requisição, mas há um redirecionamento para outro lugar. |  
| `4xx` | *Cliente Error Codes* | O servidor não conseguiu encontrar a página ou site. Este é um erro do lado do site. |  
| `5xx` | *Server Error Codes* | O cliente fez uma solicitação válida, mas o servidor falhou ao completar a solicitação. |  
