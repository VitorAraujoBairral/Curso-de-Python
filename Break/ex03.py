from random import randint
vitorias = 0
while True:
    escolha = input("Par ou ímpar? ").capitalize().strip()
    mao = int(input("Dê um número de 1 a 10"))
    com = randint(1, 10)
    soma = mao + com
    if soma % 2 == 0:
        print(f"Você digitou {mao} e eu {com}, o resultado é {soma}. {soma} é par")
        if escolha == "PAR":
            print("Você venceu! Vamos jogar de novo!")
        else:
            break
    else:
        print(f"Você digitou {mao} e eu {com}, o resultado é {soma}. {soma} é impar")
        if escolha == "IMPAR":
            print("Você venceu! Vamos jogar de novo!")
        else:
            break
print(f"Fim de jogo! Eu ganhei! Você me venceu {vitorias} vezes!")