lista = list()
for i in range(0 , 5):
    lista.append(int(input("Digite um valor: ")))
maior = max(lista)
menor = min(lista)
posmaior = ""
posmenor = ""
for c, v in enumerate(lista):
    if v == maior:
        posmaior += f" {c}"
    elif v == menor: 
        posmenor += f" {c}"
print(f"O maior valor é {maior} e está nas posições {posmaior}")
print(f"O menor valor é {menor} e está nas posições {posmenor}")


