# Resumo Python

## Iteradores

É um objeto que contém um número contável de valores que podem ser iterados, o que significa que pode percorrer todos os valores.  

O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais `__iter__()` e `__next__()`  

Exemplos:
* Economizar memória evitando carregar todas as linhas do arquivo;  
* Iterar linha a linha do arquivo.  

```py
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration

for line in FileIterator('large_file.txt'):
    print(line)
```


## Geradores

São tipos especiais de Iteradorores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória.  

São definidos usando funções regulares, mas, ao invés de retornar valores usando `return`, utilizam `yield`.  

Características:  
* Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.  
* O estado interno de um gerador é mantido entre chamadas.  
A execução de um gerador é pausada na declaração `yield` e retomada daí na próxima vez que ele for chamado.  

```py
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?pages={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

for product in fetch_products("http://api.example.com/products"):
    print(product['name'])
```