from datetime import date

class Depositar:
    def __init__(self, saldo, historico,):
        self.saldo = saldo
        self.historico = historico
        self.dataAtual = date.today()

    def deposito(self):
        while True:
            try:
                deposito = float(input("Quanto você deseja depositar em sua conta? "))

                if deposito <= 0:
                    print("O valor do depósito deve ser maior que zero.")
                    continue

                self.saldo += deposito
                self.historico.append(f"Horario: {self.dataAtual} Depósito + R$ {deposito:.2f}")
                print(f"Depósito de R$ {deposito:.2f} - realizado com sucesso!")
                print(f"Saldo Atual: R$ {self.saldo:.2f}")
                return self.saldo

            except ValueError:
                print("Digite um número válido.")
