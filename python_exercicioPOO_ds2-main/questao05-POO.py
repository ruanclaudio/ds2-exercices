class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

# Exemplo de uso da classe ContaCorrente
conta = ContaCorrente(4245, "Carlos Perereira da Silva")
print(f"Número da conta: {conta.numero_conta}")
print(f"Nome do correntista: {conta.nome_correntista}")
print(f"Saldo: {conta.saldo}")

conta.alterarNome("Carlos Perereira da Silva Costa")
print(f"Novo nome do correntista: {conta.nome_correntista}")

conta.deposito(800)
print(f"Saldo após depósito: {conta.saldo}")

conta.saque(350)
print(f"Saldo após saque: {conta.saldo}")

conta.saque(600)