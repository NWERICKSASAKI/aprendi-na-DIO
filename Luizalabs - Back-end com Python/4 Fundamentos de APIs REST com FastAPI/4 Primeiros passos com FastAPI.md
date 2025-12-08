# Primeiros passos com FastAPI

## Criando uma aplicação FastAPI

Referências: <https://fastapi.tiangolo.com/>

dio-blog  
├ main.py  
├ poetry.lock  
└ pyprojetc.toml

main.py :

```py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message':'Hello World!!!!'}
```

Após ter inicializado a ENV e recomnfigurado o Interpretador:
`py -m uvicorn main:app --reload`

```txt
INFO:     Will watch for changes in these directories: ['C:\\Users\\erick\\Meu Drive\\Documentos NUVEM\\codes\\Mult\\aprendi-na-DIO\\Luizalabs - Back-end com Python\\4 Fundamentos de APIs REST com FastAPI\\APIs Assincronas com FastAPI\\dio-blog']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
...
```

Ao rodar o uvicorn aparecerá um endereço, ao acessar verá o dicionário com Hello world.

## Estrutura básica de uma API FastAPI

Tem uma proposta similar ao Flask,
Vamos utilizar uma estrutura de pasta similar ao Flask:

```txt
dio-blog
├ controllers
| └
├ models
| └
├ services
| └
├ views
| └
├ main.py
├ poetry.lock
└ pyproject.toml
```

## Rotas e endpoints em FastAPI - Path parameter

Trata-se de receber um atributo via path:
`192.180.0.0.1:800/posts/flask`

```py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/posts/{framework}")
def read_posts(framework: str):
    return {
        "posts":[
            {"title":f"Criando uma aplicação com {framework}", "date":datetime.now()},
            {"title":f"Internacionalizando uma app {framework}", "date":datetime.now()},
        ]
    }
```

## Rotas e endpoints em FastAPI - Query parameters

```py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

fake_db = [
    {"title":f"Criando uma aplicação com Django", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com FastAPI", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com Flask", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com Starlett", "date":datetime.now(), "published": False},

]

@app.get("/")
def read_posts(skip: int = 0, limit: int = len(fake_db), published: bool = True):
    # return fake_db[skip : skip + limit]
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]

@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {
        "posts":[
            {"title":f"Criando uma aplicação com {framework}", "date":datetime.now()},
            {"title":f"Internacionalizando uma app {framework}", "date":datetime.now()},
        ]
    }
```

`192.180.0.0.1:800/posts?skip=1&limit=2`
Assim pula o primeiro elemento e exibe os próximos dois.

Formas de passar valores booleanos `1`, `True`, `true`, `on`, `yes`

`192.180.0.0.1:800/posts?published=off`
Vai retornar só último elemento.

## Rotas e endpoints em FastAPI - Request body

No caso, vamos precisar do software Insomnia para simular o `POST` passando um `JSON` pelo `BODY`.

Para mais detalhes, reassistir a aula....

```py
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = [
    {"title":f"Criando uma aplicação com Django", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com FastAPI", "date":datetime.now(), "published": True},
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now()
    published: bool = False

@app.post('/posts/', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump()) # model_dump() -> retorna a apresentação desta classe como dicionário
    return post
```

## Rotas e endpoints em FastAPI - Cookies e Headers

### Cookies parameters

As vezes precisa recuperar alguns argumentos que o front-end definiu nos cookies do browser.

`ads_id: Annotated[str | None, Cookie()] = None`

```py
from fastapi import Response, Cookie, FastAPI
from typing import Annotated

app = FastAPI()

@app.get("/posts/")
def read_posts(response: Response, limit: int , published: bool, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None):

    # para setar cookies
    response.set_cookie(key='user', value='user@email.com')

    # para ler cookies (com a key especificada)
    print(f"Cookie: {ads_id}")

    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]
```

Ao fazer `GET` pelo Insomnia será necessário configurar adicionando um cookie `Key=ads_id`, passando qualquer `Value` e `Domain=localhost`.  

Para definir um cookie vai precisar da classe `Response` e passar o `key`e `value`.

### Header parameter

```py
from fastapi import Response, Cookie, Header, FastAPI, status
from typing import Annotated
from datetime import datetime

app = FastAPI()

@app.get("/posts/")
def read_posts(
    response: Response,
    limit: int ,
    published: bool,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str|None, Header()] = None):
    response.set_cookie(key='user', value='user@email.com')
    print(f'Cookie: {ads_id}')
    print(f'user-agent: {user_agent}')
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]
```

`user-agent: insomnia/12.1.0`
`user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36`

## Retornando dados em formato JSON

```py
from fastapi import Response, Cookie, Header, FastAPI, status
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

class Foo(BaseModel):
    bar: str
    # message: str

@app.get("/foobar/")
def foobar() -> Foo:
    return {"bar":"foo", "message":"hello"}

# equivalente
@app.get("/foobar/", response_model=Foo)
def foobar() -> dict[str,str]: # <- vira descritivo e não restritivo
    return {"bar":"foo", "message":"hello"}
```

Ao acessar a página aparecerá `{"bar":"foo"}` porque a chave `bar` foi específicada como `string` na classe `Foo(BaseModel)`.

## Organizando as rotas com APIRouter

...