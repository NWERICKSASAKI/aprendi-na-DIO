# 6 Explorando Conjuntos em Python

## 6.1 Conjuntos

## 6.1.1 Valores únicos

Há duas formas de definir conjuntos, usando `{valores_iteraveis}` ou usando `set(valores_iteraveis)` em valores iteráveis.  

Inicialmente pode ser aplicado em uma lista com itens repetidos e para manter um conjunto de valores únicos:

`set(["python", "java", "python"]) # {python, java}`

## 6.1.2 União

Assim como em conjuntos em matemática é possível aplicar a união, que retorna todos os valores de ambos os conjuntos:

```py
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.union(conjunto_b) # {1,2,3,4,5}
```

## 6.1.3 Intersecção

Existe também interseção, que retorna os valores comum nos conjuntos.

```py
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.intersection(conjunto_b) # {3}
```

## 6.1.4 Diferença

Neste retorna apenas o que o segundo conjunto tem de diferente.

```py
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.difference(conjunto_b) # {4,5}
conjunto_b.difference(conjunto_a) # {1,2}
```

## 6.1.5 Diferença Simétrica

Retorna todos os valores exceto os comums

```py
conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.symmetric_difference(conjunto_b) # {1,2,4,5}
```

## 6.1.6 Contido

A está contido em B?  
Retorna `True` se o primeiro conjunto estiver contido no segundo.

```py
conjunto_b = {3,4,5}
conjunto_c = {4}

conjunto_c.issubset(conjunto_b) # True
```

## 6.1.6 Contém

A contém B?  
Retorna `True` se o primeiro conjunto contém o segundo.

```py
conjunto_b = {3,4,5}
conjunto_c = {4}

conjunto_c.issuperset(conjunto_b) # False
```

## 6.1.7 Disjunto

A e B tem valores em comum? Não? Então são disjuntos! (Retorna `True` nesse caso)

```py
conjunto_a = {1,2,3}
conjunto_c = {4}

conjunto_a.isdisjoint(conjunto_c) # True
```

## 6.1.8 Adicionar valor

Adiciona um valores no conjunto (Se já não houver, né)

```py
sorteio = {1,23}
sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}
```

## 6.1.9 Clear

Esvazia conjunto...

```py
sorteio = {1,23}
sorteio # {1, 23}
sorteio.clear()
sorteio # {}
```

## 6.1.10 Copy

Hard copy do conjunto (mas se alterar um não altera o outro)

```py
sorteio_1 = {1,23}
sorteio_2 = sorteio_1.copy()
sorteio_2 # {1, 23}
```

## 6.1.11 Remover valor (se houver)

Remove um valores no conjunto (Se já houver, né)

```py
sorteio = {1,23}
sorteio.discard(25)
sorteio.discard(23)
sorteio # {1}
```

## 6.1.12 Remover valor (COMO ASSIM NÃO TEM???)

Remove um valores no conjunto (Se não houver dá erro!)

```py
sorteio = {1,23}
sorteio.discard(23) # 23
sorteio.discard(25) # ERROOOO!
sorteio # {1} <- Se ignora a linha de erro
```

## 6.1.13 Pop

Remove do conjunto o 1° valor e o retorna.

```py
sorteio = {1,23}
sorteio.pop() # 1
sorteio # {23}
```

## 6.1.14 Len

Retorna o tamanho do conjunto

```py
sorteio = {1,2,2,3,3,3}
sorteio.len() # 3 (pq removeu os duplicados)
```

## 6.1.15 In

O valor está no conjunto?

```py
sorteio = {1,2,2,3,3,3}
4 in sorteio # False
2 in sorteio # True
```
