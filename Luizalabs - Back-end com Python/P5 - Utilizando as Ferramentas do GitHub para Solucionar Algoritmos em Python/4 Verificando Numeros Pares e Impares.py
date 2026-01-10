# Receba um número inteiro e verifique se ele é par ou ímpar

um_numero = int(input("Digite um número: "))
eh_par = um_numero % 2 == 0

if(eh_par): 
    print("É par")
else:
    print("É ímpar")