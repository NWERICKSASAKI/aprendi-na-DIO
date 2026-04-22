# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: 22 de abril de 2026  
Empresa: Abstergo Industries  
Responsável: Erick Sasaki  

## Introdução

Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Erick Sasaki. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos e modernizar a infraestrutura de TI defasada da farmácia, eliminando gastos com hardware físico local e manutenção excessiva.  

## Descrição do Projeto

O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:  

Etapa 1:

- **Amazon EC2 (Elastic Compute Cloud)**  
- **Foco da ferramenta:** Migração de Servidores Locais (Lift-and-Shift).  
- **Descrição de caso de uso:** Substituição do servidor físico antigo que roda o sistema de gestão (ERP) e o banco de dados da farmácia. Ao migrar para instâncias EC2, a empresa elimina custos de energia, refrigeração e manutenção de hardware local, pagando apenas pela capacidade computacional utilizada.  

Etapa 2:

- **Amazon S3 (Simple Storage Service)**  
- **Foco da ferramenta:** Backup e Armazenamento em Nuvem.  
- **Descrição de caso de uso:** Implementação de uma rotina de backup automatizada para as receitas digitalizadas, documentos fiscais e dados de estoque. O S3 substitui unidades de fita ou HDs externos vulneráveis, oferecendo durabilidade de dados e reduzindo custos com perda de informações ou infraestrutura de armazenamento físico.  

Etapa 3:  

- **AWS Amazon WorkSpaces**  
- **Foco da ferramenta:** Virtualização de Desktops.  
- **Descrição de caso de uso:** Modernização dos terminais de venda (PDV) e computadores administrativos sem a necessidade de comprar novos hardwares caros. Utilizando thin clients ou máquinas antigas para acessar desktops virtuais na nuvem, a farmácia estende a vida útil do hardware existente e centraliza a gestão de segurança e software.  

## Conclusão

A implementação de ferramentas AWS na empresa *Abstergo Industries tem como esperado a redução drástica de gastos com infraestrutura física (CapEx), maior disponibilidade do sistema de vendas e segurança robusta contra perda de dados*, o que aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias, como o AWS Lambda para automação de processos, que possam melhorar ainda mais os processos da empresa.

## Anexos

- Manual de configuração de instâncias EC2.
- Políticas de ciclo de vida de armazenamento do Amazon S3.
- Guia de acesso ao Amazon WorkSpaces para funcionários.
- Planilha de comparativo de custos: On-premise vs. Nuvem.

Assinatura do Responsável pelo Projeto:

__________________________________________  
Erick Sasaki