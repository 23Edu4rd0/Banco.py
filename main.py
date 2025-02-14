from Banco import Banco

banco = Banco()

MENU = """
    [c] Cadastrar Cliente
    [l] Trocar de Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

print("Bem-vindo ao banco Dudu")


usuario_logado = None

while not usuario_logado:
    print("\nPor favor, faça login ou se cadastre.")
    escolha_inicial = input("[l] Login ou [c] Cadastrar Cliente: ").lower()

    if escolha_inicial == "l":
        usuario_logado = banco.login()
    elif escolha_inicial == "c":
        banco.cadastrar_cliente()
    else:
        print("Opção inválida. Tente novamente.")


while usuario_logado:
    escolha = input(MENU).lower()


    if escolha == "c":
        banco.cadastrar_cliente()
    elif escolha == "l":
        banco.login()
    elif escolha == "d":
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
