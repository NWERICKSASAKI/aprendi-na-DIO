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

### 1.2.1 Introdução ao MongoDB

Amplamente utilizado na indústria.

* Banco de dados NoSQL orietando a documentos
* Grandes volumes de dados, escalabilidade horizontal e modelagem flexível
* Não exige um esquema
* Permite que os documentos seja armazenados em formato BSON (Binary JSON), proporcionando uma estruturada semiestruturada.

#### Vantagens

* Flexibilidade na modelagem de dados
* Escalabilidade horizontal para lidar com grandes volumes de dados
* Consultas ricas e suporte a consultas complexas
* Alta disponibilidade e tolerância a falhas
* Comunidade ativa e recursos de suporte

#### Desvantagens

* Menor consistência imediata em comparação com bancos de dados relacionais
* Consultas complexas podem exigir um maior conhecimento e planejamento adequado
* Maior consumo de espaço de armazenamento em comparação com bancos de dados relacionais devido à flexibilidade dos documentos

#### Onde é usado

* Aplicações web: Onde a flexibilidade e a escalabilidade são cruxiais para lidar com volumes variáveis de dados
* Análise de big data: Análise de grande volumes de dados não estruturados ou semiestruturados, fornecendo uma plataforma para armazenar e processar esses dados
* Armazenamento de dados semiestruturados: Permite a inserção de documentos com estruturas diferentes emuma mesma coleção
* Casos de uso de geolocalização: Com suas funcionalidades de consulta geoespacial, é adequado para casos de uso que envolvem dados baseados em localização, como aplicativos de mapeamento e rastreamento.

### 1.2.2 Instalação e configuração do MongoDB Atlas

Plataforma online!  
Sem necessidade de provisionar ou de DBA.  
Gratuito, sem tempo de *trial*.

<https://cloud.mongodv.com/>

`[Build a database]` → M0  
`Provider` AWS  
`Name`: viagens  
`[Create]`  

Crie um usuário e senha e anote o **username** e **password** criado.  

Nossa instância tem 3 nós, não tem backup.  

### 1.2.3 Modelagem de dados usando documentos

#### Estrutura

* Uma estrututra é constituido por um ou mais database.
* Um database é constituído por coleções.
* Uma colação é composta por vários documentos.

#### Coleções

* Agrupamento lógico de documentos
* Não exige esquema ou que os documentos tenham a mesma estrutura

#### Características dos documentos

Os nome das coleções devem seguir algumas regras:

* Devem começar com uma letra ou um underscore `_`
* Podem conter letras, números ou underscores
* Não podem ser vazios
* Não pode ter mais de 64 bytes de comprimento

#### Documentos

O documento é a representação da informação que estamos salvando

* São armazenados em docuemntos BSON (Binary JSON) que são estruturas flexíveis e semiestruturadas
* Cada documento possui um identificador único chamado `_id`
* É composto por pares de chaves e valores.
* Tamanho máximo: Cada documento no MongoDB pode ter um tamanho máximo de 16 MB
* Aninhamento de documentos (inner document / documento-filho / json dentro de json)
* Flexibilidade na evolução do esquema

#### Tipos de Dados Simples

* String
* Number
* Boolean
* Date
* Null
* ObjectId

#### Tipos de Dados Complexas

* Array
* Documentos Embutidos (Embedded Documento / aninhado / json dentro de json)
* Referência (Reference)
* GeoJSON

#### Estrutura de um documento

```js
{
    _id: ObjectID(""),
    "nome_campo": "valor_campo",
    ...
}
```

#### Exemplo prático: Modelagem da estrutura do Usuário e Destinos

<https:/jsonformatter.curiousconcept.com/>

Usuários:

```JS
{
    "_id":1,
    "nome": "Erick",
    "idade": 31,
    "data_nascimento":"1994-06-01",
    "endereco": "Rua ABC, 123...",
    "enderecos": [{
        "logradouro":"Rua ABC",
        "numero": "123",
        "bairro": "XYZ",
        "cidade": "Alpha"
    }],
    "intesses": ["kart", "culinária"],
    "reservas": [
        ObjectID("dsada"), ObjectID("fdsfds") 
    ]
}
```

Destinos:

```JS
{
    "_id":1,
    "nome": "Parque Ibirapuera",
    "descricao": "Principal parque de São Paulo",
    "localizacao":{
        "type": 'Point',
        "coordinates": [-46.661056, -23.587384]
    }
}
```

### 1.2.4 Estratégias de modelagem de dados eficientes e escaláveis

#### Modelagem orientada por consultas

* A modelagem de dados no MongoDB deve ser orientada pelas consultas que serão realizadas com mais frequências

#### Inner Documents

No MongoDB, é comum **denormalizar** os dados para evitar operações de junção (join) custosas.  

Isso significa que os dados relacionados podem ser armazenados juntos em um único documento, em vez de serem distribuídos em várias coleções.

##### Modelar usuário com estragégia desnormalizada

