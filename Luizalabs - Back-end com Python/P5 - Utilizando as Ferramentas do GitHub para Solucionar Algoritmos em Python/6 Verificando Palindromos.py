# Testar se uma palavra é um palíndromo

palavra = input("Digite uma palavra: ")

palindromo = True
for i in range(len(palavra)):
    if palavra[i] != palavra[-1-i]:
        palindromo = False

if palindromo:
    print(f"A palavra {palavra} é um palindromo")
else:
    print(f"A palavra {palavra} não é um palindromo")