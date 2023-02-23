estatisticas = dict()
jogadores = list()
while True:
    estatisticas["Nome"] = input("Nome: ")
    estatisticas["Partidas"] = int(input("Partidas jogadas: "))
    gols = list()
    for i in range(0, estatisticas["Partidas"]):
        gols.append(int(input(f"Gols da partida {i}")))
    estatisticas["Gols"] = gols[:]
    estatisticas["Total de Gols"] = sum(gols)
    jogadores.append(estatisticas.copy())
    if input("Deseja continuar? [S/N]") in "Nn":
        break
print("-="*30)
print("cod ", end="")
for k in estatisticas.keys():
    print(f"{k:<15}", end="")
print()
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()   
while True:
    i = int(input("Mostrar dados de qual jogador? "))
    if i >= 0 and i < len(jogadores):
        print(f"Levantamento do jogador {jogadores[i]['Nome']}")
        for i, p in enumerate(jogadores[i]["Gols"]):
            print(f"Na partida {i} fez {p} gols")
    elif i == 999:
        break
    else:
        print(f"Erro! Não existe jogador com código {i}. Tente novamente.")