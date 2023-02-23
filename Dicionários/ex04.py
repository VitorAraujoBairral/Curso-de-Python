estatisticas = dict()
estatisticas["Nome"] = input("Insira o nome do Jogador: ")
estatisticas["Partidas"] = int(input("Insira o número de partidas jogadas pelo jogador"))
gols = list()
for i in range(0, estatisticas["Partidas"]):
    gols.append(int(input(f"Digite a quantidade de gols na partida {i}")))
total = sum(gols[:])
estatisticas["Gols"] = gols[:]
estatisticas["Total"] = total
print("-="*30)
print(estatisticas)
print("-="*30)
for k, v in estatisticas.items():
    print(f"O campo {k} tem valor {v}")
print("-="*30)
print(f"O jogador {estatisticas['Nome']} jogou {estatisticas['Partidas']} partidas.")
for i, gol in enumerate(estatisticas["Gols"]):
    print(f"     => Na partida {i}, fez {gol} gols")
print(f"No total, foram {estatisticas['Total']} gols")
