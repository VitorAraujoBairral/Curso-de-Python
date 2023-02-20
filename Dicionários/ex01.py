aluno = dict()
aluno["Nome"] = input("Nome")
aluno["Média"] = float(input("Média de " + f"{aluno['Nome']}"))
aluno["Situação"] = "Aprovado" if aluno["Média"] >= 7 else aluno["Média"] < 7; aluno["Situação"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k} é igual a {v}")