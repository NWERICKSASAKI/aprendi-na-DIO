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
 |   |   ├─ autenticacao.py
 |   |   ├─ cliente.py
 |   |   ├─ conta.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ models
 |   |   |
 |   |   ├─ autenticacao.py
 |   |   ├─ cliente.py
 |   |   ├─ conta.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ schemas
 |   |   |
 |   |   ├─ autenticacao.py
 |   |   ├─ cliente.py
 |   |   ├─ conta.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ services
 |   |   |
 |   |   ├─ autenticacao.py
 |   |   ├─ cliente.py
 |   |   ├─ conta.py
 |   |   └─ transacoes.py
 |   |
 |   ├─ views
 |   |   |
 |   |   ├─ cliente.py
 |   |   ├─ conta.py
 |   |   └─ transacoes.py
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

### 2 API

Decidi deixar semi-estruturado e funcional a API para eventualmente construir e testar as funcionalidades do banco através das chamadas de end-point.

#### 2.1 src/schemas/

Para utilizarmos a API vou deixar configurado a pasta **schemas**, através dele os arquivos estarão configurados para filtrar as entradas das chamadas conforme a configuração exemplo abaixo:

```py
from pydantic import AwareDatetime, BaseModel
from typing import Literal
from datetime import date

class ClienteIn(BaseModel):
    endereco: str
    cadastrado_em: AwareDatetime | None

class ClienteInEdit(BaseModel):
    endereco: str | None = None

class PessoaFisicaIn(ClienteIn):
    tipo: str = Literal["pf"]
    cpf: str
    nome: str
    nascimento: date

class PessoaFisicaInEdit(ClienteInEdit):
    tipo: str = Literal["pf"]
    cpf: str | None = None
    nome: str | None = None
    nascimento: date | None = None

# Prevendo futuros tipos
class PessoaJuridicaIn(ClienteIn):
    tipo: str = Literal["pj"]
    cnpj: str
    razao_social: str

class PessoaJuridicaInEdit(ClienteInEdit):
    tipo: str = Literal["pj"]
    cnpf: str | None = None
    razao_social: str | None = None
```

P.S: Ainda vou me decidir se vou usar Aware ou Naive

#### 2.2 src/main.py

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

#### 2.3 src/controllers/

```py
from fastapi import APIRouter, Depends, status

from src.schemas.cliente import PessoaFisicaIn, PessoaJuridicaIn
from src.schemas.transacao import TransacaoIn

from typing import Union

ClienteIn = Union[PessoaFisicaIn, PessoaJuridicaIn]

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
async def listar_clientes():
    return "Lista de clientes"

@router.get("/{cliente_id}")
async def obter_cliente(cliente_id: int):
    return f"Detalhes do cliente {cliente_id}"

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteIn):
    return f"Cliente criado com sucesso: {cliente}"

@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteIn):
    return f"Cliente {cliente_id} atualizado com sucesso: {cliente}"

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    return
```

P.S: O `response_model` será acrescentado posteriormente, pois o foco agora é testar as funcionalidades básicas da API antes de nos aprofundarmos no Banco e suas respectivas consultas e saídas.

#### 2.4 Inicializando a API

Se tudo estiver configurado o mínimo deve funcionar nas chamadas de `GET` ao se usar: `uvicorn src.main:app --reload`.  

Se houver erros, ler os logs e corrigí-los.

#### 2.5 Teste simples da API

Vamos configurar o **Insomnia** para fazer alguns testes de `GET` e `POST` para vermos se obtemos as saídas genéricas anteriormente configuradas:

- Criado um novo Collection em `+ Create` → `Request Collection`  
- Clique em `Base Environment` → `✏️` e configure um com nome `host` passando como argumento `http://127.0.0.1:8000`
- Dentro dele foi criado várias pastas: `Autenticação`, `Cliente`, `Conta` e `Transação`
- Para cada uma das pasta foi criado um HTTP Request via `+` → `HTTP Request`, lembrete de inserir `_.host` no path.
- Para o `POST` foi usado o seguinte `body/json` para pessoa física:

```json
{
  "endereco": "Rua ABC, 123",
  "tipo": "pf",
  "cpf": "12345678901",
  "nome": "Testonildo da Silva",
  "nascimento": "1993-02-01"
}
```

- Para criação de pessoa jurídica:

```json
{
  "endereco": "Rua Empresarial, 1.000",
  "tipo": "pj",
  "cnpj": "123.456.789/0001-99",
  "razao_social": "Testes & CIA"
}
```

- Para o `POST` de Transacao foi configurado o seguinte JSON:

```json
{
  "transacao_id": 1,
  "conta_id": 1,
  "valor": 1234.56
}
```

- Para o `POST` da Conta foi configurado o seguinte JSON:

```json
{
  "conta_id": 1,
  "agencia": "0001",
  "cliente_id": 1,
}
```

### 3 Banco de Dados

#### 3.1 .env

Criado arquivo `.env` conforme modelo:

```.env
ENVIRONMENT="local"
DATABASE_URL="sqlite:///./meu_banco.db"
```

