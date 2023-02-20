from random import randint
num = int(input("Quantos jogos você quer que eu gere?"))
palpite = list()
lista = list()
for i in range(0, num):
    for i in range(0, 6):
        n = randint(0, 60)
        while n in palpite:
            n = randint(0, 60)
        palpite.append(n)
    lista.append(palpite[:])
    palpite.clear()

for i, jogo in enumerate(lista):
    jogo.sort()
    print(f"Jogo {i}: {jogo}")