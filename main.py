from Deposito import Depositar
from Sacar import Sacar
from Extrato_total import extrato
from historico_global import historico

class Banco:
    def __init__(self, saldo=0.0):
        self.saldo = saldo
        self.historico = historico
        self.depositar = Depositar(self.saldo, self.historico)
        self.sacar = Sacar(self.saldo, self.historico)

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


banco = Banco()

MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

print("Bem-vindo ao banco Dudu")

while True:
    escolha = input(MENU).lower()
    if escolha == "d":
        banco.depositar_fundo()
    elif escolha == "s":
        banco.sacar_fundo()
    elif escolha == "e":
        banco.extrato()
    elif escolha == "q":
        print("Até Logo!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
