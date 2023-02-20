import datetime
trabalhador = dict()
trabalhador["Nome"] = input("Digite o nome do empregado: ")
trabalhador["Ano de Nascimento"] = int(input("Digite o ano de nascimento: "))
trabalhador["CLT"] = int(input("Digite a carteira de trabalho do empregado. 0 se não houver: "))
trabalhador["Idade"] = datetime.datetime.now().year - trabalhador["Ano de Nascimento"]
if trabalhador["CLT"] != 0:
    trabalhador["Ano de contratação"] = int(input("Insira o ano de contratação: "))
    trabalhador["Salário"] = float(input("Insira o salário: R$"))
    trabalhador["Idade de aposentadoria"] = trabalhador["Idade"] + ((trabalhador["Ano de contratação"] + 35) - datetime.datetime.now().year)
    
print("-="*30)
for k, v in trabalhador.items():
    print(f"{k} tem o valor {v}")
