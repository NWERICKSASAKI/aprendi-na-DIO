from abc import ABC, abstractmethod
from datetime import date
import textwrap


class Conta:
    def __init__(self, saldo:float, numero:float, agencia:str, cliente:Cliente, historico:Historico):
        self._saldo:float = saldo
        self._numero:int = numero
        self._agencia:str = agencia
        self._cliente:Cliente = cliente
        self._historico:Historico = Historico()

        @property
        def saldo(self) -> float:
            return self._saldo
        
        @classmethod
        def nova_conta(cls, cliente:Cliente, numero:int) -> Conta:
            # input para solicitar dados da conta
            return cls(cliente, numero)

        def sacar(self, valor:float) -> bool:
            excedeu_saldo = valor > self._saldo
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                return False
            elif valor > 0:
                transacao_saque = Saque(valor)
                cliente.realizar_transacao(self, transacao_saque)
                # extrato += f"Saque: R$ {valor:.2f}\n"
                return True
            else:
                print("Operação falhou! O valor informado é inválido.")
                return False

        def depositar(self, valor:float) -> bool:
            if valor > 0:
                self._saldo += valor
                # extrato += f"Depósito: R$ {valor:.2f}\n"
                return True
            else:
                print("Operação falhou! O valor informado é inválido.")
                return False

class ContaCorrente(Conta):
    def __init__(self, cliente:Cliente, numero:int, limite:float=500, limite_saques:int=3):
        super().__init__(cliente, numero)
        self._limite:float = limite
        self._limite_saques:int = limite_saques
        self.numero_saques:int = 0

    @property
    def saldo(self) -> float:
        return super().saldo

    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int) -> Conta:
        return super().nova_conta(cliente, numero)


    def sacar(self, valor:float) -> bool:
        excedeu_limite = valor > self._limite
        excedeu_saques = self.numero_saques >= self._limite_saques
        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False
        else: # nada de errado até então
            sacou = super().sacar(valor)
            if sacou:
                self.numero_saques += 1
            return sacou


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta) -> None:
        pass


class Deposito(Transacao):
    def __init___(self, valor:float=0.0):
        self._valor = valor

    def registrar(self, conta:Conta):
        conta._historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor:float=0.0):
        self._valor = valor

    def registrar(self, conta:Conta):
        conta._historico.adicionar_transacao(self)
        conta._saldo -= self._valor

class Historico:
    def __init__(self):
        self._transacoes:list = []

    def adicionar_transacao(self, transacao:Transacao):
        self._transacoes.append(transacao)


class Cliente:
    def __init__(self, endereco:str, contas:list=[]):
        self._endereco:str = endereco
        self._contas:list = contas

    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        pass

    def adicionar_conta(self, conta:Conta) -> None:
        nova_conta = Conta.adicionar_conta(self, conta)
        self._contas.append(nova_conta)

class PessoaFisica(Cliente):

    def __init__(self, cpf:str, nome:str, data_nascimento:date, endereco:str, contas:list=[]):
        super().__init__(endereco, contas)
        self._cpf:str = cpf
        self._nome:str = nome
        self._data_nascimento:date = data_nascimento

    def realizar_transacao(self, conta, transacao):
        return super().realizar_transacao(conta, transacao)
    
    def adicionar_conta(self, conta):
        return super().adicionar_conta(conta)


