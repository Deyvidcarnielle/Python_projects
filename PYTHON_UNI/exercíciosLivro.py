'''1
num1 = float(input("Insira um número:"))
num2 = float(input("Insira outro número:"))
sub = num1 - num2
print("A subtração desses dois números é:", round(sub, 2))'''

'''2
num1 = float(input("Insira o primeiro número:"))
num2 = float(input("Insira o segundo número:"))
num3 = float(input("Insira o terceiro número:"))
mult = num1 * num2 * num3
print("A multiplicação desses números é:", mult)'''

'''3
num1 = float(input("Insira o primeiro número:"))
num2 = float(input("insira o segundo número:"))
div = num1 / num2
print("A divisão desses números é:", round(div, 2))'''

'''4
nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota:"))
media = (nota1 * 2 + nota2 * 3) / 5
print("Sua média será:", round(media, 2))'''

'''5
preco = float(input("Insira o preço de um produto:"))
desc = preco * 0.9
print("O valor dele com 10% de desconto é:", desc)'''

'''6
sal_fixo = float(input("Insira seu salário fixo:"))
valor_venda = float(input("Insira o valor de suas vendas:"))
com = valor_venda * 0.04
sal = sal_fixo + com
print("A comissão é:", com)
print("O salário final é:", sal)'''

'''7
peso = float(input("Digite o peso:"))
peso15 = peso * 1.15
peso20 = peso * 0.8
print("Seu peso se engordar 15% do seu peso atual será:", round(peso15, 1))
print("Seu peso se emagrecer 20% do seu peso atual será:", round(peso20, 1))'''

'''8
kilo = float(input("Informe seu peso:"))
grama = kilo * 1000
print("Seu peso em gramas é:", round(grama, 2), "g")'''

'''9
basemaior = float(input("Insira o valor da base maior:"))
basemenor = float(input("Insira o valor da base menor:"))
altura = float(input("Insira o valor da altura:"))
A = (basemenor + basemaior) * altura / 2
print("A área do trapézio é:", A)'''

'''10
lado = float(input("Insira o valor do lado do quadrado:"))
A = lado**2
print("A área do quadrado é:", A)'''

'''11
diagomenor = float(input("Insira o valor da diagonal menor do losango:"))
diagomaior = float(input("Insira o valor da diagonal maior do losango:"))
A = (diagomaior * diagomenor) / 2
print("A área do losango é:", A)'''

'''12
salmin = float(input("Insira o valor de um salário mínimo:"))
sal = float(input("Insira o valor do seu salário:"))
salfinal = sal / salmin
print("Você ganha em torno de", round(salfinal, 2), "vezes o salário minímo")'''

'''13
print("**TABUADA**")
num = int(input("Insira um número:"))
print(num, "x 0=", num * 0)
print(num, "x 1=", num * 1)
print(num, "x 2=", num * 2)
print(num, "x 3=", num * 3)
print(num, "x 4=", num * 4)
print(num, "x 5=", num * 5)
print(num, "x 6=", num * 6)
print(num, "x 7=", num * 7)
print(num, "x 8=", num * 8)
print(num, "x 9=", num * 9)
print(num, "x 10=", num * 10)
'''

'''14
from datetime import date
anonasc = int(input("Insira seu ano de nascimento:"))
idade = date.today().year - anonasc
print("Sua idade em anos é:", idade)
print("Sua idade em meses é:", idade * 12)
print("Sua idade em dias é:", idade * 365)
print("Sua idade em semanas é:", idade * 52)
'''

'''15
sal = float(input("Insira seu salário:"))
conta1 = float(input("Insira o valor da primeira conta:"))
conta2 = float(input("Insira o valor da segunda conta:"))
multa1 = conta1 * 1.02
multa2 = conta2 * 1.02
print("Após pagas as multas restará", sal - multa1 - multa2, "do seu salário")'''

'''16'''

'''17
import math
raio = float(input("Insira o raio:"))
comprimento = raio * 2 * math.pi
area = (raio**2) * math.pi
volume = 3/4 * math.pi * (raio ** 3)
print("o comprimento é:", round(comprimento, 2))
print("a área é:", round(area, 2))
print("o volume é:", round(volume, 2))'''

'''18
celsius = float(input("Insira a temperatura em celsius:"))
F = 180*(celsius + 32)/100
print("A temperatura em Fahrenheit é:", F)'''

'''19
larg = float(input("Insira a largura do cômodo:"))
comp = float(input("Insira o comprimento do cômodo:"))
area = larg * comp
W = area * 18
print("deverá ser utilizado", W, "W de potência para iluminar o cômodo")'''

'''20
import math
ang = float(input("Insira o ângulo formado:"))
dist = float(input("Insira a distância:"))
cos = math.cos(math.radians(ang))
hip = dist * cos
print("O tamanho da escada é:", hip)'''

'''21
hora = float(input("Insira a quantidade de horas trabalhadas:"))
sal = float(input("Insira o valor do salário mínimo"))
horax = float(input("Insira a quantidade de horas extras"))
hora2 = hora * (sal / 8)
horax2 = horax * (sal / 4)
salbruto = hora2 + horax2
print("O salário bruto é:", salbruto)'''

'''22'''
N = int(input("Insira a quantidade de lados do polígono:"))
ND = N*(N - 3)/2
print("O número de diagonais desse polígono é", ND)


'''23
ang = float(input("Insira um dos ângulos de um triângulo:"))
ang2 = float(input("Insira o outro ângulo triângulo:"))
ang3 = 180 - (ang + ang2)
print("O terceiro ângulo é:", ang3)'''

'''24
din = float(input("Digite o valor de dinheiro:"))
print("Esse valor em dólar é:", din * 1.8)
print("Esse valor em marco alemão é:", din * 2)
print("Esse valor em libra esterlina é:", din * 3.57)'''

'''25
hora = float(input("Digite a hora:"))
min = float(input("Digite uns minutos:"))
print("A hora em minutos são:", hora * 60, "minutos")
print("O total de minutos são:", min + hora * 60, "minutos")
print("O total de segundos são:", 60*(min + hora * 60))'''