def calcularmedia():
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

def exibiropcoes():
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
        print("OPÇÃO INVÁLIDA!!!")
        exibiropcoes()

print("*** INÍCIO DO PROGRAMA ***")

exibiropcoes()

print("*** FIM DO PROGRAMA ***")