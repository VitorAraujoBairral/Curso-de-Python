soma = 0
q = 0
while True:
    n1 = int(input("Digite um valor (999 para parar)"))
    if n1 != 999:
        soma = soma + n1
        q += 1
    else:
        break
print(f'Foram digitados {q} números. \nA soma dos números é {soma}')
