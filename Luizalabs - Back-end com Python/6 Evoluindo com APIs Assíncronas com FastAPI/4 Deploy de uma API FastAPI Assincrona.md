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
