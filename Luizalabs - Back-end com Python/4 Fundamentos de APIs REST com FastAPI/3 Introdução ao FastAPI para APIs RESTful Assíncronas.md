# 3 Introdução ao FastAPI para APIs RESTful Assíncronas

## Introdução ao FastAPI - seus benefícios e limitações

### História e propósito do FastAPI

**FastAPI** é um moderno framework web para construção de APIs com Python, baseado em padrões como OpenAPI (anteriormente conhecido como *Swagger*) e *JSON Schema*.  

Foi criado por Sebastián Ramírez e lançado em dezembro de 2018, visando proporcionar uma ferramenta que permitia desenvolvimento rápido, fácil de usar e que ofereça alto desempenho.  

Utiliza a tipagem estática para validar dados e gerar documentação automática.  

Desde o seu lançamento, ganhou popularidade por sua simplicidade e eficiência, transformando-se em uma escolha favorita entre desenvolvidores.

### Pontos positivos do FastAPI

* **Alto desempenho** - comparável ao *NodeJS* e superior ao *Flask*.
* **Geração de documentação automática** - suporta *OpenAI* para documentação.
* **Validação de dados e serialização** - Usa *Pydantic* para validação de dados e serialização automática.
* **Facilidade de uso** - Aprender e começar a usar o *FastAPI* pe geralmente considerado simples.
* **Suporte a async/await** - Suporte nativo para operações assíncronas, o que é ótimo para lidar com operações de *IO* (*input/output*).

### Pontos negativos do FastAPI

* **Comunidade menor** - Embora esteja crescendo, sua comunidade ainda é menor em comparação com frameworks estabelecidos como *Django*.  
* **Maturidade** - Por ser relativamente novo, pode faltar alguma maturidade e ter menos plugins quando comparado a outros frameworks mais antigos.  
* **Complexidade em projetos grandes** - Em projetos muito grandes e complexos, a gestão pode se tornar um desafio, especialmente para quem não é acostumado com a tipagem e a programação assíncrona.  
* **Padronização de código** - Em Flask e Django já há uma padronização, já em FastAPI trabalha com funções assíncronas que pode ser dificultoso àqueles que não tem familiaridade.  

## Instalação do FastAPI e configuração do ambiente de desenvolvimento

Diretório exemplo:
13 - APIs Assincronas com FastAPI
└ /dio-blog

Padrão:

```bash
pip install fastapi
pip install "unicon[standard]
```

Recomendado (via poetry):

```bash
poetry init
poetry add 'fastapi=*'
poetry env info
poetry add "uvicorn[standard]"
```

Observação, ao rodar o `poetry env info` após instalar o *fastapi* o Poetry inicilizará o ambiente virtual e aparecerá o `Path` do interpretador do Python do ambiente virtual:

```bash
Virtualenv
Python:         3.14.0
Implementation: CPython
Path:           C:\Users\erick\AppData\Local\pypoetry\Cache\virtualenvs\dio-blog-6h2gzqGZ-py3.14
Executable:     C:\Users\erick\AppData\Local\pypoetry\Cache\virtualenvs\dio-blog-6h2gzqGZ-py3.14\Scripts\python.exe  
Valid:          True
```

Copiar o `Path`, ou seja, `C:\Users\erick\AppData\Local\pypoetry\Cache\virtualenvs\dio-blog-6h2gzqGZ-py3.14` e aperta CTRL+SHIFT+P, procure por `selecionar interpretador` e depois `insira o caminho do interpretador` e cole.  

Pra testar, abra um novo terminal e:

```bash
python
import fastapi
```

Se não acusar nenhum erro, é porque deu certo.
