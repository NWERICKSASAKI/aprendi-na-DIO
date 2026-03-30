# 1 Fundamentos de ETL com Python

## 1.1 Fundamentos de ETL

### 1.1.1 Apresentação

Os processos de ETL (*Extract, Transform and Load*) envolvem ferramentas de software voltadas para a extração de dados de diversos sistemas e, também, a transformação desses dados conforme regras de negócios bem definidas e, por fim, o carregamento dos dados para um *Data Mart* e/ou *Data Warehouse*.

### 1.1.2 Introdução para ETL

ETL é um tipo de *data integration* em três etapas (extração, transformação e carregamento dos dados) usado para combinar dados de diversas fontes.

Ele é comummente utilizado para construir um *data warehouse*.

* Extract - importar daos de diversos formatos, como: pasta de trabalho, diversos bancos de dados, CSV, TXT, JSON, etc.
* Transform - Transformar colunas, linhas, Tipos de Dados, Mesclar, Acrescentar, Listas e Tabelas
* Load - Carregar para o modelo de dados na nuvem, em banco de dados, etc.

ETL são ferramentas de software cuja função é a extração de dados de diversos sistemas, transformação desses dados conforme regras de negócios e por fim o carregamento dos dados geralmente para um *Data Mart* e/ou *Data Warehouse*.

Nesse processo, os dados são retirados (**E**) de um sistema-fonte, convertidos (**T**) em um formato que possa ser analisado, e armazenados (**L**) em nuvem ou outro sistema.

Extração, carregamento, transformação (**ETL**) é uma abordagem alternativa, embora relacionada, projetada para jogar o processamento para o banco de dados, de modo a aprimorar a performance.

Existem muitas **ferramentas de ETL** disponíveis no mercado como:  

* IBM information Server (Data Stage),
* Oracle Data Integrator (ODI),  
* Informatica Power Center,
* Microsoft Integration Services (SSIS)

Existem também um conjunto de **Ferramenta de ETL Open Source** como:

* PDI - Pentaho Data Integrator
* Talend ETL

O **processo de ETL** abrange alguns passos importantes. Como exemplo, podemos considerar um banco de dados de clientes especiais com todas as informações essenciais.

No mapeamento, a **extração** de origem debe conter a especificação de identidade e seus atributos detalhados, tudo armazenado numa zona temporária. Quando forem efetuadas as análises e filtragens dos dados, a nova versão poderá ser comparada com a cópia da versão prévia.

A **transformação** inclui *limpeza*, *racionalização* e *complementação* dos registros. O processo de limpeza removerá erros e padronizará as informações. O processo de complementação implicará no acréscimo de dados.

### 1.1.3 Etapas para ETL

#### 1.1.3.1 Extract

O processo de **extração** de dados consiste em se comunicar em outros sistemas ou banco de dados para capturar os dados que serão inseridos no destino, seja uma *Stagin Area* ou outro sistemas.

#### 1.1.3.2 Transform

O processo de **transformaçao** de dados é composta por várias etapas: padronização, limpeza e qualidade. Dados vindoss de sistemas diferentes tem padrões diferentes seja de nomemclatura ou mesmo de tipos de dados (*VARCHAR2* Oracle ou *VARCHAR* Sql Server). 

#### 1.1.3.3 Load

O processo de **carregamento** de dados é a etapa final onde todos os dados são lidos das área de *staging* e preparação de dados, carregados no *Data Warehouse* ou *Data Mart* Final.

#### 1.1.3.4 Algumas vantages para ETL

