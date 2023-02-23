pessoa = dict()
cadastros = list()
while True:
    pessoa["Nome"] = input("Digite o nome: ")
    pessoa["Idade"] = int(input("Digite a idade: "))
    pessoa["Sexo"] = input("Digite o sexo [M/F]").upper()
    cadastros.append(pessoa.copy())
    if input("Quer continuar? [S/N]") in "Nn":
        break 
print(f"O grupo tem {len(cadastros)} pessoas")
mulheres = list()
soma = media = 0
acimamedia = list()
for p in cadastros:
    soma += p["Idade"]
    if p["Sexo"] == "F":
        mulheres.append(p["Nome"])
media = soma/len(cadastros)
for p in cadastros:
    if p["Idade"] > media:
        acimamedia.append(p.copy())
print(f"A média de idade do grupo é {media}")
print(f"As mulheres do grupo são {mulheres[:]}")
print(f"Lista de pessoas acima da média de idade:\n")
for p in acimamedia:
    print(f"{p}\n")
print("<<ENCERRADO>>")



