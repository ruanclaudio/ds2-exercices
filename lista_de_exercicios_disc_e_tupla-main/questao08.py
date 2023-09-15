# 8) Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
# Escreva um programa que leia todos os tempos em segundos e os guarde
# em um dicionário, onde a chave é o nome do corredor. Ao final diga de
# quem foi a melhor volta da prova e em que volta; e ainda a classificação
# final em ordem (1o o campeão). O campeão é o que tem a menor média
# de tempos.

runners = ['runner 1', 'runner 2']
totalTurns = 2

times = {}

for runner in runners:
    runnerTimes = []
    
    for turn in range(1, totalTurns + 1):
        secTime = int(input(f"Digite o tempo em segundos da volta {turn} para o corredor: {runner} \n"))
        runnerTimes.append(secTime)
        
    times[runner] = runnerTimes

bestTurn = float('inf') #inf representa infinito, ou seja, o valor inicial será muito grande, o que torna capaz de comparar as voltas entre os corredores
bestTurnRunner = ''
bestTurnNumber = 0

for runner, runnerTimes in times.items(): #O laço pega uma key, value do corredor e seu tempo em cada volta
    for turn, secTime in enumerate(runnerTimes):
        if secTime < bestTurn:
            bestTurn = secTime
            bestTurnRunner = runner
            bestTurnNumber = totalTurns + 1
            
average = {}

for runner, runnerTimes in times.items():
    average[runner] = sum(runnerTimes) / len(runnerTimes)
    
classification = sorted(average, key=average.get)

print(f"A melhor volta da prova foi do corredor {bestTurnRunner} na volta {bestTurnNumber}.")
print("Classificação final:")
for position, runner in enumerate(classification, 1):
    print(f'{position}º lugar: {runner}')
    
