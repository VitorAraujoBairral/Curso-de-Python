idade = pessoas = mulheres = homens = 0

while True:
    if input("Deseja cadastrar alguém [S/N]? ") == "N":
        break
    idade = int(input("Informe a idade da pessoa: "))
    if idade > 18:
        pessoas += 1 
    if input("Informe o sexo da pessoa [M/F]: ") == 'M':
        homens += 1    
    else:
        if idade < 20:
            mulheres += 1

print(f"{pessoas} pesssoas têm mais de 18 anos \n{homens} homens foram cadastrados \n{mulheres} mulheres Stêm menos de 20 anos")
