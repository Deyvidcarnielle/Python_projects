from datetime import date

ano = int(input("Insira teu ano de nascimento:"))

idade = date.today().year - ano

print("Hoje é", date.today())

print("Sua idade é:", idade)
if idade >= 18:
    print("Apto a ser eleitor.")

else:
    print("Inapto a ser eleitor.")
   