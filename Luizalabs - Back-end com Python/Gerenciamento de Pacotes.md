# Resumo Python

## Gerenciamento de pacotes e Boas práticas

### O que são pacotes em Python?

Pacotes são módulos que podem ser instalados e utilizados em seus programas Python.  
Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.

### O papel do pip

Pip é o gerenciado de pacotes do Python. Ele nos permite instalar, utilizar e remover pacotes facilmente.  
Ele se comunica com o [PyPI](https://pypi.org) (*Python Package Index*), que é onde a maioria dos pacotes Python são armazenados.  

```bash
pip install numpy
pip uninstall numpy
pip list
```

### Uso de ambientes virtuais

Ambientes virtuais, como os criados por *venvs*, nos permitem manter as dependências de diferentes projetos.  
Isso é importante para evitar conflitos entre versões de pacotes.  

```bash
# Criar o ambiente virtual "myenv"
python3 -m venv myenv

# Entrar no ambiente virtual "myenv"
source myenv/bin/active

# Encerra o ambiente virtual
deactivate
```

### Comandos do pip

Como um programador que está aprendendo Python e deseja gerenciar os pacotes do seu projeto, é importante conhecer alguns dos principais comandos do pip.

```bash
# Instalar um pacote
pip install nome_do_pacote

# Desinstalar um pacote
pip uninstall nome_do_pacote

# Listar pacotes instalados
pip list

# Atualizar um pacote
pip install --upgrade nome_do_pacote

# Procurar por pacotes
pip search termo_de_busca
```

## Gerenciando dependência com Pipenv

### Introdução ao pipenv

**Pipenv** é uma ferramente de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambientes virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo *Pipfile* conforme você instala e desinstala pacotes.

```bash
# Instalação global do pipenv
pip install pipenv

# 
pipenv install numpy

# desinstala um pacote
pipenv uninstall numpy

# remove todos os subpacotes que antes eram dependentes
pipenv clean

# gerar um arquivo de fechamento (lock de dependencias)
pipenv lock

# lista todas as dependências
pipenv graph

# atualiza as versões
pipenv upgrade
```

### Gerenciando dependências com Poetry

**Poetry** é outra ferramenta de gerenciamento de dependências para Python que permite declarar as bibliotes de que seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você. Ela também suporta o empacotamento e a publicação de projetos no PyPI.

```bash
pip install poetry
poetry new myproject
cd myproject
poetry add numpy

# remove numpy e suas dependências
poetry remove numpy

# 
poetry init

# Cria o ambiente virtual
poetry install
```

