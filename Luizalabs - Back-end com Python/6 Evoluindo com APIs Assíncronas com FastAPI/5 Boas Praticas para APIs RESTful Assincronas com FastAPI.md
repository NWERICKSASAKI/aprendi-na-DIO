# 5 Boas Práticas para APIs RESTful Assíncronas com FastAPI

## Tratamento de erros

`src/controllers/services/post.py`:

```py
from databases.interfaces import Record
from src.exceptions import NotFoundPostError

# removido as dependencias de fastapi pra caso utilizar outro framewok ou se estiver em produção
# from fastapi import HTTPException, status

from src.database import database
from src.models.post import posts
from src.schemas.post import PostIn, PostUpdateIn

class PostService:
    async def read_all(self, published: bool, limit: int, skip: int = 0) -> list[Record]:
        query = posts.select().where(posts.c.published == published).limit(limit).offset(skip)
        return await databse.fetch_all(query)
    
    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        return await database.execute(command)
    
    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def update(self, id: int, post: PostUpdateIn) -> Record:
        if not total:
            # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
            raise NotFoundPostError

        data = post.model_dump(excluse_unset=True)
        command = post.update().where(post.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)

    async def count(self, id: int) -> int:
        query = "SELECT count(id) AS total FROM posts WHERE id = :id"
        result = await database.fetch_one(query, {"id":id})
        return result.total

    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            # não é recomendado retornar HTTP Exception aqui pois se você fizer uma chamada via CLI não faz sentido ter retorno do protocolo HTTP
            # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
            raise NotFoundPostError
        return post
```

`src/exceptions.py`:

```py
class NotFoundPostError(Exception):
    # pass
    from http import HTTPStatus

    def __init__(self, message: str="Post not found", status_code: int=HTTPStatus.NOT_FOUND) -> None:
        self.message = message
        self.status_code = status_code
```

Editando assim, não obteremos erros de protocolo HTTP se utilizarmos via terminal e nem ficaremos dependentes do `fastapi` para caso estivermos utilizando outros frameworks.  

Mas quando fizermos uma requisição via API acusará `Erro 500 - Erro Interno do Servidor`, para formatar bonitinho:

`src/controllers/post.py`:

```py
from fastapi import APIRouter, Depends, status

from src.exceptions import NotFoundPostError
from src.schemas.post import PostIn, PostUpdateIn
from src.security import login_required
from src.services.post import PostService
from src.views.post import PostOut

router = APIRouter(prefix="/post", dependencies=[Depends(login_required)])

service = PostService()

@router.get("/", response_model=list[PostOut]) 
async def read_posts(published:bool, limit:int, skip:int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    try:
        return {**post.model_dump(), "id": await service.create(post)}
    except NotFoundPostError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.get("/{id}",response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)

@router.patch("/{id}",response_model=PostOut)
async def update_post(id: int):
    try:
        return await service.update(id=id, post=post)
    except NotFoundPostError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=PostOut)
async def delete_post(id: int):
    await service.delete(id=id)
```

Mas para ficar evitando de usar esse mesmo bloco de código para tratamento personalizado...

```py
    try:
        return await service.update(id=id, post=post)
    except NotFoundPostError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
```

...podemos usar o decorador `@app.exception_handler(UnicornException)`.  

Vamos abrir o `src/main.py`:

```py
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions import NotFoundPostError
from src.controllers import auth, post
from src.database import database, engine, metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(post.router)

@app.exception_handler(NotFoundPostError)
async def not_found_post_exception_handdler(request: Request, exc: NotFoundPostError):
    return JSONResponse(
        status_code=status.status_code,
        content={"detail": exc.message},
    )
```

então vamos editar aquele bloco e retirar os `try`s e só deixar os returns.

`src/controllers/post.py`:

