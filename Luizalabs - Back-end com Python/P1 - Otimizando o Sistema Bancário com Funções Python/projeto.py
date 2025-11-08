# código-fonte -> https://github.com/digitalinnovationone/trilha-python-dio/blob/00_fundamentos/00%20-%20Fundamentos/desafio.py

# Objetivo Geral
# Separar as funções exixstentes de saque, depósito e extrato em funções.
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária

# Desafio
# Precisamos deixar nosso código mais modularizarado, para isso
# vamos criar funções para as operações existentes: sacar,
# depositar e visualizar histórico. Além disso, para a versão 2 do
# nosso sistema precisamos criar duas novas funções: criar
# usuário (cliente do banco) e criar conta corrente (vincular com usuário)

# Separação em funções
# Devemos criar funções para todas as operações do sistema.
# Para exercitar tudo o que aprendemos neste módulo, cada
# função vai ter uma regra na passagem de argumentos.
# O retorno e a forma como serão chamadas, pode ser definida por
# você da forma que achar melhor.

# Saque
# A função saque deve receber os argumentos apenas por nome
# (keyword only). Sugestão de argumentos: saldo, valor, extrato,
# limite, numero_saques, limites_saques. Sugestão de retorno: saldo e extrato.

# Depósito
# A função depósito deve receber os argumentos apenas por
# posição (positional only). Sugestão de argumentos: saldo, valor, extrato.
# Sugestão de retorno: saldo e extrato.

# Extrato
# A função extrato deve receber os argumentos por posição e nome
# (positional only e keyword only). Argumentos posicionais: saldo,
# argumentos nomeados: extrato.
 
# Novas funções 
# Precisamos criar duas novas funções: criar usuário e criar conta corrente.
# Fique a votna de para adicionar mais funções, exemplo: listar contas.
 
# Criar usuário (cliente)
# O programa deve armazenar os usuários em uma lista, 
# um usuário é composto por> nome, data de nascimento, cpf e endereço.
# O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
# Deve ser armazenado somente os números do CPF.
# Não podemos cadastrar 2 usuários com o mesmo CPF.

# Criar conta corrente
# O programa deve armazenar contas em uma lista, 
# uma conta é composta por: agência, número da conta e usuário.
# O número da conta é sequencial, iniciando em 1.
# O número da agência é fixo: "0001". 
# O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário. 

# Dica
# Para vincular um usuário a uma conta, filtre a lista de usuários
# buscando o número do CPF informado para cada usuário da lista.


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")