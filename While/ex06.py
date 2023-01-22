termo = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA:"))
i = 0
ntermos = 10
while ntermos > 0:
    termo += razao
    print(termo)
    ntermos -= 1
    if ntermos == 0:
        ntermos = int(input("Deseja mostrar mais quantos termos?"))