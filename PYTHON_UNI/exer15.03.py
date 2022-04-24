''''
num = int(input("Insira um número:"))

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Nulo")
'''
'''
disc = int(input("Insira um número:"))

if disc == 0:
    print("Aprovado")
elif disc <= 5:
    print("Recuperação")
else:
    print("Reprovado")
'''
'''
nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota:"))

media = (nota1 + nota2) / 2

print("Sua média é:", round(media, 2))

if media >= 7:
    print("Aprovado")
else:
    nota3 = float(input("Insira sua terceira nota:"))

    media2 = (nota1 + nota2 + nota3 * 2) / 4
    print("Sua nova média é:", round(media2, 2))

    if media2 >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
 '''
pergunta1 = print("(1) Oque é na imagem?")
resposta1 = input("Cabide," "Menino," "Gato," "Portão")

pontos = 0

if resposta1.upper() == "MENINO":
    pontos += 3
    print("Resposta certa")
    print("Pontuação", pontos)

else:
    if resposta1.upper() == "CABIDE":
        print("Resposta errada")

        if resposta1.upper() == "PORTÃO":
            print("Resposta errada")




pergunta2 = print("(2) Oque é na imagem?")
resposta2 = input("Bola," "Carro," "Mesa," "Prato")



