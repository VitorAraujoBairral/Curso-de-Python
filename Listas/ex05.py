lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    if input("Quer continuar? s/n: ") == "n":
        break
pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"Todos os números: {lista}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")