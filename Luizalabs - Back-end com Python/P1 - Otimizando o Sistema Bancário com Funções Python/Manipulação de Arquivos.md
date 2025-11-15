# Resumo Python

## Manipulação de Arquivos

Um arquivo é um container no computador onde as informações são armazenadas em formato digital.  

Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto ee arquivos binários.  

Com manipulação de arquivos é possível persistir dados.

### Abrindo e Fechando arquivos

Para abrir `open()` e para fechar `close()`.  

Se estiver com arquivo aberto e não estiver o utilizando, há um desperdício computacional.  

```py
file = open("arquivo.txt", "r"):
# ... fazemos algo com o arquivo
file.close()
```  
#### Modos de abertura de arquivo
* `r` somente leitura  
* `w` gravação  
* `a` anexar  

#### Maneiras de ler um arquivo
* `read()` - lê todo o conteúdo de uma vez  
* `readline()` - lê uma linha por vez   
* `readlines()` - retorna todo conteúdo em uma lista, cada elemento é uma linha.  

```py
arquivo = open(path, 'r')  
while len(linha := arquivo.readline()):  
    print(linha)  
arquivo.close()  
```
#### Maneiras de escrever em um arquivo
* `write()` - escreve uma str    
* `writelines()` - escreve um iterador  

```py
arquivo = open(path, 'w')  
arquivo.write("EScrevendo um dado")  
arquivo.writelines(["\n","Escrevendo outro dado","\n"])  
arquivo.close()  
```

#### Gerenciando arquivos e diretórios

Podemos criar, renomear e excluir arquivos e diretórios usando os módulos `os` e
`shutil`.  

```py
from pathlib import Path

# retorna o caminho absoluto da pasta atual deste script
ROOT_PATH = Path(__file__).parent

# cria uma nova-pasta (independente do OS)
os.mkdir(ROOT_PATH / 'nova-pasta')

# criando um arquivo txt
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# renomeando
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# movendo
shutil.move(ROOT_PATH / "alterado.txt", ROOT_PATH /"nova-pasta" / "alterado.txt")

# removendo
os.remove(ROOT_PATH / "nova-pasta" / "alterado.txt")
```

#### Tratamento de Exceção

* `FileNotFoundError` - Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.
* `PermissionError` - Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.
* `IOError` - Lançada quando ocorre um erro geral de IO (Input / Output) ao trabalhar com o arquivo, como *problemas de permissão*, *falta de espaço em disco*, etc.  
* `UnicodeDecodeError` - Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
* `UnicodeEncodeError` - Lançada quando ocorre um erro ao tentar codificar os dados de uma determinada codificação ao gravar em um arquivo de texto.
* `IsADirectoryError` - Lançada quando é feita uma tentativa de abrir um diretóprio em vez de um arquivo de texto.

```py
try:
    file = open('non_existent.txt', 'r')
except FileNotFoundError as detalhes_da_excecao:
    print('Arquivo não encontrado, ', detalhes_da_excecao)
except Exception as detalhes_da_excecao: # demais erros
    print(detalhes_da_excecao)
```

### Boas Práticas

#### Bloco with
Use o gerenciamneto de contexto (context manager) com a declaração `with`.  
O gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.  

```py
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
    print(arquivo.read())
```

#### Verifique se o arquivo foi aberto com sucesso
É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele.

```py
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'lorem.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as e:
    print('Erro ao abrir o arquivo: ',e)
```

#### Use a codificação correta
Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto. O argument `encoding` da função `open()` permite especificar a codificação.

```py
with open(ROOT_PATH / 'lorem.txt', 'r', encoding='utf-8') as arquivo:
```


## Trabalhando com arquivo CSV

*Comma Separated Values (Valores separados por vírgulas)*.  
Um formato de arquivo de texto utilizado para armazenar dados em formato tabulares.

O Python fornece um módulo chamado `csv` para lidar facilmente com arquivos CSV.

```py
import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Lendo
with open(ROOT_PATH / 'example.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Gravando
with open(ROOT_PATH / 'example.csv','r', newline='') as file:
    writer = csv.writef(file)
    writer.writerow(["nome","idade"])
    writer.writerow(["Ana",30])
    writer.writerow(["Joao",25])
```

### Boa práticas
* Usar o `csv.reader` e `csv.write` para manipular arquivos CSV.
* Utilizar `newline('')` como argumento no open no modo write.
* Fazer o tratamento correto das exceções.
