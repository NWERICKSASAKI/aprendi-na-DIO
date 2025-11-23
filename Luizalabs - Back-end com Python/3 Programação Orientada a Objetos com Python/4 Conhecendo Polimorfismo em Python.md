# Resumo Python

## O que é Polimorfismo?

A palavra polimorfismo significa ter muitas formas.  
Na programação, **polimorfismo** significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.

```py
len("phyton") # 6
len([1,2,3]) # 3
```

## Polimorfismo com herança

### Mesmo método com comportamento diferente

Na **herança**, a classe filha herda os métodos da classe pai.  
No entando, é possível modificar um método em uma classe filha herdada pelo pai.  
Isso é particularmente útil nos casos em que o método herdado da classe pai não de encaixa perfeitamente na classe filha.

```py
class Passaro:
    def voar(self):
        print("Voando")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
plano_voo(p1) # Voando

plano_voo(Avestruz()) # Avestruz não pode voar
```
