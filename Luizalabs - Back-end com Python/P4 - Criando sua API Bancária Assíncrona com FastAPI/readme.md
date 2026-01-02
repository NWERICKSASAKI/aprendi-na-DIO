# P4 Criando sua API Bancária Assíncrona com FastAPI

Referência: <https://github.com/digitalinnovationone/trilha-python-dio/tree/main/13%20-%20APIs%20Ass%C3%ADncronas%20com%20FastAPI/desafio>

## Desafio: API Bancária Assíncrona com FastAPI

O desafio conssitem em projetar e implementar uma API RESTful assíncrona usando **FastAPI** para gerenciar operações bancárias de **depósitos** e **saques**, vinculadas a **contas correntes**. Este desafio irá lhe proporcionar a experiência de construir uma aplicação backend moderna e eficiente que utiliza **autenticação JWT** e práticas recomendadas de design de APIs.

### Objetivos e Funcionalidades

Objetivo do desafio é desenvolver uma API com as seguintes funcionalidades:

- **Cadastro de Transações:** Permita o cadastro de transações bancárias, como depósitos e saques.
- **Exibição de Extrato:** Implemente um endpoint para exibir o extrato de uma conta, mostrando todas as transações realizadas.
- **Autenticação com JWT:** Utilize JWT (JSON Web Tokens) para garantir que apenas usuários autenticados possam acessar os endpoints que exigem autenticação.

### Requisitos Técnicos

Para a realização deste desafio, deve ser atendido aos seguintes requisitos técnicos:

- **FastAPI:** Utilize FastAPI como framework para criar sua API. Aproveite os recursos assíncronos do framework para lidar com operações de I/O de forma eficiente.
- **Modelagem de Dados:** Crie modelos de dados adequados para representar contas correntes e transações. Garanta que as transações estão relacionadas a uma conta corrente, e que contas possam ter múltiplas transações.
- **Validação das operações:** Não permita depósitos e saques com valores negativos, valide se o usuário possui saldo para realizar o saque.
- **Segurança:** Implemente autenticação usando JWT para proteger os endpoints que necessitam de acesso autenticado.
- **Documentação com OpenAPI:**  Certifique-se de que sua API esteja bem documentada, incluindo descrições adequadas para cada endpoint, parâmetros e modelos de dados.

----------------------------------------

## Resolução do Projeto

Referência para resolução do projeto:  
<https://github.com/digitalinnovationone/trilha-python-dio/tree/main/13%20-%20APIs%20Ass%C3%ADncronas%20com%20FastAPI/dio-blog>

Devido a complexidade do projeto decidi separar por etapas:

### 1 Configuração inicial

#### 1.1 Ambiente virtual

Dei um `poetry init` e fazer as configurações iniciais (fastapi, uvicorn):

```bash
poetry add 'fastapi=*'
poetry add "uvicorn[standard]" 
poetry add "pydantic-settings" 
poetry add "aiosqlite" 
```

Em seguida configurei o path do interpretador obtido através de `poetry env info -p`.  

Para ativar o ambiente virtual `poetry env activate`.  

#### 1.2 Estruturas de pasta

```txt
P4 - Criando sua API Bancária Assíncrona com FastAPI
 |
 ├─ src
 |   |
 |   ├─ controllers
 |   |   |
 |   |   ├─ cliente.py
 |   |   ├─ conta_corrente.py
 |   |   ├─ conta.py
 |   |   ├─ endereco.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ models
 |   |   |
 |   |   ├─ cliente.py
 |   |   ├─ conta_corrente.py
 |   |   ├─ conta.py
 |   |   ├─ endereco.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ schemas
 |   |   |
 |   |   ├─ cliente.py
 |   |   ├─ conta_corrente.py
 |   |   ├─ conta.py
 |   |   ├─ endereco.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ services
 |   |   |
 |   |   ├─ cliente.py
 |   |   ├─ conta_corrente.py
 |   |   ├─ conta.py
 |   |   ├─ endereco.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ views
 |   |   |
 |   |   ├─
 |   |   └─
 |   |
 |   ├─ database.py
 |   ├─ main.py
 |   └─ security.py
 |
 ├─ test
 |   |
 |   ├─ integration
 |   |   |
 |   |   └─ controllers
 |   |       |
 |   |       ├─ auth
 |   |       |   |
 |   |       |   └─ test_login.py
 |   |       |
 |   |       └ post
 |   |          |
 |   |          ├─
 |   |          └─
 |   |
 |   ├─ __init__.py
 |   └─ conftest.py
 |
 ├─ .gitignore
 ├─ poetry.lock
 └─ pyproject.toml
```

#### 1.3 .env

Criado arquivo `.env` conforme modelo:

```.env
ENVIRONMENT="local"
DATABASE_URL="sqlite:///./blog.db"
```

Ele serve para armazenar chaves, tokens, senhas ou endereços que podem ser sensíveis.  
Neste projeto ele estará público para fins de testes e reprodução do projeto.  
Este arquivo .env será utilizado e através do arquivo `config.py`  

### 2 API

Decidi deixar semi-estruturado e funcional a API para eventualmente construir e testar as funcionalidades do banco através das chamadas de end-point.

#### 2.1 src/schemas/

Para utilizarmos a API vou deixar configurado a pasta **schemas**, através dele os arquivos estarão configurados para filtrar as entradas das chamadas conforme a configuração exemplo abaixo:

