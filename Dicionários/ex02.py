from random import randint
from time import sleep
from operator import itemgetter
valores = {"Jogador1": randint(1, 6), "Jogador2": randint(1, 6), "Jogador3": randint(1, 6), "Jogador4": randint(1,6)}
print("Valores sorteados:")
for k, v in valores.items():
    print(f"O {k} tirou {v}")
    sleep(0.5)
ranking = list()
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print("Ranking dos jogadores")
for place, j in enumerate(ranking):
    print(f"O {place+1}º colocado foi {j[0]} com {j[1]} pontos") 
    sleep(0.5)