Ele serve para armazenar caminhos, chaves, tokens, senhas ou endereços que podem ser sensíveis.  
Neste projeto ele estará público para fins de testes e reprodução do projeto.  
Este arquivo `.env` será acessado e através do arquivo `config.py`  

#### 3.2 src/config.py

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

#### 3.3 src/database.py

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

#### 3.4 src/models/

Foi criado os arquivos na pasta model seguindo o padrão:

```py
import sqlalchemy as sa
from src.database import metadata

cliente = sa.Table(
    'cliente',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('endereco', sa.String),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True)
    )

pessoa_fisica = sa.Table(
    'pessoa_fisica',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id', ondelete='CASCADE')),
    sa.Column('cpf', sa.String(14), nullable=False, unique=True),
    sa.Column('nome', sa.String(150), nullable=False),
    sa.Column('nascimento', sa.TIMESTAMP(timezone=True), nullable=True),
    )

pessoa_juridica = sa.Table(
    'pessoa_juridica',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id', ondelete='CASCADE')),
    sa.Column('cnpj', sa.String(), nullable=False, unique=True),
    sa.Column('razao_social', sa.String(150), nullable=False)
)
```

#### 3.5 Criando as tabelas

Vamos adicionar o Alembic: `poetry add 'alebic=*'`.  
Em seguida no terminal vamos executar `alembic init migration`.  
Vamos editar o arquivo `migration/env.py`:

```py
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from src.config import settings

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from src.database import engine, metadata
from src.models.cliente import cliente, pessoa_fisica
from src.models.conta import conta, conta_corrente
from src.models.transacao import transacao

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = settings.database_url
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

Agora executar o:

`alembic revision --autogenerate -m "Add initial tables"`  

Neste momento ele criará um script para igualar o seu banco de dados atual com os modelos informados.  

Como ainda não criamos os nosso banco ou tabelas, ao executar o comando abaixo, o Alembic irá criar o nosso banco com as nossas tabelas.  

`alembic upgrade head`

P.S:  

Se por ventura ficar constantemente revisando as tabelas, alterando de título ou nome das colunas constantemente e ainda não chegar na forma defitiva, o seu Alembic nas próximas `revision` e `upgrade head` podem dar erros e alertas.

Caso chegar nesse ponto em que valha a pena "resetar" o alembic, apagar a pasta `migration/` e deletar o `arquivo.bd` e aí sim reiniciar o processo do `alembic init migration` e etc...

#### 3.6 Inserindo dados

No `src/controllers/cliente.py` comecei a editar e acrescentar a rota POST:

```py
from src.services import clientes as services

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente_json: ClienteIn):
    cliente_id = await services.criar_cliente(cliente_json)
    return {"id": cliente_id}
```

Para o primeiro POST de cliente funcionar o arquivo `src/services/cliente.py` começou assim:

```py
import sqlalchemy as sa
from src.database import database
from src.models.cliente import cliente, pessoa_fisica, pessoa_juridica
from datetime import datetime, timezone

