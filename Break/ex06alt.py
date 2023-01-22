saque = int(input('Qual valor você deseja sacar? R$ '))
resul1 = saque // 50
resto1 = saque % 50
resul2 = resto1 // 20
resto2 = resto1 % 20
resul3 = resto2 // 10
resto3 = resto2 % 10
resul4 = resto3 // 1
print(f'Total de {resul1} cedulas de R$ 50.00')
print(f'Total de {resul2} cedulas de R$ 20.00')
print(f'Total de {resul3} cedulas de R$ 10.00')
print(f'Total de {resul4} cedulas de R$ 1.00')