class SistemaBanco:

    def __init__(self, clientes:list=[]):
        self._clientes:list = clientes

    def _criar_usuario(self, cpf:int,) -> PessoaFisica:
        nome = input("Insira o nome completo do novo usuário: ")
        data_nascimento = input("Insira o nascimento do novo usuário (dd/mm/aaaa): ")
        endereco = input("Insira endereço do novo usuário (logradouro, nro - bairro - cidade/UF): ")
        novo_usuario = PessoaFisica(cpf=cpf,
                                   nome=nome,
                                   data_nascimento=data_nascimento,
                                   endereco=endereco)
        self._clientes.append(novo_usuario)
        print("\nUsuario cadastrado!")
        return novo_usuario

    @staticmethod
    def cpf_so_numero(cpf:str) -> str|bool:
        cpf = cpf.strip()
        cpf = cpf.replace(".","")
        cpf = cpf.replace("-","")
        cpf = cpf.replace(" ","")
        if cpf.isnumeric():
            return cpf
        else:
            return False

    def ir_para_tela_inicial(self) -> None:
        print("Bem-vindo!")
        cpf = input("Informe o seu CPF (somente números): ")
        cpf = self.cpf_so_numero(cpf)
        if cpf:
            usuario = self._cliente_cadastrado(cpf)
            if not usuario:
                usuario = self._criar_usuario(cpf)
            self.ir_para_tela_cliente(usuario)
        else:
            print("CPF inválido. Tente novamente.")
        return


    def printar_contas(self, cliente) -> None:
        contas = cliente._contas
        if contas:
            for conta in contas:
                print(f"Agência: {conta._agencia} | Conta: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
        else:
            print("Nenhuma conta cadastrada.")


    def ir_para_tela_cliente(self, cliente:PessoaFisica):
        print(f"Bem-vindo, {cliente._nome}!")
        menu = """
        Escolha uma opção:

        [a] Acessar conta
        [c] Criar conta
        [q] Sair

        => """
        menu = textwrap.dedent(menu)
        
        letra = ""
        while not letra == "q":
            self.printar_contas(cliente)
            letra = input(menu)
            match letra:
                # Acessar conta
                case "a":
                    numero_conta = input("Informe o número da conta: ")
                    if numero_conta.isnumeric():
                        numero_conta = int(numero_conta)
                        if numero_conta <= len(cliente._contas):
                            self.ir_para_tela_conta(cliente._contas[numero_conta-1])
                    print("Número da conta inválido.")

                # Criar conta
                case "c":
                    nova_conta:Conta = ContaCorrente.nova_conta(cliente, len(cliente._contas)+1)
                    cliente.adicionar_conta(nova_conta)
                    print("\nConta criada com sucesso!")

                case _:
                    print("Opção inválida, tente novamente.")
        return
    
    def ir_para_tela_conta(self, conta:Conta):
        menu = f"""
        Acessando conta {conta._numero}...
        Escolha uma opção:

        [d] Depositar
        [s] Sacar
        [h] Histórico
        [q] Voltar
        => """
        menu = textwrap.dedent(menu)

        letra = ""
        while not letra == "q":
            letra = input(self.menu)
            match letra:
                case "d": # depositar
                    self.comando_depositar()
                case "s": # sacar
                    self.comando_sacar()
                case "h": # histórico
                    self.comando_historico()
                case _:
                    print("Opção inválida, tente novamente.")
        return


    def _cliente_cadastrado(self, cpf:int) -> PessoaFisica:
        for cliente in self._clientes:
            if cliente._cpf == cpf:
                return cliente
        return False

    def comando_depositar(self):
        pass

    def comando_sacar(self):
        pass

    def comando_historico(self):
        pass

    def comando_criar_usuario():
        pass


    def main_loop(self):
        while True:

            opcao = input(self.menu)

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limites_saques=LIMITE_SAQUES)

            elif opcao == "e":
                ver_extrato(saldo, extrato=extrato)

            elif opcao == "u":
                cpf:str = input("Digite o CPF: ")
                cpf:int = cpf_str_p_int(cpf)
                if cpf:
                    if cpf_cadastrado(cpf):
                        print("CPF já cadastrado.")
                    else:
                        usuarios = criar_usuario(cpf, usuarios)
                else:
                    print('CPF inválido')

            elif opcao == "c":
                cpf:str = input("Digite o CPF: ")
                cpf:int = cpf_str_p_int(cpf)
                if cpf:
                    if cpf_cadastrado(cpf):
                        contas = criar_conta_corrente(cpf,contas)
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




def ver_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return





def criar_conta_corrente(cpf:int, contas=contas):
    # O programa deve armazenar contas em uma lista, 
    # uma conta é composta por: agência, número da conta e usuário.
    # O número da conta é sequencial, iniciando em 1.
    # O número da agência é fixo: "0001". 
    # O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
    AGENCIA = "0001"
    numero_conta = contas[-1]["numero_conta"] + 1
    contas.append({"agencia":AGENCIA, 
                   "numero_conta":numero_conta,
                   "usuario":cpf})
    return contas


def listar_usuarios():
    for usuario in usuarios:
        print(usuario)
    return



def main():
    cliente_teste = PessoaFisica(cpf="11235813",
                                nome="Teste",
                                data_nascimento="01/01/1900",
                                endereco="logradouro, 123 - bairro - cidade/UF")
    cliente_teste.adicionar_conta(ContaCorrente.nova_conta(cliente_teste, 1))
    clientes = [cliente_teste]
    sistema_banco = SistemaBanco(clientes=clientes)
    while True:
        sistema_banco.ir_para_tela_inicial()




main()