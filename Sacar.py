class Sacar:
    def __init__(self, saldo, historico):
        self.saldo = saldo
        self.limiteUsado = 0
        self.limiteDiario = 3
        self.historico = historico

    def saque(self):
        while self.limiteUsado < self.limiteDiario:
            try:
                fazer_saque = float(input("Quanto você deseja sacar da sua conta? "))

                if fazer_saque > self.saldo:
                    print("Saldo insuficiente, favor realizar depósito.")
                    break
                else:
                    self.saldo -= fazer_saque  # Atualiza o saldo após o saque
                    self.limiteUsado += 1
                    self.historico.append(f"Saque - R$ {fazer_saque:.2f}")
                    print(f"Saque de R$ {fazer_saque:.2f} realizado com sucesso!")
                    print(f"Saldo Atual: R$ {self.saldo:.2f}")
                    print(f"Saques restantes hoje: {self.limiteDiario - self.limiteUsado}")

                continuar = input("Deseja sacar novamente? (s/n)").lower()
                if continuar != "s":
                    break

            except ValueError:
                print("Valor inválido! Digite um número válido.")

        if self.limiteUsado == 3:
            print("Você utilizou todos os saques disponíveis por hoje. Volte amanhã!")

        return self.saldo  # Retorna o saldo atualizado
