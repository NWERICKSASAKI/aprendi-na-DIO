# Resumo Python

## Funções são objetos de 1° classe

As funções pode ser passadas e usadas como argumentos

```py
def dizer(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Python juntos"

def mensagem_para_guilherme(funcao_mensagem):
return funcao_mensagem("Guilherme")

mensagem_para_guilherme(dizer_oi)

mensagem_para_guilherme(incentivar_aprender)
```

`Oi Guilherme`  
`Oi Guilherme, vamos aprender Python juntos`



## Decoradores

### Inner functions (funções internas)

É possível definir funções dentro de outras funções.

``` py
def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")

    def filho2():
        print("Escrevendo da filho2() função")

    filho2()
    filho1()

pai()
```

`Escrevendo da pai() função`  
`Escrevendo da filho2() função`  
`Escrevendo da filho1() função`  


```py
def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair

resultado = calcular("+")(1,3)
print(resultado)
```

`4`

```py
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope()

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()
```
`Faz algo antes de executar a função.`  
`Olá mundo!`  
`Faz algo depois de executar a função.`  

### Açúcar Sintático

O Python permite que você use decoradores de maneira mais simples com o símbolo @.


```py
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função.")
        funcao()
        print("Faz algo depois de executar a função.")
    
    return envelope()

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

ola_mundo()
```
`Faz algo antes de executar a função.`  
`Olá mundo!`  
`Faz algo depois de executar a função.`  

## Funcções de decoração com argumentos

Podemos usar ***args** e ****kwargs**  na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais      e palavras-chave.  

```python
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python)
```

`Estou aprendendo Python`  
`Estou aprendendo Python`  

### Instrospecção

É a capacidade de um objeto de um objeto saber sobre seus próprios atributos em tempo de execução.  

