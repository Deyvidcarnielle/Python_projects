soma = 0
n = 1
while n >= 0:
    n = float(input("Insira um número:"))
    if n >= 0:
        soma += n
    print("A soma dos números é:", soma)

'''soma = 0
nota = float(input("Insira a nota:"))
qtd = 0
while nota >= 0 and nota <= 10:
    soma += nota
    qtd = qtd + 1
    nota = float(input("Insira a nota:"))

if qtd == 0:
    print("A média das notas é:", round(soma/qtd, 2))'''

'''qtdf = 0
qtdm = 0
sexo = input("Digite o sexo <M/F>:")

while sexo.upper() == "F" or sexo.upper() == "M":
    if sexo.upper() == "F":
        qtdf += 1
    elif sexo.upper() == "M":
        qtdm += 1

    sexo = input("Digite o sexo <M/F>:")

total = qtdf + qtdm
print("O total de pessoas é", total)

msg = "Pessoas do sexo {0}: {1}%"
print(msg.format("feminino", round(qtdf * 100/total, 2)))
print(msg.format("masculino", round(qtdm * 100/total, 2)))'''

'''soma = 0
msg = "Digite o preço do produto{0} : R$"

for i in range(1, 11):
    preco = float(input(msg.format(i)))

    while preco <= 0:
        print("PREÇO INVÁLIDO!!!")
        preco = float(input(msg.format(i)))

    soma += preco

print("A soma dos preços é R$", round(soma, 2))'''

'''soma = 0
msg = "Digite a nota do aluno{0} :"

for i in range(1, 11):
    nota = float(input(msg.format(i)))

    while nota < 0 or nota >10:
        print("NOTA INVÁLIDA!!!")
        nota = float(input(msg.format(i)))

    soma += nota

print("A média da turma é", round(soma/i, 2))'''



