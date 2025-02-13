# Importa classes e funções de diferentes módulos
from Deposito import Depositar  
from Sacar import Sacar  
from Extrato_total import extrato  
from historico_global import historico  

class Banco:  # Define a classe Banco
    def __init__(self, saldo=0.0):  # Método construtor que inicializa a classe Banco
        self.saldo = saldo  # Define o saldo inicial da conta como um float
        self.historico = historico  # Atribui a variável 'historico' (provavelmente uma lista) 

        # Cria instâncias das classes Depositar e Sacar, passando o saldo e o histórico
        self.depositar = Depositar(self.saldo, self.historico)  
        self.sacar = Sacar(self.saldo, self.historico)  

    def extrato(self):  
        """Exibe o extrato da conta, chamando a função 'extrato' e passando o histórico e saldo."""
        extrato(self.historico, self.saldo)

    def depositar_fundo(self):  
        """Realiza um depósito, atualiza o saldo e o histórico, e sincroniza o saldo com o objeto 'sacar'."""
        # Chama o método de depósito e atualiza o saldo
        self.historico = self.depositar.historico  # Atualiza o histórico da conta
        self.sacar.saldo = self.saldo  # Garante que o saldo em 'sacar' seja atualizado

    def sacar_fundo(self):  
        """Realiza um saque, atualiza o saldo e o histórico, e sincroniza o saldo com o objeto 'depositar'."""
        self.saldo = self.sacar.saque()  # Chama o método de saque e atualiza o saldo
        self.historico = self.sacar.historico  # Atu self.saldo = self.depositar.deposito() aliza o histórico da conta
        self.depositar.saldo = self.saldo  # Garante que o saldo em 'depositar' seja atualizado
