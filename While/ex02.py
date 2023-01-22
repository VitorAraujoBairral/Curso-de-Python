from random import randint

num = randint(1, 10)
p = int(input("Insira seu palpite em um número de 1 a 10:"))
tentativas = 0

while p != num:
    p = int(input("Não foi nesse número em  que eu pensei, tente de novo:"))
    tentativas += 1

print("Parabéns, você acertou depois de tentar {} vezes!".format(tentativas))
