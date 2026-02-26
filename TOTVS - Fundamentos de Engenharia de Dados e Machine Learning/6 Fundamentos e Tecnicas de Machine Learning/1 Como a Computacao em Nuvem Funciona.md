# 1 Como a Computação em Nuvem Funciona

## 1.1 Introdução

Introdução do Felipão

## 1.2 O que vou aprender

* O que é Nuvem?
* Como funcionar?
* Por que e aonda utilizamos?

## 1.3 Pré-requitos

* Lógica

## 1.4 As a Service

### O que é a Cloud? (segundo a IA)

```txt
É uma rede de servidores remotos que armazeram e gerenciam dados e executem aplicativos e fornecem conteúdo e serviços.  

Os servidores estão interligados e funcionam como um ecossistema único. Permite aceder aos dados online, de qualquer dispositivo com acesso à Internet.

Existem diferentes tipos de nuvens, como públicas, privadas, híbridas e de comunidade.
```

### Analogia com lavar a roupa

As **casas de modelo americano** são feitos de madeiras → são pequenas e ambientes limitados e com pouca capacidade.

**Máquina de lavar** não era comum nos EUA, pois as casas eram muito pequenas e elas ocupavam muito espaço (e também era considera um item de luxo), pois:

* Era um custo (aquisição e manutenção)
* Ocupava muito espaço
* Uso que não justifica tê-la o tempo todo dentro de casa

(Compra o produto)

**Lavanderia (Loundry)**: gastava-se uma simples moeda *pagava-se pelo uso*.

(Compra o serviço)  
(**As a service**)

## 1.5 Custos do Modelo Local

Já no ambiente empresarial, também existem limites.

Vamos com o exemplo que há um banco e é necessário uma máquina para processar todos os dados e solicitações:

* Custo de aquisição e manutenção
* Espaço

Se o negócio crescer, será necessário comprar mais máquinas, ocupando muito mais espaço, com alto custos e também começar a se preocupar com a **infraestrutura**, como refrigeração, segurança.

Além disso precisa estar devidamente cabeada, precisam se conectar (**networking**).

Em um momento ficará inviável escalar, o custo vai subindo exponencial, será necessário um datacenter para resolver o problema.

## 1.6 On Premise vs Ambiente Cloud

**On Premise** - Máquinas no local, ambiente privado, lidando com os preços e custos.

Vamos supor que entrou em meses de baixa demanda e parte das máquinas estivessem paradas...

Mas e se pegasse nossas máquinas que estão ociosas e emprestar para outras empresas e só cobra pelo seu uso? (*As a service*)

Essas outras empresas só precisará de uma internet que acessará as máquinas remotamente, ou seja, essas máquinas estarão em **Ambiente Cloud**.

E não vão precisar:

* com custos de aquisição ou manutenção  
* ocupação de espaços  
* infraestrutura  

## 1.7 Hybrid Model

Quando há máquinas **On Premise** e máquinas em **Ambiente Cloud**.

Muito comum quando há oscilação do consumo de processamento, em geral maior parte do ano há pouco processamento mas em certa época dos anos há um pico de uso. (sazional)

## 1.8 Qual Modelo Escolher

Depende, precisa avaliar as condições, vantagens e desvantagens dos modelos.

Há questões como:

* Lateralização  
* Legislação (proteção dos dados)  
* Latência  
* Volatilidade do dólar  

## 1.9 Platform

A empresa que fornece as máquinas e vende a infraestrutura é conhecido como **Infra as a Service (IaaS)**

Essas empresas que tem foco de ter infraestruturas completas são conhecidas como **platform**, como exemplo a AWS, Azure, Cloud, GCP (Google)

## 1.10 Regions & Zones

Para resolver problemas de latência devido a distância das nuvens e seus clientes, há as **regions** e **zones**.

*Regions* - São lugares diferentes do mundo onde se encontra conjuntos de máquinas, nela haverá *zones*.  
*Zones* - São áreas diferentes dessas regiões.  

Analogia às lavanderias, em escolher uma lavanderia da minha cidade (region) e bairro vizinho (zone)

## 1.11 Resumão e Caderno de Anotações

 [https://felipe-aguiar.gitbook.io/cloud-fundamentals](Resumão do Felipão)
