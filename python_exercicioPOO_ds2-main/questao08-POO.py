class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(f"Conteúdo do bucho do macaco {self.nome}:")
        for alimento in self.bucho:
            print(alimento)

    def digerir(self):
        self.bucho = []

# Exemplo de uso da classe Macaco
macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")

macaco2.comer("Coco")
macaco2.comer("Abacaxi")
macaco2.comer("Melancia")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

# Macaco canibal
macaco1.comer(macaco2)
macaco1.verBucho()