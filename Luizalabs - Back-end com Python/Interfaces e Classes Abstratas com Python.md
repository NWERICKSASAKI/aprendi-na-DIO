# Resumo Python

## Variáveis de classe e Variáveis de instância

### Atributos do objeto

Todos os objetos nascem com o mesmo número de atributos de classe e de instância.  

**Atributos de instância** são diferentes para cada objeto (cada objeto tem uma cópia),  

Já os **atributos de classe** são compartilhados entre os objetos.  

```py
class Estudante:
    # Variavel de classe
    escola = "DIO"

    def __init__(self, nome, numero):
        # Variaveis de instância
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"

gui = Estudante("Guilherme", 123)
gi = Estudante("Giovanna", 456)

print(gui) # Guilherme 123 - DIO

gui.numero = 2
print(gui) # Guilherme 2 - DIO

Escola.escola = "Python" # altera pra todos os objetos
print(gui) # Guilherme 2 - Python

```

## Métodos de classe e Métodos estáticos

### Métodos de classe

Estão ligadas à classe e não ao objeto.  
Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a clase e não para a instâncoa do objeto.

### Métodos estáticos

Não recebe um primeiro argumento explícito.  
Ele também é um método vinculada à classe e não ao objeto da classe.  
Não pode acessar ou modificar o estado da classe.  
Está presente em uma classe porque faz sentido que o método esteja presente na classe.

### Métodos de classe X métodos estáticos

* Um método de classe recebe um 1° parâmetro que apontar para a classe, enquanto um método estático não.  
* Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

### Quando utilizar método de classe ou estático

* Geralmente usamos o **método de classe** para criar métodos de fábrica.  
* Geralmente usamos **métodos estáticos** para criar funções utilitárias.

```py
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    # por convenção utiliza-se cls ou invés de self
    def criar_de_data_nascimento(cls, ano, nome):
        idade = 2025 - ano
        # retorna o próprio objeto, no caso Pessoa(nome, idade)
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p1 = Pessoa("Guilherme",28)

#p2 = Pessoa().criar_de_data_nascimento(1994, "Eldrich") # desta maneira estava criando 2 objetos
p2 = Pessoa.criar_de_data_nascimento(1994, "Eldrich")
print(Pessoa.e_maior_idade(19)) # True
```

## O que são interfaces?

Definem *o que uma classe deve fazer* e não como.

### Python tem interface?

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas.  
Em Python utilizamos classes abstratas parar criar contratos.  
Classes abstratas não pode ser instanciadas.

## Classes Abstratas

### Criando classes abstratas com o módulo abc

Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC.  
O **ABC (*Abstract Base Class*)** funciona decorando métodos da classe vase como abstratos e, em seguida, registrando classes concretas como implementações da base abtrata. Um método se torna abstrato quando decorado com `@abstractmethod`.

```py
from abc import ABC


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):

    def ligar(self):
        print("Ligando TV")

    def desligar(self):
        print("desligando TV")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
```
