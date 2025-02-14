from Deposito import Depositar
from Sacar import Sacar
from Extrato_total import extrato
from historico_global import historico
from services.cadastro import cadastrar_cliente, cadastrar_conta


class Banco:
    def __init__(self, saldo=0.0):
        self.saldo = saldo
        self.historico = historico
        self.depositar = Depositar(self.saldo, self.historico)
        self.sacar = Sacar(self.saldo, self.historico)
        self.clientes = {}
        self.contas = {}

    def cadastrar_cliente(self):
        cadastrar_cliente(self.clientes)

    def cadastrar_conta(self):
        cadastrar_conta(self.contas, self.clientes)

    def login(self):
        cpf = input("Digite seu CPF para fazer login: ")
        if cpf not in self.clientes:
            print("Erro: Cliente não encontrado! Você precisa se cadastrar primeiro.")
            return None
        else:
            print(f"Login realizado com sucesso para o cliente {self.clientes[cpf].nome}.")
            return cpf

    def extrato(self):
        extrato(self.historico, self.saldo)

    def depositar_fundo(self):
        self.saldo = self.depositar.deposito()
        self.historico = self.depositar.historico
        self.sacar.saldo = self.saldo

    def sacar_fundo(self):
        self.saldo = self.sacar.saque()
        self.historico = self.sacar.historico
        self.depositar.saldo = self.saldo