* **Garantia significativa da qualidade dos dados** - As ferramentas de ETL, através de sequências de operações e instruções tem condições de solucionar problemas de maior complexidade.
* **Funcionalidade de execução** - As ferramentas de ETL já possui funções específicas, sendo necessária apenas a atenção no fluxo de dados.
* **Desenvolvimento das cargas** - Mesmo que o usuário não seja técnico poderá desenvolver uma rotina de carga em uma ferramenta de ETL, devido a facilidade e rapidez para codificação.
* **Manutenção das cargas** - As tarefas de manutenção de uma rotina de carga são mais simples de realizar em relação à manutenção de código.
* **Metainformação** - Os metadados (informações úteis para identificar, localizar, entender e gerenciar os dados) são gerados e mantidos de forma automática com a ferramenta, evitando problemas de geração de informações incorretas na finalização do processo.
* **Performance** - Os metódos mais usados para trabalhar com grande volumes conseguem extrair, transformar e carregar dadoc om maior velocidade e menos recurso, como gravações em bloco e operações não logadas.
* **Transferência** - Ferramentas de ETL podem ser deslocadas de um servidor mais facilmente ou distribuídas entre vários servidores.
* **Conectividade** - A conexão de uma ferramenta de ETL com múltiplas fontes de dados é transparente. Caso sejamm precisas mais fontes como o SAP, VSAM, MainFrame ou qualquer outra, basta a aquisição do conector sem a necessidade de codificar um.
* **Reinicialização** - Ferramentas possuem a capacidade de reinicar a carga onde pararam sem a necessidade de codificação.
* **Segurança e Estabildiade** - É possível articular melhor a segurança tornando-o mais modular, dividindo as finalidades (criação de cargas, execução de cargas, agendamento, etc).

### 1.1.4 Ferramentas aplicadas para ETL

As ferramentas são *software* utilizados para facilitar o processo de integração de dados.

Inicialmente muito usados em projetos de *Data Warehouse* e *Business Intelligence* em geral, ultimamente tem sido utilizados em processos de integração de software, banco de dados, etc.

Existem diversas ferramentas de ETL, como:

* IBM Data Stage
* Power Center
* Sql Server Integration Sergvices
* Talend ETL

Hoje com o crescimento dos projetos de **Big Data** aumenta-se mais ainda a necessidade de fazer ETL entre plataformas heterogêneas, para isso, projetos como o *Hadoop*, possuem ferramentas próprias para carga de dados, como:

* **SQOOP** - Ferramenta para movimentar dados dentre bancos de dados relacionais e o ambiente *Hadoop*.
* **HIVE** - Ambiente de SQL sobre um cluster *Hadoop*.
* **PIG** - Ferramenta de script para transformação e processamentos de dados.
* **SPARK** - Framework de processamento em memória.

**Hadoop** é uma plataforma de software em Java de computação distribuída voltada para cluster e processamentos de grandes volumes de dados, com atenção a tolerância a falhas.

Masmo com todas as possibilidades acima, vemos as ferramentas de ETL se adapatando para **Big Data** ou gerando códigos para serem rodados nessas ferramentas do Ecossistema Hadoop.

Em Big Data, o processo de carga também é conhecido como Ingestão de Dados, que geralmente é a primeira parte da carga (extract) a parte mais simples do processos, que consiste em extrair dados dos sistemas de origem e trazer para dentro do Data Lake ou ambiente de dados utilizados.

### 1.1.5 Introdução à biblioteca Pandas

De forma simples: Manipulação de dados estruturado como é feito no Excel.

O pandas permite trabalhar com diferentes tipos de dados, por exemplo:

* Dados tabulares, como uma planilha Excel ou uma tabela SQL.
* Dados ordenados de modo temporal ou não
* Matrizes
* Qualquer outro conjunto de dados, que não necessariamente precisem estar rotulados

Estrutura de dados:

* Os dois principais objetos da biblioteca de Pandas são as **Series** e os **DataFrames**.
* **Serie** é uma matriz unidimensional que contém uma sequência de valores que apresentam uma indexação (que podem ser numéricos inteiros ou rótulos), muito parecida com uma única coluna no Excel.
* **DataFrame** é uma estrutura de dados tabular, semelhante a planilha de dados no Excel, em que tanto as linhas quanto as colunas apresentam rótulos.

### 1.1.6 Biblioteca Pandas e suas funções

Todos os dados ausentes nas nossas DataFrames são substituídos por `NaN`.  

`df.head(n=4)`  

`df.shape` → (549,7)  

`df.info()` - para saber que formato se encontra os dados em cada coluna, além da quantodade de memória para ler esse conjunto de dados.

`df.isnull().sum()` → quantos dados faltantes tem no nosso df.

`df['setor'].unique()` → verificar quaos valores únicos existem naquela coluna

`df['setor'].value_counts().plot(kind='bar')` → visualização simples  e rápida

### 1.1.7 Introdução à biblioteca Scikit Learn

Dá suporte a implementação de ML.  

Busca eurística: a solução que vou buscar não é determinística, ou seja, várias possibilidades atendem minha resposta, mas que não há tempo de olhar todos os grupos.  

