from abc import ABC, abstractmethod
from datetime import date
import textwrap

class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:object, historico:object):
        self._saldo:float = saldo
        self._numero:int = numero
        self._agencia:str = agencia
        self._cliente:Cliente = cliente
        self._historico:Historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor:float) -> None:
        self._saldo = valor
    
    @classmethod
    def nova_conta(cls, cliente:object, numero:int):
        return cls(saldo=0.0, numero=numero, agencia="0001", cliente=cliente, historico=Historico())

    def sacar(self, valor:float) -> bool:
        excedeu_saldo = valor > self.saldo
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False
        elif valor > 0:
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

    def depositar(self, valor:float) -> bool:
        if valor > 0:
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente:object, agencia:str, saldo:float=0.0, numero:int=1, limite:float=500, limite_saques:int=3, historico:object=[]):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite:float = limite
        self._limite_saques:int = limite_saques
        self.numero_saques:int = 0

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

    def depositar(self, valor:float) -> bool:
        return super().depositar(valor)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta) -> None:
        conta._historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor:float=0.0):
        self._valor = valor

    def registrar(self, conta:Conta):
        conta._historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor:float=0.0):
        self._valor = valor

    def registrar(self, conta:Conta):
        conta._historico.adicionar_transacao(self)
        conta.saldo -= self._valor

class Historico:
    def __init__(self):
        self._transacoes:list = []

    def adicionar_transacao(self, transacao:Transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self) -> list:
        return self._transacoes

class Cliente:
    def __init__(self, endereco:str, contas:list=[]):
        self._endereco:str = endereco
        self._contas:list = contas

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        valor = transacao._valor
        if transacao.__class__ == Saque:
            conta.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif transacao.__class__ == Deposito:
            conta.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Tipo de transação inválida.")
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta:Conta) -> None:
        self._contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, cpf:str, nome:str, data_nascimento:date, endereco:str, contas:list=[]):
        super().__init__(endereco, contas)
        self._cpf:str = cpf
        self._nome:str = nome
        self._data_nascimento:date = data_nascimento


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
                                   endereco=endereco,
                                   contas=[])
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
        contas = cliente.contas
        if contas:
            for conta in contas:
                print(f"Agência: {conta._agencia} | Conta: {conta._numero} | Saldo: R$ {conta.saldo:.2f}")
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
        conta_criada = ContaCorrente.nova_conta(cliente, len(cliente._contas)+1)
        cliente.adicionar_conta(conta_criada)
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
                case "q": print("Saindo...")
                case _:   print("Opção inválida, tente novamente.")

    def comando_depositar(self, conta:Conta):
        valor = input("Informe o valor do depósito: ")
        if valor.isnumeric() and float(valor)>0:
            valor = float(valor)
            if conta.depositar(valor):
                conta._cliente.realizar_transacao(conta, Deposito(valor))
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
        saldo = conta.saldo
        saques = conta.numero_saques if hasattr(conta, "numero_saques") else 0
        limite = conta._limite if hasattr(conta, "_limite") else 0
        limite_saques = conta._limite_saques if hasattr(conta, "_limite_saques") else 0
        print(f"Saldo: R$ {saldo:.2f}")
        if limite:
            print(f"Saque diário: {saques}/{limite_saques} | Limite por saque: R$ {limite:.2f}")

    def comando_historico(self, conta:Conta):
        print("Exibindo histórico de transações...")
        historico = conta._historico
        if historico.transacoes:
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
            letra = input(menu)
            match letra:
                case "d": self.comando_depositar(conta)
                case "s": self.comando_sacar(conta)
                case "i": self.comando_informar_saldo(conta)
                case "h": self.comando_historico(conta)
                case _:   print("Opção inválida, tente novamente.")


def teste(clientes):
    cliente = clientes[0]
    conta = cliente._contas[0]
    valor_deposito = 1000.0
    conta.depositar(valor_deposito)



def main():
    clientes = []
    #clientes = criando_base_inicial()
    sistema_banco = SistemaBanco(clientes=clientes)
    #teste(clientes)
    while True:
        sistema_banco.ir_para_tela_inicial()

def criando_base_inicial():
    cliente_teste = PessoaFisica(cpf="123",
                                nome="Teste",
                                data_nascimento="01/01/1900",
                                endereco="logradouro, 123 - bairro - cidade/UF")
    nova_conta = ContaCorrente.nova_conta(cliente_teste, 1)
    cliente_teste.adicionar_conta(nova_conta)
    clientes = [cliente_teste]
    return clientes

if __name__ == "__main__":
    main()