```py
from fastapi import APIRouter, Depends, status

from src.schemas.post import PostIn, PostUpdateIn
from src.security import login_required
from src.services.post import PostService
from src.views.post import PostOut

router = APIRouter(prefix="/post", dependencies=[Depends(login_required)])

service = PostService()

@router.get("/", response_model=list[PostOut]) 
async def read_posts(published:bool, limit:int, skip:int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return {**post.model_dump(), "id": await service.create(post)}
    
@router.get("/{id}",response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)

@router.patch("/{id}",response_model=PostOut)
async def update_post(id: int):
    return await service.update(id=id, post=post)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=PostOut)
async def delete_post(id: int):
    await service.delete(id=id)
```

Além disso com a personalização do tratamento de erro lá na main:

`src/controllers/services/post.py`:

```py
from databases.interfaces import Record
from src.exceptions import NotFoundPostError
from src.database import database
from src.models.post import posts
from src.schemas.post import PostIn, PostUpdateIn
# from http import HTTPStatus

class PostService:
    async def read_all(self, published: bool, limit: int, skip: int = 0) -> list[Record]:
        query = posts.select().where(posts.c.published == published).limit(limit).offset(skip)
        return await databse.fetch_all(query)
    
    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        return await database.execute(command)
    
    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def update(self, id: int, post: PostUpdateIn) -> Record:
        if not total:
            # pq não faz sentifo ter resposta de protocolo HTTP aqui
            # raise NotFoundPostError(message='Post not found, in the service', status_code=HTTPStatus.NOT_FOUND)
            raise NotFoundPostError

        data = post.model_dump(excluse_unset=True)
        command = post.update().where(post.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)

    async def count(self, id: int) -> int:
        query = "SELECT count(id) AS total FROM posts WHERE id = :id"
        result = await database.fetch_one(query, {"id":id})
        return result.total

    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise NotFoundPostError#(message='Post not found, in the service', status_code=404)
        return post
```

## Documentação automática

Alterando parâmetros do objeto FastAPI é possível personalizá-lo:

`src/main.py`:

```py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

[...]

tags_metadata = [
    {
        "name": "auth",
        "description": "Operações para autenticação.",
    },
    {
        "name": "post",
        "description": "Operações para manter posts",
        "externalDocs": {
            "description": "Documentação externa para Posts.api",
            "url": "https://post-api.com/",
        },
    },
]

servers=[
    {"url": "https://servidor-de-teste.com", "description": "Stagins environment"},
    {"url": "https://servidor-de-producao.com", "description": "Production environment"},
]

description = """
DIO blog API ajuda você a criar seu blog pessoal

## Posts

Você será capaz de fazer:

* **Criar posts**
* **Recuperar posts**
* **Recuperar posts por ID**
* **Atualizar posts**
* **Deletar posts**

[...]
"""

app = FastAPI(
    title = "Dio blog API", # para substituir o título padrão "FastAPI" da documentação
    version = "1.0.2", 
    summary = "API para blog pessoal.",
    description = description, # aceita markdown
    openapi_url = None, # para desabilitar a documentação em http://localhost:8000/docs e http://localhost:8000/redocs
    openapi_tags=tags_metadata, # para adicionar metadatas conforme escrito acima
    servers=servers, # aqui pode passar seus servidores, para poder selecionar o servidor para fazer requisição
    redoc_url = None, # desabilita ou personaliza o Redoc
    lifespan=lifespan,
    )

app.include_router(auth.route, tags=["auth"]) # mas pode definir na função router dentro do controllers
app.include_router(post.router, tags=["post"])

[...]
```

## Resolvendo o problema de CORS

Esse erro ocorre quando roda o **backend** e **frontend** de origens diferentes.  
Por que isso ocorre?
Porque seu frontend roda em uma **porta** e seu backend roda em outra:

* Isso não ocorre quando usamos o FastAPI no nosso computador.  
* Mas ocorreu quando rodar a interface local apontando pra produção.

Dentro do FastAPI é possível instalar `Middleware`, que permite alterar ou adicionar algum comportamento durante a requisição/resposta. Ele já resolve o problema cruzado.

`src/main.py`:

```py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware import CORSMiddleware

[...]

app = FastAPI(
    [...]
    lifespan=lifespan,
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(post.router)

[...]
```
