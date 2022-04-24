'''nomes = []

nomes.append("José")
nomes.append("Maria")
nomes.append("Danilo")
nomes.append("Rafael")
nomes.append("Marcos")

print(nomes)

print("***POSIÇÃO POR POSIÇÃO***")

print("Posição 0:", nomes[0])
print("Posição 1:", nomes[1])
print("Posição 2:", nomes[2])
print("Posição 3:", nomes[3])
print("Posição 4:", nomes[4])


numeros = []

numeros.append(int(input("Digite um número:")))
numeros.append(int(input("Digite um número:")))
numeros.append(int(input("Digite um número:")))
numeros.append(int(input("Digite um número:")))
numeros.append(int(input("Digite um número:")))

print("Posição 0:", numeros[0])
print("Posição 1:", numeros[1])
print("Posição 2:", numeros[2])
print("Posição 3:", numeros[3])
print("Posição 4:", numeros[4])'''

numeros = []
msg1 = "Digite o {0}° número:"
msg2 = "Posição {0} = {1}"

for i in range(5):
    numeros.append(int(input(msg1.format(i+1))))
    
for i in range(5):
    print(msg2.format(i, numeros[i]))

'''
numeros = []

for i in range(10):
    numeros.append(int(input("Digite um número:")))

for i in range(9, -1, -1):
    print(numeros[i])


nomes = []

nomes.append("José")
nomes.append("Maria")
nomes.append("Danilo")
nomes.append("Rafael")
print(nomes)

nomes.insert(2, "Gerson")
print(nomes)

nomes.remove("Danilo")
print(nomes)

nomes.pop(2)
print(nomes)

nomes.append("Gabriel")
nomes.append("Igor")
nomes.append("Luis")
print(nomes)

print("Atualmente, a lista tem", nomes.count("Maria"), "elementos")
print("Atualmente, a lista tem", len(nomes), "elementos")
print("O Gabriel esta na posição", nomes.index("Gabriel"))

nomes.reverse()
print(nomes)

nomes.sort()  #ordem alfabética
print(nomes)

nomes.clear()
print(nomes)'''
