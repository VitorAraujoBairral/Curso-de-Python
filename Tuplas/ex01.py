tupla = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
num = int(input("Digite um número entre 0 e 20: "))

while True:
    if num >= 0 and num <= 20:
        break
    else: 
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))

print(f"Você digitou o número {tupla[num]}")
