class Sacar:  # Criação da classe Sacar
    def __init__(self, saldo, historico):
        self.saldo = saldo  # Saldo da conta
        self.limiteUsado = 0  # Variável que armazena o número de saques realizados
        self.limiteDiario = 3  # Limite diário de saques
        self.historico = historico  # Lista que armazena o histórico de saques

    def saque(self):
        while self.limiteUsado < self.limiteDiario:  # Loop que permite saques até o limite diário ser atingido
            try:  # Bloco para tratamento de erros
                fazer_saque = float(input("Quanto você deseja sacar da sua conta? "))  # Solicita o valor do saque

                if fazer_saque > self.saldo:  # Verifica se o valor do saque é maior que o saldo
                    print("Saldo insuficiente, favor realizar depósito.")
                    break  # Encerra o loop e retorna ao menu principal
                else:
                    self.saldo -= fazer_saque  # Subtrai o valor do saque do saldo
                    self.limiteUsado += 1  # Incrementa o contador de saques realizados
                    self.historico.append(f"Saque - R$ {fazer_saque:.2f}")  # Adiciona o saque ao histórico
                    print(f"Saque de R$ {fazer_saque:.2f} realizado com sucesso!")  # Exibe confirmação do saque
                    print(f"Saldo Atual: R$ {self.saldo:.2f}")  # Exibe saldo atual após o saque
                    print(f"Saques restantes hoje: {self.limiteDiario - self.limiteUsado}")  # Exibe quantidade de saques restantes

                continuar = input("Deseja sacar novamente? (s/n)").lower()  # Pergunta se o usuário deseja fazer outro saque
                if continuar != "s":  # Se a resposta não for 's', sai do loop
                    break

            except ValueError:
                print("Valor inválido! Digite um número válido.")  # Exibe erro caso o valor informado não seja numérico

        if self.limiteUsado == 3:  # Se o limite diário de saques for atingido
            print("Você utilizou todos os saques disponíveis por hoje. Volte amanhã!")

        return self.saldo  # Retorna o saldo atualizado
