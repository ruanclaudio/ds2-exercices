class Square:
    
    def __init__(self, sideValue):
        self.sideValue = sideValue
    
    def changeSideValue(self):
        self.sideValue = float(input('Digite o valor do lado do quadrado: '))
        
    def showsideValue(self):
        print(f'O valor do lado do Quadrado é: {self.sideValue}')
    
    def calculateArea(self):
        area = self.sideValue ** 2
        print(f'A área do quadrado é: {area}')


squareA = Square(sideValue=0)
squareA.changeSideValue()
squareA.showsideValue()
squareA.calculateArea()

        