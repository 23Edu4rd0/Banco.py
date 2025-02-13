class Depositar: # cria a classe depositar
    def __init__(self, saldo, historico): #self recebe os valores de variaveis e transforma para o objeto entender que so eles serão usados
        self.saldo = saldo # self recebe o valor de saldo
        self.historico = historico #self recebe o valor de historico

    def deposito(self): # metodo deposito recebe as variaveis self
        while True: # Loop (obvio)
            try: #tratamento de erros
                deposito = float(input("Quanto você deseja depositar em sua conta? ")) #variavel local, definida como float

                if deposito <= 0: # não permitir que o usuario envie valores menores que 1
                    print("O valor do depósito deve ser maior que zero.")
                    continue # volta ao inicio do loop

                self.saldo += deposito # self recebe os valores de deposito
                self.historico.append(f"Depósito + R$ {deposito:.2f}") # adciona a lista historico a string
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!") # mostra ao usuario o deposito realizado e quando ele tem em conta
                print(f"Saldo Atual: R$ {self.saldo:.2f}") 
                return self.saldo #retorna o valor de saldo para ser usado

            except ValueError: # se houver erro de valor
                print("Digite um número válido.")
