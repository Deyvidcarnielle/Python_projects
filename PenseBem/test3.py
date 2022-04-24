print("*** PENSE BEM ***")

pontos = 0

pergunta1 = print("(1) Oque é a figura?")
escolha1 = input("Cabide  ,"  "Menino  ,"  "Gato  ,"  "Portão:")

if escolha1.upper() == "MENINO":
    print("Resposta certa")
    pontos += 3
    print("Pontuação", pontos)
else:
    print("Você errou, tente novamente")
    escolha1 = input("Cabide  ,"  "Menino  ,"  "Gato  ,"  "Portão:")
    if escolha1.upper() == "MENINO":
        print("Resposta certa")
        pontos += 2
        print("Pontuação", pontos)
    else:
        print("Você errou, tente novamente")
        escolha1 = input("Cabide  ,"  "Menino  ,"  "Gato  ,"  "Portão:")
        if escolha1.upper() == "MENINO":
            print("Resposta certa")
            pontos += 1
            print("Pontuação", pontos)
        else:
            print("Resposta errada")

print()

pergunta2 = print("(2) Oque é a figura?")
escolha2 = input("Bola  ,"  "Carro  ,"  "Mesa  ,"  "Prato:")

if escolha2.upper() == "BOLA":
    print("Resposta certa")
    pontos += 3
    print("Pontuação", pontos)
else:
    print("Você errou, tente novamente")
    escolha2 = input("Bola  ,"  "Carro  ,"  "Mesa  ,"  "Prato:")
    if escolha2.upper() == "BOLA":
        print("Resposta certa")
        pontos += 2
        print("Pontuação", pontos)
    else:
        print("Você errou, tente novamente")
        escolha2 = input("Bola  ,"  "Carro  ,"  "Mesa  ,"  "Prato:")
        if escolha2.upper() == "BOLA":
            print("Resposta certa")
            pontos += 1
            print("Pontuação", pontos)
        else:
            print("Resposta errada")
print()

pergunta3 = print("(3) Oque é a figura?")
escolha3 = input("Xícara  ,"  "Caixa  ,"  "Chapéu  ,"  "Bule:")

if escolha3.upper() == "XÍCARA":
    print("Resposta certa")
    pontos += 3
    print("Pontuação", pontos)
else:
    print("Você errou, tente novamente")
    escolha3 = input("Xícara  ,"  "Caixa  ,"  "Chapéu  ,"  "Bule:")
    if escolha3.upper() == "XÍCARA":
        print("Resposta certa")
        pontos += 2
        print("Pontuação", pontos)
    else:
        print("Você errou, tente novamente")
        escolha3 = input("Xícara  ,"  "Caixa  ,"  "Chapéu  ,"  "Bule:")
        if escolha3.upper() == "XÍCARA":
            print("Resposta certa")
            pontos += 1
            print("Pontuação", pontos)
        else:
            print("Resposta errada")