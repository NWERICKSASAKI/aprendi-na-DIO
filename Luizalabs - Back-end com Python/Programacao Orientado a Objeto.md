# Resumo Python

## O que é Orientação a Objetos (OO)?

### Paradigmas de programação

Um paradigma de programação é um estilo e programação. Não é uma linguaguem, e sim a forma como você soluciona os problemas através do código.

### Alguns paradigmas

* Imperativo ou procedural
* Funcional
* Orientado a eventos

### Programação orientada a objetos

O paradigma de programação orientada a objetos estrutura o código abastraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: classes e objetos.

## Os conceitos de Classes e Objetos

### Conceito de classes e objetos

Uma **classe** define as características e comportamentos de um objetos, porém não conseguimos usá-las diretamente.  
Já os **objetos** podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

## Construtores e Destrutores

### Método construtor

O **método construtor** sempre é executado quando uma nova instância da classe é criada.  
Nesse método inicializamos o estado do nosso objeto.  
Para declarar o **método construtor** da classe, criamos um método com o none `__init__`.

### Método destrutor

O **método destrutor** sempre é executado quando uma instância (objeto) é destruída.  
**Destrutores** em Python não são tão necessários quanto em C++ porque o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente.  
Para declarar o **método destrutor** da classe, criamos um método com o nome `__del__`.

```py
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro()
# del c
```

Assim que executar o código acima, o `__del__` será executado assim que o programa for encerrado ou quando `del` for utilizado.
