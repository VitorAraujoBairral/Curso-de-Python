lista = list()
while True:
    entrada = int(input("Digite um valor:"))
    if entrada in lista:
        print("Valor duplicado, não vou adicionar.")
    else:
        lista.append(entrada)
    if input("Deseja continuar? [s/n]").upper().strip() == "N":
        break
lista.sort()
print(f"Você digitou os valores {lista}")