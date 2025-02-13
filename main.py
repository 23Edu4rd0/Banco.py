from Banco import Banco

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
