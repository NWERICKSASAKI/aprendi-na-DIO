# Resumo Python

## Herança em POO

Em programção **herança** é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

### Benefícios

* Representa bem os relacionamentos do mundo real.
* Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
* É de natura transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

## Herança Simples

Quando uma classe filha herda apenas uma classe pai.

```py
class A:
    pass
    
class B(A): # B é filha de A
    pass
```

```py
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('ligando motor')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

moto = Motocicleta('azul','ABC-1234',2)
moto.ligar_motor()
```

## Herança Múltipla

Quando uma classe filha herda de várias classes pai.

```Py
class A:
    pass
    
class B:
    pass

class C(A,B):
    pass
```

```Py
class Animal:
    def __init__(self, n_patas):
        n_patas = n_patas

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Ornitorrinco(Mamifeto, Ave):
    def __init__(self, cor_bico, cor_pelo, n_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, n_patas=n_patas)

ornitorrinco = Ornitorrinco(n_patas=2, cor_pelo='vermelho', cor_bico='laranja')
```
