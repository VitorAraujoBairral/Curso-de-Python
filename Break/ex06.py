valor = int(input("Quanto você deseja sacar?"))
notas1 = notas10 = notas20 = notas50 = 0
while True:
    if valor >= 50:
        valor -= 50
        notas50 += 1
    elif valor >= 20:
        valor -= 20
        notas20 += 1
    elif valor >= 10:
        valor -= 10 
        notas10 += 1
    elif valor >= 1:
        notas1 += 1
        valor -= 1
    else:
        break
print(f"Total das notas de 50: {notas50} \nTotal das notas de 20: {notas20}\nTotal das notas de 10 {notas10}\nTotal das notas de 1 {notas1}")