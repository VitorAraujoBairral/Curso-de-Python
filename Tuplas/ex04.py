tupla = int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: "))
print(f"O número nove apareceu {tupla.count(9)} vezes")
if tupla.count(3) > 0:
    print(f"O número 3 apareceu na posição {tupla.index(3) + 1}")
else:
    print("O número 3 não apareceu")
print("Os números pares foram: ")
for n in tupla:
    if n % 2 == 0:
        print(n)
