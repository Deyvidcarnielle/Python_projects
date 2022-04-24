nome = input("insira seu nome:")
print(nome[0])
print(nome[0:5])
print(nome[2:4])

qtd = len(nome)
print(qtd)

print("A quantidade de caracteres é", qtd, "a primeira letra é", nome[0], "e a últim letra é", nome[qtd-1])

print(nome.replace('a', '@'))

print(nome.lower())
print(nome.upper())