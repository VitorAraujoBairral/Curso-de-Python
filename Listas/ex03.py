lista = list()
lista.append(int(input("Insira um número: ")))
print("Adicionado ao final da lista")
i = 1
while i <= 5:
    n = int(input("Insira um número: "))
    if n > max(lista):
        lista.append(n)
        print("Valor adicionado ao final da lista.")
    else:
        for num in lista:
            if n < num:
                lista.insert(lista.index(num), n)
                break
        print(f"Valor adicionado na posição {lista.index(n)} da lista")  
    i += 1 
print("-="*20 + f"\n Os valores adicionados foram {lista}")
