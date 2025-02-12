
def deposito(saldo_total, historico):
    while True:
        deposito_feito = input("Quanto você deseja depositar em sua conta? ")
        if deposito_feito.isdigit():
            deposito_feito = float(deposito_feito)
            saldo_total += deposito_feito
            historico.append(f"Deposito + R$ {deposito_feito}")
            print(f"Deposito de {deposito_feito:.2f} realizado com sucesso!")
            print(f"Saldo Atual: {saldo_total:.2f}")
            return saldo_total
        else:
            print("Digite um numero valido")
            continue


def saque(saldo_saque, historico, limite_utilizado, limite_diario):
    while limite_utilizado < limite_diario:
        fazer_saque = input("Quanto você deseja sacar da sua conta? ")
        if fazer_saque.isdigit():
            fazer_saque = float(fazer_saque)

            if fazer_saque > saldo_saque:
                print("Saldo indisponivel,favor realizar deposito")
                break
            else:
                saldo_saque -= fazer_saque
                limite_utilizado += 1
                historico.append(f"Saque - R$ {fazer_saque}")
                print(f"Saque de {fazer_saque:.2f} realizado com sucesso!")
                print(f"Saldo atual: {saldo_saque:.2f}")
                print(f"Saques restantes hoje: {limite_diario - limite_utilizado}")

            continuar = input("Deseja sacar novamente? (s/n)").lower()
            if continuar != "s":
                break

        else:
            print("Valor invalido, digite um numero valido")
    if limite_utilizado == 3:
        print("Você utilizou todos os saldos disponiveis por hoje. Volte amanha!")
    return saldo_saque


def extrato(historico, saldo):
    print("\n=== EXTRATO ===")
    if not historico:
        print("Nenhuma movimentação registrada.")
    else:
        for transicao in historico:
            print(transicao)
        print(f"Saldo Atual: R${saldo}")
        print("================\n")

Saldo = 0
Historico = []
saques_realizados = 0
limite_saques_diario = 3

MENU = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

print("Bem vindo ao banco Dudu")
while True:
    escolha = input(MENU).lower()
    if escolha == "d":
        Saldo = deposito(Saldo, Historico)
        continue
    elif escolha == "s":
        Saldo = saque(Saldo, Historico, saques_realizados, limite_saques_diario)
    elif escolha == "e":
        extrato(Historico, Saldo)
    elif escolha == "q":
        print("Até Logo!")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")









