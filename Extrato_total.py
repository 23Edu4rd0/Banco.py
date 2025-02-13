
def extrato(historico, saldo):
    print("\n=== EXTRATO ===")
    if not historico:
        print("Nenhuma movimentação registrada.")
    else:
        for transicao in historico:
            print(transicao)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("================\n")
