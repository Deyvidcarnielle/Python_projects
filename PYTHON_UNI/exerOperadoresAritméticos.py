'''1
n = float(input("Digite um número:"))
dobro = n * 2
print("o dobro de", n,"é", dobro)
'''

'''2
print("Antecessor e sucessor")
n = input("Digite um número:")
antecessor = int(n) - 1
sucessor = int(n) + 1
print("O antecessor de", n, "é", antecessor, "e o sucessor é", sucessor)
'''

'''3
polegadas = input("Insira quantas polegadas de chuva são:")
milimetros = float(polegadas) * 25.4
print("Essa quantidade em milímetros é", milimetros,"ml")
'''

'''4
num1 = input("Insira um número:")
num2 = input("Insira outro número:")
soma = int(num1) + int(num2)
media = soma /2
dif = int(num1) - int(num2)
metade = dif /2
print("A média aritmética desses dois números é =", media)
print("E a metade da diferença deles é =", metade)
'''

'''5
nota1 = float(input("Insira sua primeira nota:"))
nota2 = float(input("Insira sua segunda nota"))
nota3 = float(input("Insira sua terceira nota"))
media = (nota1 + nota2 + nota3)/3
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
print("Sua média é:", round(media, 2))
'''

'''6
sbruto = float(input("Insira seu salário:"))
desc = sbruto * 0.92
print("Seu salário líquido é:", desc)
'''

'''7
A = int(input("Insira o valor de A:"))
B = int(input("Insira o valor de B:"))
C = int(input("Insira o valor de C:"))
delta = B**2-4*A*C
print("Seu delta é", delta)
'''

'''8
far = input("Insira uma temperatura em fahrenheit:")
sub = float(far) - 32
cel = sub / 1.8
print("Essa temperatura em celsius é igual a:", cel, "°C")
'''

'''9
conc = float(input("Quantos m³ de concreto será feito:"))
areia = conc * 0.6
pedra = conc * 0.6
cimento = conc * 4.8
print("Para produzir", conc, "m³ de concreto, será necessário", areia, "m³ de areia,", pedra, "m³ de pedra e", cimento, "sacos de cimento")'''

'''10
compri = input("Insira o comprimento em metros de uma calçada:")
larg = input("Insira a largura em metros de uma calçada:")
alt = input("Insira a altura em centímetros de uma calçada:")
altm = float(alt) / 100
m3 = altm * float(compri) * float(larg)
areia = m3 * 0.6
pedra = m3 * 0.6
cimento = m3 * 4.8
print("A quantidade de areia a ser utilizada é:", areia)
print("A quantidade de pedra a ser utilizada é:", pedra)
print("A quantidade de sacos de cimento a ser utilizada é:", cimento)'''

'''11
comp = input("Informe quantos metros de comprimento tem o piso:")
larg = input("Informe quantos metros de largura tem o piso:")
meq = float(comp) * float(larg)
print("Será necessário", meq, "m² para revestir o quarto"'''

'''12
compri = input("Insira o comprimento do cômodo:")
larg = input("Insira a largura do cômodo:")
compricm = input("Insira o comprimento do piso:")
largcm = input("Insira a largura do piso:")
quarto = float(compri) * float(larg)
piso = float(compricm) * float(largcm)
tot = quarto/piso * 10000
print("A quantidade necessária de pisos para revestir o quarto é:", tot)'''

'''13
compri = input("Insira o comprimento do piso:")
larg = input("Insira a largura do piso:")
rodape = input("Insira a metragem linear do rodapé em cm:")
piso = float(compri) * float(larg)
altrodape = float(rodape) * 10
tot = piso//altrodape
print("A quantidade de pisos necessários para preencher o rodapé é:", tot)'''

'''14'''

'''15
mas = input("Insira a quantidade de alunos do sexo masculino:")
fem = input("Insira a quantidade de alunos do sexo feminino:")
apro = input("Insira a quantidade de alunos aprovados:")
total = int(mas) + int(fem)
femp = int(fem)*100 / int(total)
masp = int(mas)*100 / int(total)
aprop = int(apro)*100 / int(total)
print("O total de alunos são:", total,"alunos")
print("A porcentagem de alunos do sexo feminino é:", femp, "%")
print("A porcentagem de alunos do sexo masculino é:", masp, "%")
print("A porcentagem de alunos aprovados é:", aprop, "%")'''

'''16
game = input("Informe a quantidade de mini-games vendidos:")
cal = input("Informe a quantidade de calculadoras vendidas:")
can = input("Informe a quantidade de canetas vendidas:")
fatgame = int(game) * 6.95
fatcal = int(cal) * 3.5
fatcan = int(can) * 1.2
fattotal = fatgame + fatcal + fatcan
print("O faturamento da venda de mini-games é:", fatgame)
print("O faturamento da venda de calculadoras é:", fatcal)
print("O faturamento da venda de canetas é:", fatcan)
print("E o faturamento total de todos os produtos foi:", fattotal)'''

'''17
vit = input("Insira a quantidade de vitórias:")
der = input("Insira a quantidade de derrotas:")
emp = input("Insira a quantidade de empates:")
pontvit = int(vit) * 3
pontemp = int(emp) * 1
pont = pontvit + pontemp
total = int(vit) + int(der) + int(emp)
print("A quantidade total de jogos é:", total)
print("A quantidade de pontos ganhos é:", pont)
print("A quantidade total de pontos disputados foi:", total*3)'''