'''for i in range(1, 4):
    print("*** ALUNO", i, "***")
    n1 = float(input("Digite a nota 1:"))
    n2 = float(input("Digite a nota 2:"))
    n3 = float(input("Digite a nota 3:"))

    media = (n1 + n2 + n3/3)
    print("A média é:", round(media, 2))

    if media <= 6:
        print('Reprovado')
    else:
        print("Aprovado")'''

'''soma = 0
for i in range(10):
    n = int(input("Digite um número: "))
    soma += n
    print("A soma é:", soma)'''


'''soma = 0
for i in range(1, 6):
    print("Dados do cômodo", i)

    comp = float(input("Insira o comprimento do cômodo:"))
    larg = float(input("Insira a largura do cômodo:"))

    soma += comp * larg
    print("A area é:", round(comp * larg, 2))

print("A area total é:", round(soma, 2))'''


'''soma = 0
for i in range(1, 11):
    print("*** ALUNO", i, "***")
    n = float(input("Digite a sua nota :"))
    soma += n

print("A média da turma é:", round(soma / 10, 2))'''


'''maior = int(input("Digite um número:"))
for i in range(9):
    n = int(input("Digite um número: "))

    if n > maior:
        maior = n

print("O maior número digitado foi:", maior)'''

maior = 0
menor = 10
for i in range(10):
    n = int(input("Digite sua nota: "))

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print("A maior nota foi:", maior)
print("A menor nota foi:", menor)





