menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta corrente
[l] Listar contas
[v] Listar usuarios
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = [{"nome":"Teste",
             "nascimento":"01/01/1900",
             "cpf":11235813,
             "endereco":"logradouro, 123 - bairro - cidade/UF"}]
contas = [{"agencia":"0001",
           "numero_conta":1,
           "usuario":11235813}]

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
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
    return saldo, extrato

def ver_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return

def criar_usuario(cpf:int):
    global usuarios
    nome = input("Insira o nome completo do novo usuário: ")
    data_nascimento = input("Insira o nascimento do novo usuário (dd/mm/aaaa): ")
    endereco = input("Insira endereço do novo usuário (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append({"nome":nome,
                     "data_nascimento":data_nascimento,
                     "cpf":cpf,
                     "endereco":endereco})
    print("\nUsuario cadastrado!")
    return

def cpf_str_p_int(cpf:str) -> int:
    cpf = cpf.strip()
    cpf = cpf.replace(".","")
    cpf = cpf.replace("-","")
    cpf = cpf.replace(" ","")
    if cpf.isnumeric():
        return int(cpf)
    else:
        return False

def cpf_cadastrado(cpf:int):
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            return True
    else:
        return False

def criar_conta_corrente(cpf:int):
    # O programa deve armazenar contas em uma lista, 
    # uma conta é composta por: agência, número da conta e usuário.
    # O número da conta é sequencial, iniciando em 1.
    # O número da agência é fixo: "0001". 
    # O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    global contas
    AGENCIA = "0001"
    numero_conta = contas[-1]["numero_conta"] + 1
    contas.append({"agencia":AGENCIA, 
                   "numero_conta":numero_conta,
                   "usuario":cpf})
    return

def listar_contas():
    for conta in contas:
        print(conta)
    return

def listar_usuarios():
    for usuario in usuarios:
        print(usuario)
    return



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limites_saques=LIMITE_SAQUES)

    elif opcao == "e":
        ver_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        cpf:str = input("Digite o CPF: ")
        cpf:int = cpf_str_p_int(cpf)
        if cpf:
            if cpf_cadastrado(cpf):
                print("CPF já cadastrado.")
            else:
                criar_usuario(cpf)
        else:
            print('CPF inválido')

    elif opcao == "c":
        cpf:str = input("Digite o CPF: ")
        cpf:int = cpf_str_p_int(cpf)
        if cpf:
            if cpf_cadastrado(cpf):
                criar_conta_corrente(cpf)
            else:
                print("Usuário não cadastrado.")
        else:
            print('CPF inválido')

    elif opcao == "l":
        listar_contas()

    elif opcao == "v":
        listar_usuarios()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")