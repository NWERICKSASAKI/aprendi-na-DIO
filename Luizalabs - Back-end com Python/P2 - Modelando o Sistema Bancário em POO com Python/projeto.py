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
        conta._historico.adicionar_transacao(self)


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
        valor = transacao._valor
        if transacao.__class__ == Saque:
            conta._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif transacao.__class__ == Deposito:
            conta._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Tipo de transação inválida.")
            return
        transacao.registrar(conta)

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

    def _cliente_esta_cadastrado(self, cpf:int) -> PessoaFisica:
        for cliente in self._clientes:
            if cliente._cpf == cpf:
                return cliente
        return False

    def comando_criar_usuario(self, cpf:int,) -> PessoaFisica:
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

    def ir_para_tela_inicial(self) -> None:
        print("Bem-vindo!")
        cpf = input("Informe o seu CPF (somente números): ")
        cpf = self.cpf_so_numero(cpf)
        if cpf:
            usuario = self._cliente_esta_cadastrado(cpf)
            if not usuario:
                usuario = self.comando_criar_usuario(cpf)
            self.ir_para_tela_cliente(usuario)
        else:
            print("CPF inválido. Tente novamente.")

    def printar_contas(self, cliente) -> None:
        contas = cliente._contas
        if contas:
            for conta in contas:
                print(f"Agência: {conta._agencia} | Conta: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
        else:
            print("Nenhuma conta cadastrada.")

    def comando_acessar_conta(self, cliente:PessoaFisica) -> None:
        numero_conta = input("Informe o número da conta: ")
        if numero_conta.isnumeric():
            numero_conta = int(numero_conta)
            if numero_conta <= len(cliente._contas):
                self.ir_para_tela_conta(cliente._contas[numero_conta-1])
            else:
                print("Número da conta inválido.")
        else:
            print("Número da conta inválido.")

    def comando_criar_conta(self, cliente:Conta) -> None:
        nova_conta:Conta = ContaCorrente.nova_conta(cliente, len(cliente._contas)+1)
        cliente.adicionar_conta(nova_conta)
        print("\nConta criada com sucesso!")

    def ir_para_tela_cliente(self, cliente:PessoaFisica):
        menu = """
        Escolha uma opção:

        [a] Acessar conta
        [c] Criar conta
        [q] Sair

        => """
        menu = textwrap.dedent(menu)
        
        letra = ""
        print(f"Bem-vindo, {cliente._nome}!")
        while not letra == "q":
            self.printar_contas(cliente)
            letra = input(menu)
            match letra:
                case "a": self.comando_acessar_conta(cliente)
                case "c": self.comando_criar_conta(cliente)
                case _:   print("Opção inválida, tente novamente.")

    def comando_depositar(self, conta:Conta):
        valor = input("Informe o valor do depósito: ")
        if valor.isnumeric() and float(valor)>0:
            valor = float(valor)
            if conta.depositar(valor):
                conta.cliente.realizar_transacao(conta, Deposito(valor))
            else:
                print("Depósito não realizado.")
        else:
            print("Valor inválido.")

    def comando_sacar(self, conta:Conta):
        valor = input("Informe o valor do depósito: ")
        if valor.isnumeric() and float(valor)>0:
            valor = float(valor)
            if conta.sacar(valor):
                conta.cliente.realizar_transacao(conta, Saque(valor))
            else:
                print("Saque não realizado.")
        else:
            print("Valor inválido.")

    def comando_informar_saldo(self, conta:Conta):
        saldo = conta._saldo
        saques = conta.numero_saques if hasattr(conta, "numero_saques") else 0
        limite = conta._limite if hasattr(conta, "_limite") else 0
        limite_saques = conta._limite_saques if hasattr(conta, "_limite_saques") else 0
        print(f"Saldo: R$ {saldo:.2f}")
        if limite:
            print(f"Saque diário: {saques}/{limite_saques} | Limite por saque: R$ {limite:.2f}")

    def comando_historico(self, conta:Conta):
        print("Exibindo histórico de transações...")
        historico = conta._historico
        if historico._transacoes:
            for transacao in historico._transacoes:
                tipo = type(transacao).__name__
                valor = transacao._valor
                print(f"{tipo}: R$ {valor:.2f}")
        else:
            print("Nenhuma transação realizada.")
        
    def ir_para_tela_conta(self, conta:Conta):
        menu = f"""
        Acessando conta {conta._numero}...
        Escolha uma opção:

        [d] Depositar
        [s] Sacar
        [i] Saldo
        [h] Histórico
        [q] Voltar
        => """
        menu = textwrap.dedent(menu)

        letra = ""
        while not letra == "q":
            letra = input(self.menu)
            match letra:
                case "d": self.comando_depositar(conta)
                case "s": self.comando_sacar(conta)
                case "i": self.comando_informar_saldo(conta)
                case "h": self.comando_historico(conta)
                case _:   print("Opção inválida, tente novamente.")


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


if __name__ == "__main__":
    main()