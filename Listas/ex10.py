matriz = list()
coluna = list()
for i in range(0, 3):
    for j in range(0, 3):
        coluna.append(int(input(f"Digite um número para {i}, {j}")))
    matriz.append(coluna[:])
    coluna.clear()
print("-="*20)
for row in matriz:
    print(f"[ {row[0]} ][ {row[1]} ][ {row[2]} ]")
print("-="*20)
pares = terceiracoluna = 0
for i in matriz:
    for index, j in enumerate(i):
        if j % 2 == 0:
            pares += j
        if index == 2:
            terceiracoluna += j
        
print(f"A soma dos valores pares é {pares} \nA soma dos valores da terceira coluna é {terceiracoluna} \nO maior valor da segunda linha é {max(matriz[1])}")