# 3) Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave (cpf), nome, idade, telefone. O programa deve ler um número
# indeterminado de dados, criar a agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idadefone.

schedule = {}

while True:
    CPF = input('Digite o CPF da pessoa: ')
    name = input('Digite o nome: ')
    age = input('Digite a idade: ')
    celphone = input('Digite o telefone:')
    
    schedule[CPF] = f'{name} - {age} - {celphone}'    
    opt = int(input('Deseja adicionar mais dados há Agenda? \n 01) SIM | 02) NÃO\n'))
    if opt == 2:
        break
    
for  key, value in schedule.items():
    print('{} : {}'.format(key, value ))    
    