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

## Boas práticas

Python tem um a série de convenções e melhores práticas codificadas em PEPs (Propostas de Melhoria do Python). A mais conhecida destas é provavelmente a PEP 8, que cobre o estilo de codificação.

### O que é PEP 8?

[PEP8](http://peps.python.org/pep-0008/) é o guia de estilo para codificação em Python. Ele inclui convenções sobre nome de variáveis, uso de espaços em branco, comprimento da linha e muitas outras coisas que ajudam a manter o código Python consistente e legível.

Algumas das principais recomendações:

* usar 4 espaçoes para identação,
* limitar as linhas a 79 caracteres,
* snake_case para funções e variáveis,
* CamelCase para classes.

### Uso de ferramentas de checagem de estilo

Para nos ajudar a seguir as recomendações da PEP 8, podemos usar ferramentas de checagem de estilo como flake8. Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo.

```bash
pip install flake8
flake8 meu_script.py
```

### Formatação automática de código

**Black** é uma ferramenta de formatação de código Python que segue a filosofia "formato único". Black reformata todo o seu arquivo em um estilo consistente, simplificando a tarefa de manter o código em conformidade com a PEP 8.

```bash
pip install black
black meu_script.py
```

### Organização de imports com isort

**Isort** é uma ferramenta Python para classificar importações alfabeticamente e separá-las automaticamente em seções. Ele proporciona uma maneira rápida e fácil de ordenar e categorizar suas importações.

```bash
pip install isort
isort meu_script.py
```

VSCode - extensão: Fonte Microsoft

* Black formatter
* isort
