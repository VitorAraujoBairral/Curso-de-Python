boletim = list()
while True:
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    mean = (n1 + n2)/2
    boletim.append([nome, n1, n2, mean])
    if input("Deseja continuar? [S/N]: ").upper().strip() != "S":
        break
print("-="*20)
print("No. NOME" + " "*20 + "MÉDIA")
for i, aluno in enumerate(boletim):
    print(f'{i+1}   {aluno[0]}' + "."*(25-len(aluno[0])) + f"{aluno[3]}")
while True:
    index = int(input("Deseja mostrar as notas de qual aluno? (Digite 0 para não mostrar nenhuma)"))
    if index == 0:
        print("FINALIZANDO... \n<<<VOLTE SEMPRE>>>")
        break
    print(f"As notas de {boletim[index-1][0]} são {boletim[index-1][1]} e {boletim[index-1][2]}")
