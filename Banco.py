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