async def _criar_cliente_base(cliente_json) -> int:
    query = cliente.insert().values(
        endereco = cliente_json.endereco,
        cadastrado_em = datetime.now(timezone.utc)
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pf(id, cliente_json) -> int:
    query = pessoa_fisica.insert().values(
        cliente_id = id,
        cpf = cliente_json.cpf,
        nome = cliente_json.nome,
        nascimento = cliente_json.nascimento
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pj(id, cliente_json) -> int:
        query = pessoa_juridica.insert().values(
            cliente_id = id,
            cnpj = cliente_json.cnpj,
            razao_social = cliente_json.razao_social
        )
        id = await database.execute(query)
        return id

async def criar_cliente(cliente_json):
    async with database.transaction(): # commit automático e rollback em caso de erro
        id = await _criar_cliente_base(cliente_json)
        match cliente_json.tipo:
            case "pf":
                await _criar_cliente_pf(id, cliente_json)
            case "pj":
                await _criar_cliente_pj(id, cliente_json)
        return id
```

Após essa configuração foi inserido via POST pelo Insonmia alguns clientes.

#### 3.7 Resgatando dados

Editado no arquivo `src/controllers/cliente.py`:

```py
@router.get("/")
async def listar_clientes():
    return await services.listar_clientes()
```

Enquanto isso no `src/services/cliente.py` foi adicionado a função:

```py
async def listar_clientes():
    query = sa.select(
        cliente.c.id,
        cliente.c.endereco,
        cliente.c.cadastrado_em,

        pessoa_fisica.c.id.label("pf_id"),
        pessoa_fisica.c.cpf,
        pessoa_fisica.c.nome,
        pessoa_fisica.c.nascimento,

        pessoa_juridica.c.id.label("pj_id"),
        pessoa_juridica.c.cnpj,
        pessoa_juridica.c.razao_social
    ).select_from(
        cliente
        .outerjoin(pessoa_fisica, pessoa_fisica.c.cliente_id == cliente.c.id)
        .outerjoin(pessoa_juridica, pessoa_juridica.c.cliente_id == cliente.c.id)
    )
    rows = await database.fetch_all(query)
    return rows
```

Ao usar o Insomnia retornará todos os clientes com todas as suas informações, sejam elas Pessoas Físicas ou Jurídicas.

Único detalhe que a saída do `GET` trará todas as informações independente do tipo de cliente/pessoa, retornando vários campos como `null`.

#### 3.8 src/views/

Para configurarmos como queremos que seja a saída, precisaremos do `model_response` no `src/controllers/cliente.py`:

```py
from src.views.cliente import PessoaFisicaOut, PessoaJuridicaOut 
from src.views.transacao import TransacaoOut

from pydantic import Field
from typing import Union, Annotated

# com o ClienteOut, será selecionado qual das VIEWS será utilizada com base no "tipo" dos dados, seja ela "pj" ou "pf".
ClienteOut = Annotated[
    Union[PessoaFisicaOut, PessoaJuridicaOut],
    Field(discriminator="tipo")
]

# ...

@router.get("/", response_model=list[ClienteOut])
async def listar_clientes():
    return await services.listar_clientes()
```

Mas vamos ter que formatar a saída da função `listar_clientes()` do `src/services/cliente.py` também:

```py
async def listar_clientes():
    # ...
    return [_mapear_cliente(row) for row in rows]
```

Foi adicionado a função `_mapear_cliente(row)` neste mesmo arquivo:

```py
def _mapear_cliente(row) -> dict:
    base = {
        "id": row["id"],
        "endereco": row["endereco"],
        "cadastrado_em": row["cadastrado_em"].replace(tzinfo=timezone.utc) # para reconverter pro AwareDatetime
    }
    if row["cpf"]:
        return {
            **base,
            "pf_id": row["pf_id"],
            "tipo": "pf",
            "cpf": row["cpf"],
            "nome": row["nome"],
            "nascimento": row["nascimento"]
        }
    if row["cnpj"]:
        return {
            **base,
            "pj_id": row["pj_id"],
            "tipo": "pj",
            "cnpj": row["cnpj"],
            "razao_social": row["razao_social"]
        }
    raise ValueError("Cliente sem PF/PJ associado")
```

Por fim, foi configurado para visualização das nossas futuras saídas no `src/views/cliente.py`:

```py
from pydantic import BaseModel, AwareDatetime
from datetime import date
from typing import Literal

class ClienteOut(BaseModel):
    id: int
    endereco: str
    # contas_id: list[dict] | None
    cadastrado_em: AwareDatetime

class PessoaFisicaOut(ClienteOut):
    tipo: Literal["pf"] = "pf"
    pf_id: int
    cpf: str
    nome: str
    nascimento: date

class PessoaJuridicaOut(ClienteOut):
    tipo: Literal["pj"] = "pj"
    pj_id: int
    cnpj: str
    razao_social: str
```

A nova saída do `GET` sairá com os campos definidos e sem qualquer campo adicional com `null`.

#### 3.9 Deletando dados

Editado no `src/controllers/cliente.py`:

```py
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    await services.deletar_cliente(cliente_id)
    return
```

Enquanto no `src/services/cliente.py`:

```py
async def deletar_cliente(cliente_id: int):
    async with  database.transaction():
        await database.execute(pessoa_fisica.delete().where(pessoa_fisica.c.cliente_id == cliente_id))
        await database.execute(pessoa_juridica.delete().where(pessoa_juridica.c.cliente_id == cliente_id))
        result = await database.execute(cliente.delete().where(cliente.c.id == cliente_id))
        return result>0 # True/False se apagou alguma linha
```

#### 3.10 Patch de dados

Em `src/controllers/cliente.py`:

```py
@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteInEdit):
    await services.atualizar_cliente(cliente_id, cliente)
    return
```

Em `src/services/cliente.py` tive que separar o JSON em dicionários específicos para cada tabela para depois realizar o `UPDATE`:

```py
async def atualizar_cliente(cliente_id: int, cliente_json):
    dicio_dados = cliente_json.model_dump(exclude_unset=True)
    tipo = dicio_dados.pop("tipo")

    dados_base = {}
    dados_pf = {}
    dados_pj = {}

    for k,v in dicio_dados.items():
        if k in cliente.c:
            dados_base[k]=v
    if dados_base:
        await database.execute(cliente.update().values(**dados_base).where(cliente.c.id == cliente_id))

    match tipo:
        case 'pf':
            for k,v in dicio_dados.items():
                if k in pessoa_fisica.c:
                    dados_pf[k]=v
            if dados_pf:
                await database.execute(pessoa_fisica.update().values(**dados_pf).where(pessoa_fisica.c.id == cliente_id))
        case 'pj':
            for k,v in dicio_dados.items():
                if k in pessoa_juridica.c:
                    dados_pj[k]=v
            if dados_pj:
                await database.execute(pessoa_juridica.update().values(**dados_pj).where(pessoa_juridica.c.id == cliente_id))
    return
```

