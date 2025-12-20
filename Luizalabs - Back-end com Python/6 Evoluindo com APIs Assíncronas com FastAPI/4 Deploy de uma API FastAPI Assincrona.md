# 4 Deploy de uma API FastAPI Assíncrona

## Criando o repositório e o servidor web

Para fazer o deploy da API vamos utilizar o <http://dashboard.render.com>

Após criar conta e logar → no menu de topo clique em `New +` → [Web Service](https://dashboard.render.com/web/new).  

1. Víncule à sua conta GitHub caso não o tenha feito.  
2. Selecione o repositório
3. Configure a `Language` pra Python 3
4. No comando de `Build Command` deixe `poetry install --no-root --without dev`
5. No `Start Command` deixe `uvicorn src.main:app --host 0.0.0.0 --port $PORT`, conforme [documentação](https://render.com/docs/deploy-fastapi)
6. `Instance Type`: `Free`
7. `Deploy Web Service`

### Configurando no Insomnia

Acesse sua `Collection` (dio-blog), vá em `Base Environment` → `Settings` → `✏️`
Em Base Environments adicione com nome de `host` e edite com o formato `JSON`:

```JSON
{
    "host":"localhost:8000"
}
```

Em seguida `+` `Private Environment`:

* Uma chamada `local`
* Outra chamada produção `prd`

no `prd` configure com a URL gerada, conforme abaixo, também com nome `host` e tipo `JSON`:

```JSON
{
    "host":"https://dio-blog-fastapi-prqo.onrender.com"
}
```

## Criando o banco de dados

Ainda no render → `New +` → [PostgreSQL](https://dashboard.render.com/new/database)

* Name → `dio_blog_fastapi_pg`
* Database → `dio_blog`
* User → `dio_blog`
* Instance Type → `Free`
* e associe ao seu projeto criado anteriormente.

Após isso, volte em `home`, acesse o seu `projeto` e acesse o seu serviço [dio-blog-fastapi](https://dashboard.render.com/web/srv-d51fnushg0os7389spt0):

1. Vá em [Enviroment](https://dashboard.render.com/web/srv-d51fnushg0os7389spt0/env)
2. Clique em `+ ADD ▼` → `Database URL >` e selecione a sua database *dio_blog_fastapi_pg*.

Ficará algo assim:  

`DATABASE_URL`  
`postgresql://dio_blog:TlSjtQU5QWxA0IjKpbr1Y5Tor4V8RPQ3@dpg-d5270bu3jp1c73btfil0-a/dio_blog_xpkm` 

e por fim `Save,rebuild and deploy`.

Coisas para alterar nos nossos arquivos para compatibilidade com o Render:

`add "database[aiosqlite,asyncpg]=" "psycopg2-binary=*"`

No arquivo `database.py`:

```py
import databases
import sqlalchemy as sa

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

database = databases.Database(DATABASE_URL)
metadata = sa.Metadata()

if os.getenv("RENDER"):
    engine = sa.create_engine(DATABASE_URL)
else:
    # check_same_thread não existe em postgres
    engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
```

## Ajustando o problema com o CRUD


Alterado em relação ao timestamp em `models/post.py`:

```py
import sqlalchemy as sa
from src.database import metadata

posts = sa.Table(
    'posts',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(150), nullable=False, unique=True),
    sa.Column('content', sa.String, nullable=False),
    sa.Column('published_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('published', sa.Bollean, default=False),
    )
```

Em `schemas/post.py` retirado `datetime`:

```py
from pydantic import AwareDatetime, BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    published_at: AwareDatetime | None = None
    published: bool = False

class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published_at: datetime | None = None
    published: bool | None = None
```

e na `views/post.py`:

```py
from pydantic import AwareDatetime, BaseModel

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: AwareDatetime | None
```
