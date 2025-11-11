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
