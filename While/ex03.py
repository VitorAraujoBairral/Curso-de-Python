while True:
    n1 = float(input("Digite um Número:"))
    n2 = float(input("Digite um Número:"))
    opcao = int(input("Digite um número para escolher o que fazer com os dois valores: \n [1] Para somar \n [2] para subtrair \n [3] para multiplicar \n [4] Para dividir \n [5] Para sair"))
    if opcao == 1:
        print("Resultado da soma de {} e {}: {}".format(n1, n2, n1+n2))
    elif opcao == 2:
        print("Resultado da subtração de {} e {}: {}".format(n1, n2, n1-n2))
    elif opcao == 3:
        print("Resultado da multiplicação de {} e {}: {}".format(n1, n2, n1 * n2))
    elif opcao == 4:
        print("Resultado da divisão de {} e {}: {}".format(n1, n2, n1 / n2))
    elif opcao == 5:
        break
