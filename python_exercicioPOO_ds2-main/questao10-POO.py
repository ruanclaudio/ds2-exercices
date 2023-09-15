class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Valor a ser pago: R$ {valor_pagar:.2f}")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade


# Exemplo de uso da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 4.5, 1000)

bomba.abastecerPorValor(100)  # Abastece R$100
bomba.abastecerPorLitro(20)  # Abastece 20 litros
bomba.alterarValor(5.94)  # Altera o valor do litro para R$5.94
bomba.alterarCombustivel("Etanol")  # Altera o tipo do combustível para Etanol
bomba.alterarQuantidadeCombustivel(1500)  # Altera a quantidade de combustível para 1500 litros