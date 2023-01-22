t0 = 0
t1 = 1
tr = 0
i = int(input("Insira o número de termos desejados:")) - 1
if i >= 0:
    print("1")
while i > 0:
    tr = t1 + t0
    print(tr)
    t0 = t1
    t1 = tr
    i -= 1