<https://jsonformatter.curiousconcept.com>

```js
{
    "_id":1,
    "nome": "Erick",
    "idade": 31,
    "data_nascimento":"1994-06-01",
    "endereco": "Rua ABC, 123...",
    "enderecos": [{
        "logradouro":"Rua ABC",
        "numero": "123",
        "bairro": "XYZ",
        "cidade": "Alpha"
    }],
    "intesses": ["kart", "culinária"],
    "reservas": [ {
        "data": "2023-10-10",
        "status": "pendente",
        "destino": ObjectId("123")
    } ]
}
```

##### ✅ Quando usar o Inner Documents

* Os dados aninhados são específicos para o documento pai
* Os dados aninhados são sempre acessados juntamente com o documento pai
* A cardinalidade do relacionamento é um-para-muitos (um usuário pode ter várias reservas)

##### ❌ Quando não usar o Inner Documents

* Se os dados aninhados precisarem ser consultados e atualizados independetemente do documento pai, é mais adequado utilizar coleções separadas.

#### Referências

* Forma de relacionar os documentos entre si

##### Modelar usuário com estratégia de referências

```js
{
    "_id":1,
    "nome": "Erick",
    "idade": 31,
    "data_nascimento":"1994-06-01",
    "endereco": "Rua ABC, 123...",
    "enderecos": [{
        "logradouro":"Rua ABC",
        "numero": "123",
        "bairro": "XYZ",
        "cidade": "Alpha"
    }],
    "intesses": ["kart", "culinária"],
    "reservas": [ ObjectcID("123"), ObjectcID("124") ]
}
```

ou pode guardar os usuários nas reservas:

```js
{
    "_id": ObjectId("123"),
    "destino": Object("456"),
    "data": "2023-10-10",
    "status": "pendente",
    "usuario": ObjectID(345)
}
```

##### ✅ Quando usar

* Os dados têm seus próprio significado e podem ser acessados independentemente do documento pai
* Os dados têm uma cardinalidade mais alta (por exemplo, vários usuários podem ter reservas)

#### ❌ Quando não usar

* Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas.

<https://www.luiztools.com.br/post/padroes-para-modelagem-de-dados-documentos-em-mongodb/>

## 1.3 Operação no MongoDB

### 1.3.1 Operação no MongoDB

<https://www.mongodb.com/docs/compass/master/install/>

**Compass** permite se conectar com o mongodb e permite criar um database e editar...

`use {{nome_do_banco}}`

Se não existir, ele cria o banco.  
Se já existir, ele acessa o banco.  

Enquanto o database não tiver uma `collection` ele não será apresentado na lista do compass.

No **Compass** → Menu Lateral Esquerdo - Databases `+`:

* Database Name: teste
* Collection Name: teste

ou **linha de comando (compass)**: `use viagens> db.usuarios.insertOne({})`.  
Neste criado cria o collections `viagens` com uma database chamada `usuarios`.

Ou no **Atlas**:

* Menu de topo - Data Services  
* Menu lateral - Deployment / Database  
`[Add My Own Data]` ??

* Dabase name: viagens2
* Collection name: destinos
* `[Create]`.  

#### Criando uma collection

**Compass**:
`db.createColletcion("usuarios")`
`db.createColletcion("destinos")`

No **Atlas** tem um `+` e só preencher os valores.

#### Inserindo Documentos

`db.usuarios.insertOne({});`
`db.usuarios.insertMany([{}]);`

Exemplo:

```mongodb
db.usuarios.insertOne({
    "nome": "Pamela",
    "email": "pamela.apolinario@yahoo.com",
    "idade": 30
})
```

#### Consultando Documentos

* `db.usuarios.find({})` - ache a quantidade de referencia com base na nossa busca
* `db.usuarios.findOne({})` - traz a 1° referência que encontrar na nossa colection com base no nosso critério de busca
* `db.usuarios.findOneAndUpdate({},{})` - consegue passar nosso critério de busca, qual a atualização, e já retorna o dado que foi alterado.
* `db.usuarios.findOneAndDelete({})` - exclui mas retorna os dados e registros que foram excluídos.

Prática:

Trazendo todos os usuários:  
`db.usuarios.find({})` → retorna todos os dados.

Agora quero todos os usuários chamados João:  
`db.usuarios.find({"nome": "João"})`

Agora quero um usuários chamados Pamela (primeiro):  
`db.usuarios.findOne({"nome": "Pamela"})`

Agora quero atualizar o nome da 1° Pamela que localizar:  
`db.usuarios.findOneAndUpdate({"nome": "Pamela"}, {$set: {"nome": "Pamela Apolinario"}})`

Deletando Pamela Apolinario:  
`db.usuarios.findOneAndDelete({"nome": "Pamela"})`

Adicionando nos usuários Pamela um contador de viagens:  
`db.usuarios.UpdateMany({"nome":"Pamela"}, {$set: {"viagens": 0}})`

