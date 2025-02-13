class Depositar:  # Cria a classe Depositar
    def __init__(self, saldo, historico):  # Inicializa a classe com saldo e histórico
        self.saldo = saldo  # Armazena o saldo da conta
        self.historico = historico  # Armazena o histórico de transações

    def deposito(self):  # Método de depósito
        while True:  # Loop infinito até um depósito válido ser realizado
            try:  # Tratamento de erro para garantir que o valor inserido seja válido
                deposito = float(input("Quanto você deseja depositar em sua conta? "))  # Solicita o valor do depósito como float

                if deposito <= 0:  # Verifica se o valor do depósito é menor ou igual a zero
                    print("O valor do depósito deve ser maior que zero.")  # Informa o erro ao usuário
                    continue  # Retorna ao início do loop para tentar novamente

                self.saldo += deposito  # Atualiza o saldo com o valor do depósito
                self.historico.append(f"Depósito + R$ {deposito:.2f}")  # Adiciona o depósito ao histórico
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")  # Confirma o depósito para o usuário
                print(f"Saldo Atual: R$ {self.saldo:.2f}")  # Exibe o saldo atualizado
                return self.saldo  # Retorna o saldo atualizado para ser usado

            except ValueError:  # Captura erro de valor (quando o input não for um número válido)
                print("Digite um número válido.")  # Informa o erro ao usuário