```py
from pydantic import AwareDatetime, BaseModel, NaiveDatetime
from datetime import date

class ClienteIn(BaseModel):
    # Cliente
    endereco: str
    # PessoaFisica
    cpf: str
    nome: str
    nascimento: date
    # etc
    cadastrado_em: AwareDatetime | None

class ClienteInEdit(BaseModel):
    # Cliente
    endereco: str | None = None
    # PessoaFisica
    cpf: str | None = None
    nome: str | None = None
    nascimento: date | None = None
```

P.S: Ainda vou me decidir se vou usar Aware ou Naive

#### 2.2 src/views/

Assim como já configurei para a entrada de dados, vou deixar pré-configurado para visualização das nossas futuras saídas:

```py
from pydantic import BaseModel, AwareDatetime, NaiveDatetime
from datetime import date

class ClienteOut(BaseModel):
    cliente_id: int
    # Cliente
    endereco: str
    contas: list[dict] | None
    # PessoaFisica
    cpf: str
    nome: str
    nascimento: date
    # etc
    cadastrado_em: AwareDatetime | NaiveDatetime | None
```

#### 2.3 src/config.py

Este arquivo é utilizado no arquivo `src/database.py`.  
É usado para auxiliar e automatizar leitura de variáveis e demais informações escritas no `.env` seguindo o modelo abaixo:

```py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8")

    database_url: str
    environment: str = "production"

settings = Settings()
```

#### 2.4 src/database.py

```py
import databases
import sqlalchemy as sa

from src.config import settings

database = databases.Database(settings.database_url)
metadata = sa.MetaData()

if settings.environment == 'production':
    engine = sa.create_engine(settings.database_url)
else: # para uso de fastapi
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread":False})
```

#### 2.5 src/main.py

Neste arquivo vamos preparar a main e pré-configurar as rotas para os principais grupos:

```py
from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import database
from src.controllers import cliente
from src.controllers import conta
from src.controllers import autenticacao
from src.controllers import transacao

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

# TODO adicionar middlewares e configurações do APP
app = FastAPI(
    lifespan=lifespan
)

app.include_router(autenticacao.router)
app.include_router(cliente.router)
app.include_router(conta.router)
app.include_router(transacao.router)
```

#### 2.6 src/controllers/

```py
from fastapi import APIRouter, Depends, status

from src.schemas.cliente import ClienteIn
from src.schemas.transacao import TransacaoIn
from src.views.cliente import ClienteOut
from src.views.transacao import TransacaoOut

# TODO adicionar dependencias de login com Depends

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
#@router.get("/", response_model=list[ClienteOut])
async def listar_clientes():
    return "Lista de clientes"  # TODO implementar lógica de listagem de clientes

@router.get("/{cliente_id}")
#@router.get("/{cliente_id}", response_model=ClienteOut)
async def obter_cliente(cliente_id: int):
    return f"Detalhes do cliente {cliente_id}"

@router.post("/", status_code=status.HTTP_201_CREATED)
#@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteIn):
    return f"Cliente criado com sucesso: {cliente}"

@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
#@router.patch("/{cliente_id}", response_model=ClienteOut, status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteIn):
    return f"Cliente {cliente_id} atualizado com sucesso: {cliente}"

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    return

@router.post("/{cliente_id}/transacao", status_code=status.HTTP_202_ACCEPTED)
#@router.post("/{cliente_id}/transacao", response_model=TransacaoOut, status_code=status.HTTP_202_ACCEPTED)
async def realizar_transacao(cliente_id, transacao:TransacaoIn):
    return f"Transacao realizada com sucesso no valor de {transacao.valor}"
```

P.S: Deixei comentado os `response_model` para testar as funcionalidades básicas da API antes de nos aprofundarmos no Banco e suas respectivas consultas e saídas.

#### 2.7 Inicializando a API

Se tudo estiver configurado o mínimo deve funcionar nas chamadas de `GET` ao se usar: `uvicorn src.main:app --reload`.  

Se houver erros, ler os logs e corrigí-los.

#### 2.8 Teste simples da API

Vamos configurar o **Insomnia** para fazer alguns testes de `GET` e `POST` para vermos se obtemos as saídas genéricas anteriormente configuradas:

- Criado um novo Collection em `+ Create` → `Request Collection`  
- Clique em `Base Environment` → `✏️` e configure um com nome `host` passando como argumento `http://127.0.0.1:8000`
- Dentro dele foi criado várias pastas: `Autenticação`, `Cliente`, `Conta` e `Transação`
- Para cada uma das pasta foi criado um HTTP Request via `+` → `HTTP Request`, lembrete de inserir `_.host` no path.
- Para o `POST` foi usado o seguinte `body/json`:

```json
{
  "endereco": "Rua ABC, 123",
  "cpf": "12345678901",
  "nome": "Testonildo da Silva",
  "nascimento": "1993-02-01",
  "cadastrado_em": "2026-01-01 12:59:00-03:00"
}
```

- Para o `POST` de Transacao foi configurado o seguinte JSON:

```json
{
  "transacao_id": 1,
  "conta_id": 1,
  "valor": 1234.56,
  "cadastrado_em": "2026-01-31 12:34-03:00"
}
```

- Para o `POST` da Conta foi configurado o seguinte JSON:

```json
{
  "conta_id": 1,
  "agencia": "0001",
  "cliente_id": 1,
  "cadastrado_em": "2026-01-31 12:34-03:00"
}
```

### 3 Banco de Dados
