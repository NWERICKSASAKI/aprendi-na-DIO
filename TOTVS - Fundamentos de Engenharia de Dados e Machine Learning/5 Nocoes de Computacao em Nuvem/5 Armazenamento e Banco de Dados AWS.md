# 5 Armazenamento e Bando de Dados AWS

## 5.1 Armazenamento de dados em nuvem

E os dados? O quê, onde e como estão armazenados?

Está relacionado como vai armazenar informações, são eles:

* De objetos (*Object Storage*)
* De arquivos (*File Storage*)
* De blocos (*Block Storage*)

### 5.1.1 Armazenamento de Objetos

* Gravar dados como objetos, ou seja, além do arquivos tem metadados (url, permissões).
* Dados não estruturados
* Casos de uso: Data lakes, Mídias, Backup

### 5.1.2 Armazenamento de Arquivos

* Sistema de arquivos compartilhados
* Permite acesso por meio de servidores, aplicações e usuários
* Analogia com pastas compartilhadas em uma rede
* Casos de uso: Ferramentas de desenvolvimento, Diretórios pessoais.

### 5.1.3 Armazenamento de Blocos

* Armazenamento de blocos: HDD, SSD
* DIspositivo com diferentes configurações de Leitura e Escrita
* Casos de uso: Máquinas virtuais, contêiners, banco de dados.

## 5.2 Amazon Elastic Block Storage - EBS

Quando a gente usa o EC2, cria uma instância para rodar alguma aplicação, não estamos usando um espaço físico dedicado, ele usa uma virtualização (há várias instâncias no mesmo computador).

### 5.2.1 Volume Instance Store

É basicamente um HD (ou memória né) da máquina que roda as instâncias EC2.

Quando você inicia uma instância EC2, ele se associa a um dos HD, mas nas próximas vezes, pode ser que seja com algum outro HD.

* Armazenamento de Blocos
* Discos anexados fisicamento ao computador host
* Ideal para dados de armazenamento temporário como buffers, cache, rascunhos

Esses dados serão perdidos se:

* Falha de disco de uma unidade
* Instância parada
* Instância hibernada
* Instância encerrada

### 5.2.2 EBS - Amazon Elastic Block Store

Você anexa um volume (disco) dedicado à instância EC2.

* Armazenamento em blocos
* Bloco (*block*) = HD Físico
* Projetado para Amazon Elastic Compute Cloud (EC2)
* HDs são chamados de "volume"

Como funciona:

* Define o tipo de volume
* Escolhe o tamanho e configurações
* Anexa o voluma a uma instância EC2

São dados permanentes, não perde ao desligar o EC2.

Você pode escolher usar HDD ou SSD, cada um com duas classes.

#### 5.2.2.1 HDD

É Mais barato, porém mais lento

* HDD Thoughput Optimizes - 
* HDD Cold -

#### 5.2.2.2 SSD

Mais rápido, porém mais caro

* SSD General Purpose - SSD para usos gerais
* SSD Provisioned IOPS - SSD com alta velocidade para entrada e saída de dados

### 5.2.3 Como funcionam os backups (snapshots)

Oa backups são incrementais.

Exemplo:

* 1° dia - grava todo o HD (ex: +10 GB)
* 2° dia - grava apenas aquilo que foi modificado (ex: +0, mas 2GB foi alterado)

## 5.3 Amazon S3 - Simple Storage Service

Serviço de armazenamento de objetos

O que é um objeto no S3?

É um dado de qualquer tipo (ou extensão) e possuí:

* Valor ou Dados (o conteúdo)
* Metadados (tipo, formato, encode, tags)
* Chave (nome que você atribui ao objeto)

Onde estão os objetos?

O S3 grava os objetos num *Bucket* (balde) - uma analogia ao HD.

### 5.3.1 Buckets S3

* Antes de um upload dos seus objetos, você precisa criar um
* É um contêiner para objetos armazenados no Amazon S3
* Você pode armazenar qualquer número de objetos em um bucket
* Objetos podem ter de 0 **até 5 TB** de tamanho
* Você pode **ter até 100 buckets** na sua conta
* Pode controlar acesso por objeto
* Pode utilizar versioanamento de objetos

Casos de uso:

* Data lakes
* Arquivamento de dados
* Hospedagem de sites estáticos

### 5.3.2 Classes de armazenamento

* Categorias para adequar melhor as necessidade de negócios e custo
* Fatores importante na seleção de uma categoria:

1. Com que frequência você planeja recuperar seus dados?  
2. Seus dados precim estar muito ou pouco disponíveis?  

* S3 Standard
* S3 Standard-Infrequent Access (S3 Standard-IA)
* S3 One Zone-Infrequent Access (S3 One Zone-IA)
* S3 Intelligent-Tiering
* S3 Glacier Instant Retrieval
* S3 Glacier Flexible Retrieval
* S3 Glacier Deep Archive

#### 5.3.2.1 S3 Standard

* Projeto para dados acessados com frequência
* Armazena dados em um mínimo de 3 Zonas de Disponibilidade
* Boa esolha para diversos casos de uso: sites, distribuição de conteúdo e análise de dados.
* Custo mais alto

#### 5.3.2.2 S3 Standard-Infrequent Access (S3 Standard-IA)

* Semelhante ao S3 Standard
* Armazena dados em um mínimo de 3 Zonas de Disponibilidade
* Ideal para dados acessados com pouca frequência
* Taxa por GB de armazenamento e recuperação mais baixo