Vamos supor que toda alteração que fizermos na Pamela está relacionado a uma viagem, vamos **incrementar** o contador:  
`db.usuarios.UpdateMany({"nome":"Pamela"}, {$inc: {"viagens": 1}})`

Adicionando um array de interesses na Pamela:  
`db.usuarios.UpdateMany({"nome":"Pamela"}, {$set: {"interesses": ["culinaria"]}})`

Vamos dar um **push** nessa lista de interesses:  
`db.usuarios.UpdateMany({"nome":"Pamela"}, {$push: {"interesses": "cerveja"}})`

#### Excluindo Documentos

* `db.usuarios.deleteOne({})`
* `db.usuarios.deleteMany({})`

Exemplos:

Vamos deletar o João (um):  
`db.usuarios.deleteOne({"nome": "João"})`

### 1.3.2 Consultas Simples Operadores

#### Igualdade

Realizar consultas baseadas em um valor específico para um campo.

`db.usuarios.find({"endereco.cidade":"São Paulo"})`

#### Operados Lógicos

Realizar consultas baseadas em um valor específico para um campo.

* `$and`
* `$or`
* `$not`

#### Operadores de Comparação

* `$eq` ==
* `$ne` !=
* `$gt` >
* `$gte` >=
* `$lt` <
* `$lte` <=
* `$in` [] - verificar dentro de um array
* `$nin` [] - negação do in no array

#### Projeções

Definir quais campos devem ser retornados em uma consulta.

#### Ordenação

Ordenar os resultados de uma consulta com base em um ou mais campos.

#### Limitação

Limitar o número de documentos retornados em uma consulta

#### Paginação

`db.usuarios.find().skip(10).limit(5)`

#### Mão na Massa

Usando `$and`:

`{idade: 20, nome: "Carlos"}`

ou

`{$and: [{idade: 20}, {nome: "Carlos"}]}`

ou

`{$and: [{idade: {$eq: 20}}, {nome: "Carlos"}]}`

Vamos usar o `$or`:

`{$or: [{idade: 20}, {nome: "Carlos"}]}`

Vamos usar comparação:

`{idade: {gte: 18}}` - pegar todos os usários com 18 ou mais anos.

`{idade: {$not: {$eq: 30}}}` == `{idade: {$ne: {$eq: 30}}`

Vamos supor que queiramos mostrar os resultados de todos que moram em São Paulo ou Belo Horizonte:

`{$or: [{cidade: "São Paulo"}, {cidade: "Belo Horizonte"}]}`

ou

`{cidade: {$in: ["São Paulo", "Belo Horizonte"]}}`

Projeção:

`db.usuarios.find({cidade: {$nin: ["São Paulo", "Belo Horizonte"]}}, {nome: 1})`

Ou seja, só vai trazer resultado de `nome` para a nossa consulta.  

Usando Sort:  

`{nome: 1}` - ascendente
`{nome: -1}` - decrescente (maior para menor)

`{idade: 1, nome: -1}` - ordenada primeiro pela idade e no empate pelo nome

`db.usuarios.find({cidade: {$in: ["São Paulo"]}}, {nome:1}).sort({idade:1})`

#### GitHub com os Códigos

<https://github.com*pamelaborges/dio-db-nosql>

## 1.4 Breve apresentação do Redis

### 1.4.1 Introdução ao Redis

#### O que é o Redis?

O Redis é um sistema de armazenamento de dados em memória de alto desempenho.

#### Principais Características do Redis

* armazenamento em memória
* estrutura de dados versátil
* operações atômicas
* cache de alto desempenho
* Pub/Sub (Publicação / Assinatura)

#### Principais utilizações do Redis

* Cache de dados
* Filas de mensagens
* Contagem de acesso e estatísicas em tempo real
* Gerenciamento de sessões
* cache de resultados de consultas

#### Principais comandos

* `SET`
* `GET`
* `DEL` - deletar
* `EXISTS` - se já existe uma chave no Redis
* `KEYS` - usando patterns, retornas chaves correspondentes
* `INCR`
* `DECR`

<https://try.redis.io>

`SET nome "Pamela"`  
`SET nome_2 "João"`  
`GET nome` → "Pamela" P.S: Não dá pra pesquisar com base no valor, só com a chave  
`KEYS nome*` → "nome" e "nome_2"  
`SET nome_3 "Maria"`  
`DEL nome_3"` → 1 (Excluído 1 valor)  
`EXPIRE nome_2 10` - exclui daqui 10 segundo  
`TTL nome_2` - retorna o tempo (segundos) de vida  
`SET acessos 1`  
`INCR acessos` → agora acessos retorna 2  
`DECR acessos` → agora acessos retorna 1  
`LPUSH usuarios "Pamela" "João" "Maria"` - cria um array de usuarios  
`LRANGE usuarios 0 -1` - retorna todo o array desde a posição 0 até o -1 (último valor)  
`LPUSH usuarios "Rebeca"` - Adiciona a Rebeca  
`LLEN usuario` → 4 (tamanho da lista)  
