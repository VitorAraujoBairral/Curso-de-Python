soma = entrada = nvalores = 0
while entrada != 999:
    entrada = int(input("digite o valor desejado: "))
    if entrada != 999:
        soma += entrada
        nvalores += 1
print("Número de valores: {} \nSoma dos valores: {}".format(nvalores, soma))