lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    if input("Quer continuar? s/n: ") == "n":
        break
lista.sort(reverse= True)
print(f"Você digitou {len(lista)} números, em ordem decrescente foram {lista}") 
print("5 faz parte da lista." if 5 in lista else "5 não faz parte da lista.")