class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Exemplo de uso da classe Pessoa
pessoa = Pessoa("Ruan", 21, 80, 172)
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Peso: {pessoa.peso}")
print(f"Altura: {pessoa.altura}")

pessoa.envelhecer(2)
print(f"Idade após envelhecer: {pessoa.idade}")
print(f"Altura após envelhecer: {pessoa.altura}")

pessoa.engordar(5)
print(f"Peso após engordar: {pessoa.peso}")

pessoa.emagrecer(3)
print(f"Peso após emagrecer: {pessoa.peso}")

pessoa.crescer(1.5)
print(f"Altura após crescer: {pessoa.altura}")