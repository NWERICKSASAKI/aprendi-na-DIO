# 3 Testando APIs RESTFul Assíncronas em FastAPI

## Escrevendo testes para suas APIs assíncronas

Testes unitários
Podemos fazer testes sincronos ou assincronos.

Poderia usar o pytest para testes assíncronos;

`pytest` - para teste unitários
`pytest-asyncio` - adiciona suporte para asyc I/O
`pytest-mock` - para mockar dados necessários
`httpx` - para utilizar o test client para chamada assíncrona

Recomendado configurar no `pyproject.toml` conforme abaixo:
Assim evitará de realizar configurações e confirmações durantes os testes - e o faz de forma automática.

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

O diretório foi reestruturado conforme:

```txt
DIO-BLOG
 |
 ├─ src
 |   |
 |   ├─ controllers
 |   |   |
 |   |   ├
 |   |   └
 |   |
 |   ├─ models
 |   |   |
 |   |   ├
 |   |   └
 |   |
 |   ├─ schemas
 |   |   |
 |   |   ├
 |   |   └
 |   |
 |   ├─ services
 |   |   ├
 |   |   └
 |   |
 |   ├─ views
 |   |   |
 |   |   ├
 |   |   └
 |   |
 |   ├ database.py
 |   ├ main.py
 |   └ security.py
 |
 ├─ test
 |   |
 |   ├─ integration
 |   |   |
 |   |   └─ controllers
 |   |       |
 |   |       ├─ auth
 |   |       |   |
 |   |       |   └ test_login.py
 |   |       |
 |   |       └ post
 |   |          |
 |   |          ├ test_create_post.py
 |   |          ├ test_delete_post.py
 |   |          ├ test_read_all.py
 |   |          ├ test_read_post.py
 |   |          └ test_update_post.py
 |   |
 |   ├ __init__.py
 |   └ conftest.py
 |
 ├ .gitignore
 ├ poetry.lock
 └ pyproject.toml
```

`conftest.py`:

```py
import asyncio
import os

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("DATBASE_URL", f"sqlite:///test.db")

@pytest_asyncio.fixture
async def db(request):
    from src.database import database, engine, metadata
    from src.models.post import posts

    await database.connect()
    metadaa.create_all(engine)

    def teardown():
    # addfinalizar não aceita método assíncrono
    # por isso foi passado um método síncrono com assíncrono    
        async def _teardown():
            await database.disconnect()
            # apaga todas as tabelas
            metadata.drop_all(engine) 

        asyncio.run(_teardown())

    request.addfinalizer(teardown)

@pytest_asyncio.fixture
async def client(db):
    from src.main import app

    transport = ASGITransport(app=app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",

    }
    async with AsyncClient(base_url = "http://test", transport=transport, headers=headers) as client:
        yield client

@pytest_asyncio.fixture
async def access_token(client: AsyncClient):
    response = await client.post("/auth/login", json={"user_id": 1})
    return response.json()["access_token"]
```

`database.py`:

```py
import os
import databases
import sqlalchemy as sa

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
```

`DIO-BLOG/tests/integration/controllers/auth/` `test_login.py`:

```py
from fastapi import status
from httxpx import AsyncClient

async def test_login_success(client: AsyncClient):
    # Given
    data = {"user_id": 1}
    
    # When
    response = await client.post("/auth/login", json=data)
    
    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["access_token"] is not None
```

`DIO-BLOG/tests/integration/controllers/post/` `test_create_post.py`:

```py
from fastapi import status
from httxpx import AsyncClient

async def test_create_post_success(client: AsyncClient, access_token: Str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "title":"post 1",
        "content":"some content",
        "published_at":"2024-04-12T04:33:14.4032",
        "published": True
    }
    
    # When
    response = await client.post("/posts/", json=data, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_201_CREATED
    assert content["id"] is not None

async def test_create_post_invalid_payload_fail(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "content":"some content",
        "published_at":"2024-04-12T04:33:14.4032",
        "published": True
    }
    
    # When
    response = await client.post("/posts/", json=data, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert content["detail"][0]["loc"] == ["body", "title"]

async def test_create_post_not_authenticated_fail(client: AsyncClient):
    # Given
    data = {
        "content":"some content",
        "published_at":"2024-04-12T04:33:14.4032",
        "published": True
    }
    
    # When
    response = await client.post("/posts/", json=data, headers={})
    
    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
```

`DIO-BLOG/tests/integration/controllers/post/` `test_read_all.py`:

```py
import pytest
import pytest_asyncio
from fastapi import status
from httxpx import AsyncClient

# autouse = True, ou seja, quando usar qualquer outra função, este vai rodar primeiro
@pytest_asyncio.fixture(autouse=True)
async def populate_posts(db):
    from src.schemas.post import PostIn
    from src.services.post import PostService

    service = PostService()
    await service.create(PostIn(title="post 1", content="some content", published=True))
    await service.create(PostIn(title="post 2", content="some content", published=True))
    await service.create(PostIn(title="post 3", content="some content", published=False))

# executa 2 testes
# * para 2 published==on
# * para 1 published==off
@pytest.mark.parametrize("published,total", [("on", 2), ("off", 1)])
async def test_read_posts_by_status_success(client: AsyncClient, access_token: Str, published: str, total: int):
    # Given
    params = {"published": published, "limit": 10}
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # When
    response = await client.get("/posts/", params=params, headers=headers)
    
    # Then
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == total

async def test_read_posts_limit_success(client: AsyncClient, access_token: str):
    # Given
    params = {"published": "on", "limit": 1}
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # When
    response = await client.get("/posts/", params=params, headers=headers)
    
    # Then
    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(content) == 1

async def test_read_posts_empty_parameters_fail(client: AsyncClient, access_token: str):
    # Given
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # When
    response = await client.get("/posts/", params={}, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
```

`test_read_post.py`  
`test_delete_post.py`

Para rodar nossos testes: `poetry run pytest -v` ou `poetry run pytest -vvv`  
Ao rodar aparecerá quais deram certo `PASSED` caso os assert não dêem certos retornar `FAILED`.  
