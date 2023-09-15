class Ball:
    
    def __init__(self, color, circumference, material):
        self.color = color
        self.circumference = circumference
        self.material = material

    def tradeColor(self):
        self.color = input('Digite a cor da bola de basquete:')
    
    def showColor(self):
        print(f'A cor da sua bola de basquete é: {self.color}')
    
basketball = Ball('branco', 74.9, 'couro')

basketball.tradeColor()
basketball.showColor()
     