Esta biblioteca dispões de de ferramentes simples para análise preditiva de dados, é reutilizável em diferentes situações, possui código aberto, sendo acessível a todos e foi construída sobre os pacotes **NumPy**, **SciPy** e **matplotlib**.

Neste exemplo iremos criar uma massa de dadso com 200 observações, com apenas uma variável preditora, que será a variável `x` e a variável target, que sera a `y`. Para isso indicamos os parâmetros `n_samples = 200` e `n_features = 1`. O parâmetro `noise` define o quão dispersos os dados estarão um dos outros.

```py
from sklearn.datasets import make_regression

x,y = make_regression(n_samples=200, n_features=1, noise=30)
```

Utilizando o pacote `matplotlib`, com o móduglo `pyplot` e a função `scatter()`, que criará o gráfico, e a função `show()` que o exibirá na tela.

```py
import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.show()
```

Com os dados gerados, já podemos iniciar a criação de nosso modelo de *machine learning*.

Para isso utilizaremos o módulo `linear_model`, e a função `LinearRegression()`.

```py
from sklear.linear_model import LinearRegression

modelo = LinearRegression()
```

Após esta execução, o objeto modelo que acamos de criar está pronto para receber os dados que darão origem ao modelo.

Como não indicamos nenhum parâmetro específico na função, estamos utilizando suas configurações padrão.

Agora preciamos apenas apresentar os dados ao modelo, e para isso temos o método `fit()`. Na documentação da função podemos conferir todos os métodos que ela possui.

Após esta etapa, nosso modelo de *machine learning* está pronto e **podemos utilizá-lo para prever dados desconhecidos**.

Simplificando este primeiro entendimento, vamos apenas visualizar a **reta de regressõa linear** que o modelo gera, com os mesmos dados que criaram o modelo.

Para isso iremos utilizar o método `predict()`, indicando que queremos aplicar a previsão nos valores de `x`.

O resultado do método será uma previsão de `y` para cada valor de `x` apresentado.

`modelo.predict(x)` → retorna um array carregado cheio de elementos, que representa a população.

A função `plot()` do pacote `pyplot` gera uma reta com os dados apresentados. Como já temos os dados de `x` e `y`, basta indicá-los na função. 

Assim, primeiramente montamos novamente o gráfico de `x` e `y` original com a função `scatter()`, e somamos a ele a reta de

### 1.1.8 Manipulando Dados com Pandas em Python

```py
import pandas as pd
url = 'https://raw.githubcontent.com/Muralimekala/python/master/Resp2.csv'
df1 = pd.read_csv(url)
```

```py
import pandas as pd
url = 'https://raw.githubcontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
sf.head()
```

### 1.1.9 Framework Luigi para ETL com Python

Utiliza pandas, numpy, matplotlib, scikit learning, etc.

Este framework foi desenvolvido para ser de código-aberto.

**Luigi é um framework** de execução criado pelo **Spotify** que cria pipelines de dados em Python.

É um pacote Python (2.7, 3.6, 3.7 testado) que ajuda a construir pipelines complexos de trabalhos em lote.

Ele lida com resolução de dependências, gerenciamento de fluxos de trabalho, visualização, tratamento de falhas, integração de linha de comando e muito mais.

**Target**: Em palavras simples, um alvo contém a saída de uma tarefa. Um destino pode ser local (por exemplo: um arquivo, MySQL etc)

**Task** - Tarefa é algo onde o trabalho real ocorre. Uma tarefa pode ser independete ou dependente. O exemplo de uma tarefa dependente é despejar os dados de um arquivo ou bando de dados. Antes de carregar os dados, os dados devem estar lá por qualquer meio (scrapping, API, etc). Cada tarefa é representada como uma classe Python que contém certas funções-membro obrigatórias. Uma função de tarefa contém os seguintes métodos:

* `require()` - esta função membro da classe `task` contém todas as instâncias de tarefas que devem ser executadas antes da tarefa atual.
* `output()` - este método contém o destino a saída da tarefa será armazenada. Isso pode contar um ou mais objetos de destino.
* `run()` - este método contém a lógica real para executar uma tarefa.

<https://luigi.readthedocs.io/en/stable/>

Para instalação: `pip install luigi`

No terminal do python só executar `luigid` depois acessar o `localhost:8082`.
