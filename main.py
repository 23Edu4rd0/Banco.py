from Banco import Banco

banco = Banco()

MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [t] Transferir
    [l] Trocar de Usuario
    [q] Sair

Escolha:
"""

def login_ou_cadastrar():
    while True:
        escolha = input("\n[c] Cadastrar Cliente\n[l] Fazer Login\nEscolha: ").lower()

        if escolha == "c":
            banco.cadastrar_cliente()
            print("Cadastro realizado com sucesso. Por favor, faça login.")
            continue

        elif escolha == "l":
            resultado = banco.login()
            if resultado:
                return resultado
            else:
                print("Login falhou. Por favor, tente novamente.")
                continue
        else:
            print("Operação inválida. Por favor, escolha 'c' para cadastrar ou 'l' para login.")
            continue

print("Bem-vindo ao banco ConfetiBank")

cpf, numero_conta = login_ou_cadastrar()

print("O que você deseja fazer?")

while True:
    escolha = input(MENU).lower()

    if escolha == "d":
        banco.depositar_fundo(numero_conta)
    elif escolha == "s":
        banco.sacar_fundo(numero_conta)
    elif escolha == "e":
        banco.extrato(numero_conta)
    elif escolha == "t":
        banco.transferir_fundo(numero_conta)
    elif escolha == "l":
        cpf, numero_conta = login_ou_cadastrar()
    elif escolha == "q":
        print("Até Logo!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")