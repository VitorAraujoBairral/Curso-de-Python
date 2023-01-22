#lê a expressão e alimenta uma tupla com ela
text = input("Insira sua expressão: ")
#testa os parênteses
abre = []
for parentese in text:
    if parentese == "(":
        abre.append(parentese)
    elif parentese == ")" and len(abre) == 0:
        break
    elif parentese == ")" and len(abre) > 0:
        abre.pop()

#dá o resultado
print("Expressão Válida!" if len(abre) == 0 else "Expressão inválida!")