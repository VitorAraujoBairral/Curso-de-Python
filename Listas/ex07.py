cadastros = list()
pessoa = ["", 0]
while True:
    pessoa[0] = input("Nome:")
    pessoa[1] = float(input("Peso"))
    cadastros.append(pessoa[:])
    if input("Quer continuar?[S/N]").capitalize().strip() == "N":
        break
print("-="*20)
print(f"Ao todo, você cadastrou {len(cadastros)} pessoas.")
maiorpeso = list()
menorpeso = list()
maxpeso = 0
minpeso = cadastros[0][1]

for pessoas in cadastros:
    if pessoas[1] > maxpeso:
        maxpeso = pessoas[1]
    elif pessoas[1] < minpeso:
        minpeso = pessoas[1]

for pessoas in cadastros:
    if pessoas[1] == maxpeso:
        maiorpeso.append(pessoas[0])
    elif pessoas[1] == minpeso:
        menorpeso.append(pessoas[0])

print(f"O maior peso foi de {maxpeso}, peso de {maiorpeso}")
print(f"O menor peso foi de {minpeso}, peso de {menorpeso}")