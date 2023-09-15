class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        humor = (self.fome + self.saude) / 2
        return humor

# Exemplo de uso da classe BichinhoVirtual
bichinho = BichinhoVirtual("Tamagotchi")
print(f"Nome: {bichinho.retornarNome()}")
print(f"Fome: {bichinho.retornarFome()}")
print(f"Saúde: {bichinho.retornarSaude()}")
print(f"Idade: {bichinho.retornarIdade()}")
print(f"Humor: {bichinho.retornarHumor()}")

bichinho.alterarNome("Bichinho Feliz")
bichinho.alterarFome(50)
bichinho.alterarSaude(80)
bichinho.alterarIdade(2)

print(f"Nome após alteração: {bichinho.retornarNome()}")
print(f"Fome após alteração: {bichinho.retornarFome()}")
print(f"Saúde após alteração: {bichinho.retornarSaude()}")
print(f"Idade após alteração: {bichinho.retornarIdade()}")
print(f"Humor após alteração: {bichinho.retornarHumor()}")