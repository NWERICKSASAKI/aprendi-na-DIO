# Utilizando Microsoft Copilot para escrever consultas SQL

## 1 Introdução

### 1.1 O que vamos aprender

### 1.2 Pré-requisitos

Instalar um SGBD, sugestão PostGres

### 1.3 O que vamos construir

Simular um banco de dados das cartas de TCG do Pokemon.

Quanto o copilot consegue nos ajudar?

## 2 Organização

### 2.1 Setup do Projeto

Diretório:

```txt
E-CARDS
|
├ assets
|   └ charizard.jpg
|
├ db_scripts
|   ├ seeds
|   |   └ 001_seeds_cards.sql
|   |
|   └ tables
|       └ 001_create_card.sql
|
├ prompts
|   └ tcg-cards.txt
|
└ readme.md
```

### 2.2 Table Scripts Types

tcg-cards.txt

```txt
[ação]
create a script to create a table in postgresql

[context]
- the first table is a table to save a pokemon card tcg cards
- the second table is a table to sabe collections set

connect to tables with FOREIGN KEY

[informações]
the first table: tbl_cards
- id
- hp
- name
- type
- stage
- info
- attack
- damage
- weak
- resis
- retreat
- cardNumberInColletion

the second table: tbl_colletions
- id
- collectionSetName
- release Date
- totalCardsInCollection
```

Jogue no copilot (sem os conchetes).

+ alguns prompts para separar mais algumas tabelas com type.

Copiado o código SQL e colado no arquivo `001_create_card.sql`

### 2.3 Generates Seeds

Para não começar as tabelas sem dados, vamos implementar dados iniciais na tabela.

Partindo do suposto que o chat da IA esteja sem contexto:

```txt
consider tables bellow

{código SQL criado anteriormente}

create a initial seed to all tables with tcg pokemo, geenerate insert scripts
```

e salvar o resultado do script SQL no `001_seeds_cards.sql`

e pode pedir mais e mais inserts e gerando outros arquivos: 

`002_bulk_cards_1.sql`, `003_bulk_cards_2.sql`, `004_bulk_cards_3.sql`

## 3 Execução

### 3.1 Executando Scripts

Abre o SGBD (ou terminal) e vamos executar os arquivos SQL.

### 3.2 Criando Migrations Automatizadas

Mas eu não quero rodar todos os arquivos individualmente!

`to_migration.ps1` na mesma pasta das seeds

```powershell
# Pegar o diretório atual
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# Arquivo saída com todos sql
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

# Verifica se arquivo já existe, se existir deleta
if (Test-Path $outputFile){
    Remove-Item $outputFile
}

# Pega conteúdo dos arquivos
$sqlFile = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File |  Sort-Object Name

# Concatena arquivos
foreach($file in $sqlFile){
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outpuFile
}

Write-Host "Todos os arquivos foram combinados em $outputFile"
```

Pra executar só passar o fullpath do arquivo .ps1 no terminal e pronto!

### 3.3 Views e Uso

```txt
Considere o modelo relacional abaixo:

{código do 001_create_card.sql}

traga todas as informações da tbl_cards substituindo os IDs das chaves estrangeiras, salve isso em uma view para o postgresql
```

Salvar em `views/001_view_cards.sql` e vamos testar no nosso SGBD.

`select * from vw_vards_info` retorna a nossa tabela (porém não é perfomático, coloque campo por campo)
