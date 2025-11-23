# Resumo Python

## O que encapsulamento

### Proteção de acesso

O **encapsulamento** é um dos conceitos fundamentais em programação orientada a objetos.  
Ele descreve a ideia de *agrupar dados e os métodos* que manipulam esses dados em uma unidade.  
Isso impõe *restrições ao acesso direto* a variáveis e métodos e pode evitar a modificação acidental de dados.  
Para evitar alterações acidentais, a variável de um objeto *só pode ser alterada pelo método* desse objeto.

## Recursos públicos e privados

### Modificadores de acesso

Em linguagens como Java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e métodos da classe.  
Em Python não temos palavras reservadas, porém *usamos convenções* no nome do recurso, para definir se a variável é pública ou privada.

* **Privado**: inicia com `_` - só pode ser acessado pela classe
* **Público**: sem underline, pode ser acessado fora da classe

### Público/Privado

Em Python, todos os recursos são públicos, a menos que o nome inicie com underline.  
Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe.

```Py
class Conta:
    def __init__(self, saldo=0):
        # propriedade privada
        self._saldo = saldo

    # método público
    def depositar(self,valor):
        pass
```

## Propriedades

### Para que servem?

Com o `property()` do Python, você pode criar atributos gerenciados em suas classes.  
Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisa modificar sua implementação interna sem alterar a API pública da classe.

**Decorador** é uma função que executa antes da sua função

```py
class Foo:
    def __init__(self, x=None):
        self._x = x
    
    # atributo x vai estar disponível em sua classe
    # a função abaixo será interpretada como variavel
    @property
    def x(self):
        return self._x or 0

    # p/ inferir o processo de atribuição
    @x.setter
    def x(self, value):
        _x = self._x = 0
        _value = value or 0
        self._x = _x + _value
     
    # p/ inferir o processo de deleção
    # ao invés de excluir, diminui em um
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x) # 10

foo.x = 10
print(foo.x) # 20

del foo.x
print(foo.x) # 10
```
