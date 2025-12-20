# 1 Manipulação de Dados com FastAPI Assíncrono

## Conexão a bando de dados assíncronos

Referência:  
~~<https://fastapi.tiangolo.com/how-to/async-sql-encode-databases/>~~   
<https://fastapi.xiniushu.com/az/advanced/async-sql-databases/>

`pip install databases[aiosqlite]` ou `poetry add "databases[aiosqlite]"`

*P.S: O Código desta aula foi alterado posteriormente em aulas seguinte, você está vendo o código final.*

`models/post.py`:

```py
import sqlalchemy as sa
from database import metadata

posts = sa.Table(
    'posts',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(150), nullable=False, unique=True),
    sa.Column('content', sa.String, nullable=False),
    sa.Column('published_at', sa.DateTime, nullable=True),
    sa.Column('published', sa.Bollean, default=False),
    )
```

`main.py` (porém ficou obsoleto):

```py
import databases
import sqlalchemy as sa
from controllers import post
from fastapi import FastAPI

DATABASE_URL = 'sqlite:///./blog.db'

database = databases.Database(DATABASE_URL)
metadata = sa.Metadata()
engine = sa.create_engine(DATABASE_URL, connect_arg={'check_same_thread': False})

async def lifespan()

app = FastAPI()
app.include_router(post.router)

# obsoleto
@app.on_event("startup")
async def startup():
    from models.post import posts
    await database.connect()
    metadata.create_all(engine)

# obsoleto
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

```

Mas como o método `on_event` está obsoleto:  

*P.S: O Código desta aula foi alterado posteriormente em aulas seguinte, você está vendo o código final.*

`main.py`:

```py
from contextlib import asynccontextmanager

from controllers import post
from database import database, engine, metadata
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts
    await database.connect()
    metadata.create_all(engine)

    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

```

## Modelos de dados em FastAPI

Criando modelos com Pydantic com `In` e `Out` ou `request` e `response`  

`schemas/post.py`:

```py
from datetime import datetime
from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    published_at: datetime|None = None
    published: bool = False
```

`views/post.py`:

```py
from datetime import datetime
from pydantic import BaseModel

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime|None = None
```

## Operaçõs CRUD assíncronas em APIs RESTful

`controllers/post.py`:

```py
from fastapi import APIRouter, status
from schemas.post import PostIn
from views.post import PostOut
from models.post import posts
from database import database

router = APIRouter(prefix="/post")


@router.get("/", response_model=list[PostOut])
async def read_posts(published:bool, limit:int, skip:int = 0):
    query = posts.select()
    return await database.fetch_all(query)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(title=post.title,
        content=post.content,
        published_at=post.published_at,
        published=post.published,
    )
    last_id = await database.execute(command)
    return {**post.model_dump(), "id":last_id}
```

`database.py`:

```py
import databases
import sqlalchemy as sa

DATABASE_URL = 'sqlite:///./blog.db'

database = databases.Database(DATABASE_URL)
metadata = sa.Metadata()
engine = sa.create_engine(DATABASE_URL, connect_arg={'check_same_thread': False})
```

## Implementação final do CRUD

Vídeo apresentando a solução já completa.
Coisas relavantes:

* `raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")`
* `post.model_dump(exclude_unset=True)` <- remove vamos passados como `None`
