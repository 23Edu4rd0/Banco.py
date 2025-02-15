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
        data_nascimento = input("Digite sua data de nascimento: ")

        if cpf in self.clientes:
            print("Erro: CPF já cadastrado!")
            return

        senha = input("Digite sua senha:")
        self.clientes[cpf] = Cliente(nome, cpf, data_nascimento)
        numero_conta = str(random.randint(1000, 9999))
        self.contas[senha] = Conta(cpf, senha)

        print(f"Cliente {nome} cadastrado com sucesso!")
        print(f"Conta criada com sucesso! Seu número de conta é {numero_conta}.")

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
        senha = input("Digite a sua senha: ")

        if senha not in self.contas or self.contas[senha].cpf != cpf:
            print("Erro: Conta não encontrada!")
            return None, None

        print(f"\nSeja bem-vindo {self.clientes[cpf].nome}!")

        return cpf, senha

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

    def transferir_fundo(self, numero_conta):
        cpf_transferencia = input("Digite o CPF da conta que deseja transferir: ")

        contas_destino = [num for num, conta in self.contas.items() if conta.cpf == cpf_transferencia]

        if not contas_destino:
            print("Erro: Nenhuma conta encontrada para esse CPF!")
            return

        if len(contas_destino) > 1:
            conta_destino = input("Digite o número da conta para transferência: ")
            if conta_destino not in contas_destino:
                print("Erro: Conta inválida!")
                return
        else:
            conta_destino = contas_destino[0]

        print(f"Conta de destino: {self.clientes[cpf_transferencia].nome}")
        try:
            saldo_transferencia = float(input("Digite o valor a ser transferido: R$"))
            if saldo_transferencia <= 0:
                print("Erro: O valor deve ser positivo!")
                return
        except ValueError:
            print("Erro: Valor inválido!")
            return

        if saldo_transferencia > self.contas[numero_conta].saldo:
            print("Erro: Saldo insuficiente!")
            return
        if numero_conta == conta_destino:
            print("Erro: Não é possivel transferir para a mesma conta!")
            return

        confirmacao = input(
            f"Confirma a transferência de R$ {saldo_transferencia:.2f} para a conta {self.clientes[cpf_transferencia].nome}? [s/n] ").lower()

        if confirmacao != "s":
            print("Tranferencia cancelada!")
            return

        self.contas[numero_conta].saldo -= saldo_transferencia
        self.contas[conta_destino].saldo += saldo_transferencia

        self.historico.append(
            f"{self.dataAtual} - Transferência de R$ {saldo_transferencia:.2f} para conta {self.clientes[cpf_transferencia].nome}")
        print(f"Transferência de R$ {saldo_transferencia:.2f} para a conta {conta_destino} realizada com sucesso!")
