import random

from Extrato_total import extrato
from historico_global import historico
from models.cliente import Cliente
from models.conta import Conta
from datetime import datetime


class Banco:
    def __init__(self):
        self.historico = historico
        self.clientes = {}
        self.contas = {}
        self.dataAtual = datetime.now().strftime('%d/%m/%Y %H:%M')

    def cadastrar_cliente(self):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu email: ")

        if cpf in self.clientes:
            print("Erro: CPF já cadastrado!")
            return

        self.clientes[cpf] = Cliente(nome, cpf, email)
        numero_conta = str(random.randint(1000,9999))
        self.contas[numero_conta] = Conta(cpf, numero_conta)

        print(f"Cliente {nome} cadastrado com sucesso!")
        print(f"Conta criada com sucesso! Seu número de conta é {numero_conta}.\nQuarde esse numero, ele sera importante para que você possa fazer login\n")

    def login(self):
        cpf = input("Digite seu CPF para fazer login: ")

        if cpf not in self.clientes:
            print("Erro: Cliente não encontrado! Você precisa se cadastrar primeiro.")
            return None, None

        contas_usuario = [num for num, conta in self.contas.items() if conta.cpf == cpf]

        if not contas_usuario:
            print("Erro: Nenhuma conta associada a este CPF!")
            return None, None

        print(f"Login realizado com sucesso para o cliente {self.clientes[cpf].nome}.")
        numero_conta = input("Digite o número da sua conta: ")

        if numero_conta not in self.contas or self.contas[numero_conta].cpf != cpf:
            print("Erro: Conta não encontrada!")
            return None, None

        return cpf, numero_conta

    def extrato(self, numero_conta):
        if numero_conta in self.contas:
            extrato(self.historico, self.contas[numero_conta].saldo)
        else:
            print("Erro: Conta não encontrada!")

    def depositar_fundo(self, numero_conta):
        if numero_conta in self.contas:
            valor = float(input("Digite o valor do depósito: "))
            self.contas[numero_conta].saldo += valor
            self.historico.append(f"{self.dataAtual} - Depósito de R$ {valor:.2f} na conta {numero_conta}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: Conta não encontrada!")

    def sacar_fundo(self, numero_conta):
        if numero_conta in self.contas:
            valor = float(input("Digite o valor do saque: "))
            if valor > self.contas[numero_conta].saldo:
                print("Erro: Saldo insuficiente!")
            else:
                self.contas[numero_conta].saldo -= valor
                self.historico.append(f"{self.dataAtual} - Saque de R$ {valor:.2f} da conta {numero_conta}")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Erro: Conta não encontrada!")

    def cadastrar_conta(self):
        pass
