class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


# Função para exibir o centro de um retângulo
def exibirCentro(retangulo):
    centro = retangulo.encontrarCentro()
    print("Centro do retângulo:")
    centro.imprimir()


# Função para alterar os valores do retângulo
def alterarRetangulo(retangulo):
    print("Digite os novos valores do retângulo:")
    x = float(input("Coordenada x do vértice inferior esquerdo: "))
    y = float(input("Coordenada y do vértice inferior esquerdo: "))
    largura = float(input("Largura do retângulo: "))
    altura = float(input("Altura do retângulo: "))

    ponto_inicial = Ponto(x, y)
    retangulo.ponto_inicial = ponto_inicial
    retangulo.largura = largura
    retangulo.altura = altura


# Criação dos objetos Retângulo
retangulo1 = Retangulo(Ponto(0, 0), 4, 3)
retangulo2 = Retangulo(Ponto(1, 1), 5, 2)

# Menu interativo
opcao = 0
while opcao != 3:
    print("\nMenu:")
    print("1. Alterar valores do retângulo")
    print("2. Exibir centro do retângulo")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        retangulo_escolhido = int(input("Digite o número do retângulo (1 ou 2): "))
        if retangulo_escolhido == 1:
            alterarRetangulo(retangulo1)
        elif retangulo_escolhido == 2:
            alterarRetangulo(retangulo2)
        else:
            print("Opção inválida.")

    elif opcao == 2:
        retangulo_escolhido = int(input("Digite o número do retângulo (1 ou 2): "))
        if retangulo_escolhido == 1:
            exibirCentro(retangulo1)
        elif retangulo_escolhido == 2:
            exibirCentro(retangulo2)
        else:
            print("Opção inválida.")

    elif opcao == 3:
        print("Saindo...")
    else:
        print("Opção inválida.")