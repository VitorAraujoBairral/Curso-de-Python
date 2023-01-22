listagem = ("Lápis", 1.00, "Caderno", 10.00, "Tesoura", 15.00, "Borracha", 3.99)
print("_"*40)
print(" "*11+"LISTAGEM DE PREÇOS")
print("_"*40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        strpreco = f"R${listagem[i + 1]}"
        print(listagem[i] + "."*(40 - len(listagem[i]) - len(strpreco)) + strpreco)

