from models.cliente import Cliente
from models.conta import Conta
import random


def cadastrar_cliente(clientes):
    """Função para cadastrar um novo cliente."""
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    if cpf in clientes:
        print("Erro: Cliente já cadastrado!")
        return

    email = input("Digite o e-mail do cliente: ")
    novo_cliente = Cliente(nome, cpf, email)
    clientes[cpf] = novo_cliente
    print(f"Cliente {nome} cadastrado com sucesso!")
    numero_conta = str(random.randint(1000, 9999))  # Número aleatório entre 1000 e 9999
    print(f"Número da conta gerada: {numero_conta} Guarde esse numero, ele sera importante!")

def cadastrar_conta(contas, clientes):
    """Função para cadastrar uma nova conta vinculada a um cliente."""
    cpf = input("Digite o CPF do cliente: ")

    if cpf not in clientes:
        print("Erro: Cliente não encontrado. Cadastre o cliente primeiro!")
        return

    numero_conta = input("Digite o número da conta: ")

    if numero_conta in contas:
        print("Erro: Esta conta já existe!")
        return

    saldo_inicial = float(input("Digite o saldo inicial: "))
    nova_conta = Conta(numero_conta, clientes[cpf], saldo_inicial)
    contas[numero_conta] = nova_conta
    print(f"Conta {numero_conta} criada com sucesso para {clientes[cpf].nome}!")
