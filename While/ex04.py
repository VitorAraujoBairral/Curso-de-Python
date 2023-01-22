num = fator = int(input("Digite um número:"))
while fator != 1:
    fator -= 1
    num *= fator
    print(fator)
print(num)