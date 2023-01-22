termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA:"))
i = 0

print(termo)
while i < 9:
    termo += razao
    print(termo)
    i += 1