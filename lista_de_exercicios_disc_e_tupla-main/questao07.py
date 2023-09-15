# 7) Escreva um programa que lê duas notas de vários alunos e armazena tais
# notas em um dicionário, onde a chave é o nome do aluno. A entrada de
# dados deve terminar quando for lida uma string vazia como nome.
# Escreva uma função que retorna a média do aluno, dado seu nome.

def calculate_average(std_name, std_grades):
    if std_name in std_grades:
        grades = std_grades[std_name]
        average = sum(grades) / len(grades)
        return average
    else:
        return None

std_grades = {}

while True:
    nome = input("Digite o nome do aluno: ")
    print("OBS.: Deixe em branco para sair")
    if nome == "":
        break
    
    grade1 = float(input("Digite a primeira nota do aluno: "))
    grade2 = float(input("Digite a segunda nota do aluno: "))
    
    std_grades[nome] = [grade1, grade2]

search_name = input("Digite o nome do aluno para calcular a média: ")
std_average = calculate_average(search_name, std_grades)

if std_average is not None:
    print("A média do aluno", search_name, "é:", std_average)
    
else:
    print("Aluno não encontrado.")