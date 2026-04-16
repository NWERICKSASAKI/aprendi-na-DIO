# Criando um Processso de ETL com Excel e Power Query

## 1 Introdução

### 1.1 O que vou aprender

Transformar uma tabela totalmente fora de padrão para depois ser utilizada para análise e dashboards.

### 1.2 Pré-requisitos

Excel com Power Query

### 1.3 Case Situation

A tabela que vamos trabalhar está com:

- Linhas vazias
- Valores com "$"
- Linhas com "---" sendo usado como separador de lotes
- Nome do jogo junto com o console
- Número do lote contendo strings

## 2 Resolução

### 2.1 ETL

(explicação do que é ETL)

### 2.2 Overview power query

`Excel → Planilha Excel em branco → Aba: Dados → Obter Dados → De Arquivo → Do Excel Pasta de Trabalho`

Seleciona a tabela e clica em `transform` para iniciar o **power query**.

`Página Inicial / Editor` Avançado mostra o código (receita) das transformações que você vai fazendo dentro do Power Query (excluir coluna, filtrar valores, etc...)

### 2.3 Trabalhando com Números

Coisas que foi feito durante as aulas:

- **Excluir coluna**
- Aplicar **filtro** por coluna
- **Dividir coluna**
- **Renomear** coluna (duplo clique na coluna)
- Página Inicial / Transformar → **Substituir valores** (retirar `$`, ou substituir `.` por `,`)
- Mudar a **unidade da coluna** (clica lá no `ABC123` e muda pro formato número inteiro)
- **Adicionar Coluna** → (seleciona as colunas stock  e preço_unitário) Padrão → **Multiplicar**

### 2.4 Processo de Load

`Página inicial → Fechar e Carregar → Fechar e Carregar para`

Nesse caso volta pro Excel.

Precisa editar algo que esqueceu lá no Power Query?

Só clicar em Consulta, botão direito na planilha e `Editar`

### 2.5 Finalização

E se aquela planilha, no mês seguinte, for atualizada?

No excel tem um botão de `Refresh` lá em Consultas e Conexões.
