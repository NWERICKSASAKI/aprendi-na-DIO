# 2 Infraestrutura Global AWS

## 2.1 O que é Infraestrutura Global AWS

* Infraestrutura de datacenters em todo o mundo que fornecem os diversos serviços que pode utilizar na AWS.
* Composto por Regiões e Zonas de disponibilidade.
* Vantagens: Alta disponibilidade, Tolerância a falhas.

## 2.2 Regiões e Zonas de disponibilidade

Regiões:

* São locais onde são hospedados os data centers da AWS
* Cada região possuem locais isolados chamados Zonas de Disponibilidade
* Todas as regiões são conectadas com rede de alta velocidade
* Isolamento de dados
* Regulação de dados local

Zonas de Disponibilidades:

* Também chamadas de AZs (*Availability Zones*)
* Agrupamento de datacenters isolados dentro de uma região
* Rede, energia e conectividade redundantes
* Próximas o suficiente para manter baixa latência, longe o suficiente para evitar quer um desastre afete mais de uma AZ
* Recomendação: Execute pelo menos em duas AZs.

## 2.3 Pontos de Presença

* Também chamados de *Edge locations*, Locais de borda ou Redes de borda
* Funcionam como pontos específicos pelo globo para distribuir conteúdo de forma rápida
* Exemplos de serviços que se encontram nos locais de borda: *Route 53* (DNS), *Cloud Front* (CDN)

Exemplo:

* Um usuário do Brasil acessa um streaming de filme na China.
* Entre eles, na Nigéria, tem um Ponto de Presença, um servidor que deixa salvo em cache o conteúdo
* Quando o usuário tentar acessar novamente, terá um acesso mais rápido.

### 2.3.1 Route 53 - DNS

Lê o endereço que o usuário está digitando e vai traduzir no IP.

* Serviço de DNS
* Ajuda os clientes a redirecionar corretamente as requisições.

### 2.3.2 Amazon CloudFront

* Serviço de entrega de conteúdo: CDN
* Melhora a performance do seu serviço (baixa latência, alta taxa de transferência)
* Provê conteúdo o mais próximo possível do seu usuário

## 2.4 Provisionamento de recursos na AWS

Como é possível interagir com serviços AWS?

* Console de gerenciamento
* AWS CLI
* SDKs

### 2.4.1 Console de gerenciamento

Acessar pelo portal web, com usuário e senha.

### 2.4.2 AWS CLI

Baixa um pacote na AWS e instala no computador, e então consegue acessar os mesmos serviços através de linha de comando.

* Instalado na sua máquina
* Opera com APIs da AWS através de linha de comando

### 2.4.3 SDKs

Quando um dos suas aplicações acessem seus serviços ou recursos da AWS.

Pega o SDK da sua linguagem, acopla no programa através de linhas de código usando a documentação.

* Acesso as APIs AWS através de SDK
* SDK possui versões em diversas linguagens, como: Java, C#, Go, Python, Javascript

### 2.4.4 Provisionando infraestrutura

* Elastic Beanstalk - automatiza processos de deploy. Pega seu software, empacota e ao executar ele provisiona uma infraestrutura com suas necessidades.
* CloudFormation - para automatizar de construção de ambientes na AWS através de arquivos JSON ou YAML.
