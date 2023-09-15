# 5) Considere um sistema onde os dados são armazenados em dicionários.
# Nesse sistema existe um dicionario principal e o dicionário de backup.
# Cada vez que o dicionário principal atinge tamanho 5, ele imprime os
# dados na tela e apaga o seu conteúdo. Crie um programa que insira dados
# em um dicionário, realizando o backup a cada dado e excluindo os dados
# do dicionário principal quando ele atingir tamanho 5.

from time import sleep

principaldicCelp = {}
backupdicCelp = {}
limit = 2
delay = 1

while True:
    name = input('Digite o name da Pessoa para adicionar na agenda: ')
    celphone = input('Digite o número de celphone da respectiva pessoa: ')
    
    principaldicCelp[name] = celphone
        
    if len(principaldicCelp) >= limit:
        print(principaldicCelp)
        
        print('A sua agenda principal está cheia, um BackUp será iniciado e após isso os dados da Agenda principal irão ser excluidos.')
        sleep(delay)
        
        print('REALIZANDO BACKUP [...]')
        
        backupdicCelp.update(principaldicCelp)
        print('BACKUP REALIZADO')
        principaldicCelp.clear()
        print('Agenda de BackUp: {}'.format(backupdicCelp))
        
    
    opt = int(input('Deseja adicionar mais contatos a sua Agenda? \n 01) SIM | 02) NÃO\n'))
    if opt == 2:
        break

print('Encerrando o programa...')
 