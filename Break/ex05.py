print("      LOJA SUPER BARATÃO         ")
nome = pMaisBarato = input("Informe o nome do produto: ")
total = preco = mPreco = float(input("Informe o preco do produto: "))
pcaros = 0
opcao = ""
if preco >= 1000:
    pcaros += 1

while True:
    opcao = input("Deseja continuar [S/N]?").capitalize().strip()
    if opcao == "S":
        nome = input("Informe o nome do produto: ")
        preco = float(input("Informe o preco do produto: "))
        total += preco
        if preco < mPreco:
            pMaisBarato = nome
            mPreco = preco
        if preco >= 1000:
            pcaros += 1
    elif opcao == "N":
        break

print(f"\nTotal gasto pela compra: R${total} \n{pcaros} produtos custam mais de R$1000,00 \n{pMaisBarato} é o produto mais barato.")
    
    
