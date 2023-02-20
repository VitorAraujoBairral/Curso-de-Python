matriz = list()
coluna = list()
for i in range(0, 3):
    for j in range(0, 3):
        coluna.append(int(input(f"Digite um número para {i}, {j}")))
    matriz.append(coluna[:])
    coluna.clear()
for row in matriz:
    print(f"[ {row[0]} ][ {row[1]} ][ {row[2]} ]")
