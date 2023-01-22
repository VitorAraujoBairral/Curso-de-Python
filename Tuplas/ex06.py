palavras = "baguete", "insano", "acochambrado", "esculhambacao", "constituicao", "cosseno"
vogaisPalavra = ""
for i in palavras:
    for letra in i:
        if letra in "aeiou":
            vogaisPalavra += letra + " "
    print(f"A palavra {i} tem as vogais {vogaisPalavra}")
    vogaisPalavra = ""
 
