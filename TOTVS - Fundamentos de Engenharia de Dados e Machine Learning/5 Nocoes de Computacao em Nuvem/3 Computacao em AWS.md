# 3 Computação em AWS

## 3.1 Elastic Compute Cloud - EC2

Num cenário real:

Tem uma API para prover um site ou aplicativo. Vamos colocar num servidor!

Vamos montar um datacenter!

Mas precisa de infraestrutura, rede, energia, analistas de segurança, refrigeração...é caro mesmo!

E se...

* Todo esse investimento não for necessário para a demanda?
* Um dia o negócio crescer e a infraestrutura não suportar a demanda de usuários?

Então seria ideial:

* Economia de recursos e custos
* Escalabilidade
* Elasticidade (atender a demanda)
* Dispononibilidade

### 3.1.1 EC2 - Elastic Compute Cloud

* Capacidade computacional segura e redimensionável
* Computação: CPU, Memória, Rede, Armazenamento, Sistema  operacional
* Definição de preço conforme uso e modalidades específicas a necessidade
* Instâncias com tipos otimizados para sua atividade

Cada um desses servidores são chamadas de **instância**

### 3.1.2 Tipos de instância

* Uso geral (a mais padrão/básica/equilibrada)
* Otimizadas para computação (uso geral ++)
* Otimizadas para memória (alto processamento na memória, tratamento em streaming)
* Computação acelerada (cálculos e processamentos de gráficos)
* Otimizadas para armazenamento (para sistema de arquivos, warehouse)

## 3.2 Amazon EC2 AutoScalling

Vamos imaginar um e-commerce e os servidores trabalham com sazonalidade, seja ao longo do dia, ao longo da semana, ao longo do ano...

Se escalar para a maior capacidade, acaba ocorre uma subdimensionamento, pagando a mais por recurso que acaba não utilizando (em baixa demanda)

Se escalar para uma capacidade média, na maior demanda pode ocorrer problemas no servidor (carregamento nos apps dos clientes)

Solução: Escalar conforme necessidade!

### 3.2.1 Amazon EC2 AutoScalling

* Provê escalabilidade horizontal para seus serviços
* Melhora a tolerância a falhas com identificação de instâncias indisponíveis e implantação multi-AZ
* Melhor gerenciamento de custos

### 3.2.1 Como é a configuração

* Tamanho mínimo, quantidade mínima de instância rodando
* Qual capacidade desejada.
* Se precisar, quantas vou precisar?
* Quantidade máxima de instâncias.

### 3.2.2 Abordagem

* Scalling Preditivo (a partir de modelos de previsão)
* Scalling Dinâmico (a partir de métrica. Ex: CPU > 80%)
* Combinado

## 3.3 Elastic Load Balancing - ELB

Cenário de contexto:

Vamos imaginar um app com quantidade de 200 mil usuários sendo processados em 5 instâncias EC2.

E vamos precisar dobrar as instância devido a uma campanha promocional.

Mas como coordenar e distribuir a demanda dos processamentos entre todas as instâncias?

**ELB** é um algoritmo que distribui as cargas de processamentos entre as instâncias.

* É um balanceamento de carga de aplciação, gateway e rede
* Escopo regional
* Escala de forma automática, sem custos
* Junto ao EC2 AutoScaling permite criar aplicações altamente disponíveis.

## 3.4 Serviço de mensageria

Imagine que, há diversos micro-serviços (aplicação): de compra, de fraude, de e-mail.

Princípio de desacoplar

**SQS** é um serviço de fila de forma assíncrona.

Vamos supor que os usuários fizeram uma compra, e então essas transações passam para o microsserviço de fraude, acumulando em uma fila.

O ms-fraude vai realizando o análise e vai esvaziando a fila.

**SNS** também um serviço de mensageria, no caso é possível linkar para disparo de e-mail, notificação, etc.

### 3.4.1 Amazon Simple Queue Service - SQS

* Sistema de enfileiramento de mensagens
* Um usuário envia uma mensagem para fila, o outro usuário lê, processa e a exclui da fila

### 3.4.2 Amazon Simple Notification Service - SNS

* Sistema pub/sub
* Utiliza tópicos como estrutura
* Usário publica mensagens no tópico e assinantes escutam

## 3.5 Computação sem servidor

* Também chamado por *Servless*
* O termo "sem servidor" significa que o código é executado em servidores sem que você precise provisionar ou gerenciar esses servidores.
* Capacidade automaticamente ajustada pelo serviço, sem necessidade de nenhuma configuração

### 3.5.1 AWS Lambda

* Execução de código sem provisionar servidores
* Código organizado em funções
* Você pode escolher a linguagem de programação de sua preferência
* Executa a partir de eventos ou chamadas diretas a API do Lambda
* Você escreve o código e publica (sem configurar o servidor)

### 3.5.2 Como funciona?

* Faz o upload do seu código
* Configura a trigger - o que dispara a execução do código (quando houver um upload de arquivo, chamada HTTP)
* Executa de forma automática
* Todo o recurso de computação é usado
* Só se paga pelo recurso e tempo de CPU

## 3.6 Containers em AWS

### 3.6.1 Containers

* Forma padrão de empacotar seu aplicativo em um único objeto
* Executados como processos isolados
* Exemplo: Docker - construir ou usar imagens prontas (baixa e executa, sem precisar configurar banco de dados, etc)

Começa-se construindo a imagem (se configura apenas uma vez)

### 3.6.2 ECR - Elastic Container Registry

Você coda uma imagem docker, ele armazena os versionamentos das suas  versões de imagens.

### 3.6.2 ECS - Elastic Container Service

Escreve o docker file, empacota a aplicação do servidor, publica no ECR e **executa**-o pelo ECS.

### 3.6.3 EKS - Elastic Kubernetes Service

Provisiona um cluster EKS, faz o deploy dos seus containers, conecta com o EKS e consegue rodar suas aplicações.

### 3.6.4 AWS Fargate

Ferramenta servless que escolhe entre ECS ou EKS e passa a ter uma facilidade para executar as aplicações.
