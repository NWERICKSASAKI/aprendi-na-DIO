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


