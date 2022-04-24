'''
num = []
msg =

for i in range(1, 16):
    num.append(int(input("Digite um número:")))

    if num == 30:

        print("O Gabriel esta na posição", num.index("Gabriel"))

print("O 30 esta na posição", num.index("Gabriel"))

numeros = []
msg1 = "Digite o {0}° número:"
msg2 = "Posição {0} = {1}"

for i in range(15):
    numeros.append(int(input(msg1.format(i + 1))))

for i in range(15):
    print(msg2.format(i, numeros[i]))'''



'''
num = []
soma = 0
msg1 = "Digite o {0}° número:"
for i in range(5):
    num.append(int(input(msg1.format(i+1))))
    if num[i] >= 0:
        soma += num[i]

print("Os números digitados foram:", num[0], "+", num[1], "+", num[2], "+", num[3], "+", num[4], "=", soma)'''

'''
num = []
pos = []
pares = 0
for i in range(1, 6):
    num.append(int(input("Digite um número:")))
    if num[i] = 30:
        pares += 1

print(pares)'''



nota = 0

while nota > 0 and nota < 10:

   nota = input(float('Digite uma nota: '))
   print("A nota é :", nota)











