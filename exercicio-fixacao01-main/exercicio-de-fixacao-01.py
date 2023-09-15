"""01 - Ler uma lista de 5 números inteiros e mostre cada número
juntamente com a sua posição na lista:"""

lista_int = [0, 15, 25, 50, 75]
print(lista_int)

for i in range(0, 5):
    print(f'{lista_int[i]} posição {i}')
    
######################################################################################################################################################################################

"""02 - Ler uma lista de 10 números reais e mostre-os na ordem
inversa:"""

lista_reais = [1.5, 2.55, 3.555, 4.6, 5.65, 6.655, 7.7, 8.75, 9.755, 10.8]

for i in range(-1, -11, -1):
    print(f'{lista_reais[i]} posição {i}')
    
######################################################################################################################################################################################

"""03 - Ler uma lista com 4 notas, em seguida o programa deve exibir
as notas e a média:"""

lista_notas = [6.0, 5.8, 7.9, 8.8]

soma_notas = 0
for nota in lista_notas:
    soma_notas += nota

media_notas = (soma_notas / 4)
print(f'NOTAS: {lista_notas}')
print(f'MÉDIA = {round(media_notas, 2)}')

######################################################################################################################################################################################

#04 - Ler um vetor com 20 idades e exibir a maior e menor:

idades = list(range(18, 78, 3))

print(f'A idade máxima é {max(idades)}')
print(f'A idade miníma é {min(idades)}')

######################################################################################################################################################################################

"""05 - Utilizando o del, remova todos os elementos da lista criada
anteriormente até a lista ficar vazia."""

idades = list(range(18, 80, 3))
print(idades)
for i in range(len(idades)):
    idades.pop(0)
    print(idades)
    
######################################################################################################################################################################################   

#06 - Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!

lista_de_compras = ['Arroz', 'Feijão', 'Farinha', 'Açucar', 'Bananas', 'Laranjas', 'Leite', 'Queijo', 'Frango', 'Carne bovina', 'Detergente para louças', 'Sabão em pó', 'Papel higiênico', 'Sorvete de chocolate', 'Sorvete de baunilha']
print(lista_de_compras)

######################################################################################################################################################################################    

#07 - Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.

lista_de_compras.remove('Detergente para louças')
lista_de_compras.remove('Sabão em pó')
print(lista_de_compras)

######################################################################################################################################################################################

#08 - Agora «vá à sorveteria» e se empanturre e sorvete e tire o sorvete da lista.

lista_de_compras.remove('Sorvete de chocolate')
lista_de_compras.remove('Sorvete de baunilha')
print(lista_de_compras)

######################################################################################################################################################################################

#09 - Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o resto de uma divisão.Por exemplo: 3 % 2 = 1 e 4 % 2 = 0

def par_impar(num):
    if num % 2 == 0:
        print("O número digitado é par!")
    else:
        print("O número digitado é ímpar!")
        
num = int(input("Informe um número para determinar se este, é par ou ímpar: "))
par_impar(num)

######################################################################################################################################################################################

#10 - Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado duas palavras,retorne True caso sejam.

def palavra_inverso(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    for i in range(len(palavra1)):
        if palavra1[i] != palavra2[-i-1]:
            return False
    return True

palavra1 = input("Digite a primeira palavra aleatória: ")
palavra2 = input("Digite a segunda palavra para verificar se ela é o inverso da primeira: ")
print(palavra_inverso(palavra1, palavra2))


######################################################################################################################################################################################

#11 - Escreva uma função que imprime todos os números primos entre 1 e 50 

def num_primos():
    for num in range(1, 51):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

num_primos()