#### 5.3.2.3 S3 One Zone-Infrequent Access (S3 One Zone-IA)

* Tem um preço de armazenamento menor do que o S3 Standard-IA
* Armazena dados em um única Zona de Disponibilidade

#### 5.3.2.4 S3 Intelligent-Tiering

* Ideal para dados com padrões de acesso desconhecidos ou em alteração
* Gerencia automaticamente o ciclo de vida dos objetos armazenados otimizando custos
* Requer uma pequena taxa mensal de monitoramento e automação por objeto

Exemplo:
Começa no **S3 Standard** → 30 dias sem acesso **Infrequent Access** → 90 dias sem acesso **Archive Instant Access**

#### 5.3.2.5 S3 Glacier Instant Retrieval

* Ideal para dados de longa duração, raramento acessados mas que exigem recuperação rápida (milissegundos)
* Oferece acesso tão rápido quanto Standard e Standard-IA (*infrequent access*)
* Ideal para dados acessados uma vez por trimestre

#### 5.3.2.6 S3 Glacier Flexible Retrieval

* Para dados que não requerem acesso imediato
* Ideal para casos de uso de backups não urgentes, recuperação de desastres
* Usuário pode escolher qual velocidade de recuperação
* Ideal para dados acessados 1 ou 2 vezes por ano

#### 5.3.2.7 S3 Glacier Deep Archive

* Suporte a retenção a preservação digital de longo prazo para dados que pode ser acessados 1 ou 2 vezes por ano
* Ideal para empresas que precisam manter dados por conformidade legais por 7 ou 10 anos
* Recuperação de dados em até 12 horas

## 5.4 EFS - Amazon Elastic File System

* Fornece um sistema de arquivos
* Servless e totalmente elástico
* Escala até Petabytes
* Aumenta e diminui confirme adição e remoção de arquivos
* Compatível com protocolo NFS (Network file System)
* Pode ser acessado por EC2, Lambda, ECS
* Acesso simultâneo ao mesmos dados sem problemas de performance

### 5.4.1 Classes de Armazenamento

* Padrão (Instância regional): Standard e Standard - IA (Infrequent Access)
* Uma AZ: One Zone e One Zone - IA

### 5.4.2 Casos de uso

1 VPC rodando uma instância em 3 AZ e apenas um EFS.

## 5.5 Amazon Relational Database Service (RDS)

Como usar Banco de dados relacionais na nuvem?

* Daria pra montar um DB em um EC2 - mas desta você usa e gerencia (backup, controlar armazenamento, controlar recursos da máquina EC2, um DBA)

### 5.5.1 RDS

* Facilita configurações e provisionamento de hardware
* Patches automatizados
* Backups
* Redundância
* Failover e Recuperação de Desastres
* Compatível com MySQL, PostgreSQL, MariaDB, etc.

### 5.5.2 Amazon Aurora

* Servless
* Mecanismos compatíveis: PostgresSQL e MySQL
* Preço 1/10 de outros vendors
* Replicação multi-regional
* Até 15 réplicas de leituras
* Backups contínua via S3

## 5.6 DynamoDB

* Banco de dados não relacional (NoSQL)
* Gerenciado (Servless) - não precisa se preocupar com configuração e escalabilidade
* Performance abaixo de 10 milissegundos
* Escala automaticamente
* Replicação de dados regional
* Casos de uso: Muitos dados, baixa latência

## 5.7 Outros serviços de banco de dados

A escolha do BD correto:

"A necessidade de negócio escollhe o tipo de banco de dados"

### 5.7.1 Amazon DocumentDB

* Banco de dados de documentos
* Gerenciamento de conteúdo
* Catálogos, perfis de usuário
* Compatível com cargas de trabalho MongoDB

### 5.7.2 Amazon Neptune

* Redes sociais, mecanismos de recomendação, detecção de fraude e gráficos de conhecimento
* Banco de dados de grafos

### 5.7.3 Amazon QLDB

* Quantum Ledger Database
* Banco de dados serviço ledger
* Imutabilidade (uma vez inserido não pode sofrer alteração)

### 5.7.4 Amazon DynamoDB Accelerator

* Também chamado de DAX
* Camada de cache nativa para otimizar tempo de leitura de dados

### 5.7.5 Amazon Elasticache

* Camada de cache sobre banco de dados
* Compatível com Redis e Memcached

## 5.8 Big data com Amazon Redshift

Contexto: Vivemos num mundo de cada vez mais dados...

* Velocidade de geração de dados
* Variedade de fonte de dados
* Quando os dados precisam responder com inteligência de negócios

Exemplo:

* EC2 → S3 Buckets → Lambda → DynamoDB
* Desktop/Celular → EC2 → RDS
* Escritório → EC2 → EFS

Com inúmeros tipo de dados: doc, powerpoint, planilhas, vídeo, pdf e etc.

Quantas vendas foi feita desde o lançamento?  
Quantos cadastros teve na última hora?  

### 5.8.1 Amazon Redshift

* Serviço de Data warehouse para análise de Big Data
* Oferece coletar informações de muitas fontes de dados
* Projeta relações e tendências de dados
* Usando Redshift Spectrum é possível rodar comandos SQL em cima de todas as fontes de dados agrupadas
* Funciona como um cluster de nós

