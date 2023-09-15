# 4) Crie um programa que cadastre informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário.

biggerP = {}
smallerP = {}
tempDictionary = {}

while True:
    name = input('Digite o nome: ')
    age = int(input('Digite a idade: '))
    CPF = input('Digite o CPF da pessoa: ')
    
    tempDictionary[name] = {'idade' : age, 'cpf' : CPF}
    
    for key, value in tempDictionary.items():
        tempAge = value['idade']
        tempCPF = value['cpf']
         
        if tempAge < 18:
            smallerP[name] = {'idade': tempAge, 'cpf': tempCPF}
        else:
            biggerP[name] = {'idade' : tempAge, 'cpf' : tempCPF}
    
    del tempDictionary[name]
            
    opt = int(input('Deseja adicionar mais dados há Agenda? \n 01) SIM | 02) NÃO\n'))
    if opt == 2:
        break
for key, value in biggerP.items():    
    print('Pessoas maiores que 18 anos: {} : {}'.format(key, value))
for key, value in smallerP.items():
    print('Pessoas menores que 18 anos: {} : {}'.format(key, value))
    