palavra = input("Digite uma palavra:")

print("A primeira letra é:", palavra[0])
print("A segunda letra é:", palavra[1])

print("O trecho entre palavras é:", palavra[3:7])

qtd = len(palavra)

print("A palavra", palavra, "tem", qtd, "caracteres")

print("A última letra é:", palavra[qtd-1])

print("Sem espaço:---", palavra.strip(), "---")  #tira espaço SÓ antes e depois da palavra

print("Em letra minúscula:", palavra.lower())

print("Em letra maiúscula:", palavra.upper())

print("Trocando a por x:", palavra.replace("a", "x"))

print("Sem espaços entre palavras:", palavra.replace(" ", ""))

print("Texto dividido:", palavra.split("a"))
palavras = palavra.split(" ")
print("Primeira palavra:", palavras[0])
print("segunda palavra:", palavras[1])
print("terceira palavra:", palavras[2])