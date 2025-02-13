
def extrato(historico, saldo): #funcao extrato que recebe historico  e saldo
    print("\n=== EXTRATO ===")
    if not historico: # se historico vazio
        print("Nenhuma movimentação registrada.")
    else:
        for transicao in historico: #para item em historico
            print(transicao)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("================\n")
