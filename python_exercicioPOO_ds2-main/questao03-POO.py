class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def changeValues(self):
                self.base = float(input('Informe o valor da BASE do retângulo: '))
                self.height = float(input('Informe o valor da ALTURA do retângulo: '))
                
    def showValues(self):
        print(f'Base do retângulo: {self.base}')
        print(f'Altura do retângulo: {self.height}')
        
    def calculateRectangleArea(self):
        print(f'A área do Retângulo é de: {self.base * self.height}')
        
        
rectangleA = Rectangle(base= 0, height= 0)
rectangleA.changeValues()
rectangleA.showValues()
rectangleA.calculateRectangleArea()