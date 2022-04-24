'''def calcularTriplo():
    n = int(input("Digite um número:"))
    msg = "O triplo de {0} é {1}"
    print(msg.format(n, n *3))

print("*** ÍNICIO DO PROGRAMA ***")

calcularTriplo()

print("*** FIM DO PROGRAMA ***")'''

'''def calcularQuadrado():
    n = int(input("Digite um número:"))
    msg = "O quadrado de {0} é {1}"
    print(msg.format(n, n **2))

print("*** ÍNICIO DO PROGRAMA ***")

for i in range(10):
calcularQuadrado()

print("*** FIM DO PROGRAMA ***")'''

'''def calcularmedia():
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número:"))
    print('A média é:', (n1 + n2) / 2)

def calculardiferenca():
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número:"))

    if n1 > n2:
        print('A diferença é:', n1 - n2)
    else:
        print('A diferença é:', n2 - n1)

def calcularproduto():
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número:"))
    print('O produto é:', n1*n2)

def calculardivisao():
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número:"))
    print('O produto é:', n1/n2)

print("As operações são:")
print("(1) Média Aritmética")
print("(2) Diferença do maior pelo menor")
print("(3) Produto")
print("(4) Divisão")

opcao = int(input("Digite a opção:"))

if opcao == 1:
    print("MÉDIA ARITMÉTICA")
    calcularmedia()
elif opcao == 2:
    print("DIFERENÇA")
    calculardiferenca()
elif opcao == 3:
    print("PRODUTO")
    calculardiferenca()
elif opcao == 4:
    print("DIVISÃO")
    calculardiferenca()
else:
    print("OPÇÃO INVÁLIDA!!!")'''

import math

raio = float(input("Digite o raio:"))
def calcularcomp(n1):

    print('O comprimento é:', round(2*math.pi*n1, 2))

def calculararea(n1):

    print("A área é:", round(math.pi*n1**2, 2))

def calcularvolume(n1):

    print('O volume é:', round(3/4*math.pi*n1**3, 2))

print("As operações são:")
print("(1) COMPRIMENTO")
print("(2) ÁREA")
print("(3) VOLUME")

opcao = int(input("Digite a opção:"))

if opcao == 1:
    print("COMPRIMENTO")
    calcularcomp(raio)
elif opcao == 2:
    print("ÁREA")
    calculararea(raio)
elif opcao == 3:
    print("VOLUME")
    calcularvolume(raio)
else:
    print("OPÇÃO INVÁLIDA!!!")

