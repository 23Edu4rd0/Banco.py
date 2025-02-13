class Sacar: # crição da classe Sacar
    def __init__(self, saldo, historico):
        self.saldo = saldo
        self.limiteUsado = 0 #variavies de uso local
        self.limiteDiario = 3
        self.historico = historico

    def saque(self):
        while self.limiteUsado < self.limiteDiario: # loop que so permite ate o momento em que o limite dirario seja igual ao usado
            try: #tratamento de erros
                fazer_saque = float(input("Quanto você deseja sacar da sua conta? "))

                if fazer_saque > self.saldo: # não permite que o saque seja menor que o saldo
                    print("Saldo insuficiente, favor realizar depósito.")
                    break #quebra e volta pro loop principal
                else:
                    self.saldo -= fazer_saque #retira o valor de saque do saldo
                    self.limiteUsado += 1 # adciona 1 uso ao limite
                    self.historico.append(f"Saque - R$ {fazer_saque:.2f}") # adciona ao dicionario
                    print(f"Saque de R$ {fazer_saque:.2f} realizado com sucesso!") #mostra as informações ao usuario
                    print(f"Saldo Atual: R$ {self.saldo:.2f}")
                    print(f"Saques restantes hoje: {self.limiteDiario - self.limiteUsado}")

                continuar = input("Deseja sacar novamente? (s/n)").lower() #pergunta se o usuario deseja sacar novamente
                if continuar != "s":
                    break

            except ValueError:
                print("Valor inválido! Digite um número válido.")

        if self.limiteUsado == 3:
            print("Você utilizou todos os saques disponíveis por hoje. Volte amanhã!")

        return self.saldo #retorna saldo
