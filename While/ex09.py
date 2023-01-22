soma = entrada = maior = menor = int(input("Insira o primeiro valor: "))
nvalores = 1

while input("Deseja continuar? [s/n]: ") == "s":
    entrada = int(input("Insira o novo valor: "))
    soma += entrada
    if(entrada > maior):
        maior = entrada
    if(entrada < menor):
        menor = entrada
    nvalores += 1

media = (soma / nvalores)
print("Média dos valores: {} \nMaior valor: {} \nMenor valor: {}".format(media, maior, menor))