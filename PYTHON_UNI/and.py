'''
print("*** Sistema de validação de crédito***")

nome = input("Nome do cliente:")
sal = float(input("Salário Bruto: R$"))
cpf = input("Possui alguma restrição no CPF? <S/N>")

if sal > 1100 and cpf.upper() == 'N':
    print("O cliente", nome, "teve o crédito aprovado.")
else:
    print("O cliente", nome, "teve o crédito reprovado.")
'''
from datetime import date

nasc = int(input("Insira o ano de nascimento:"))
sexo = input("Insira seu sexo:<M/F>")

idade = date.today().year - nasc

if sexo.upper() == 'M' and nasc >= 18:
    print("Serviço militar obrigatório.")
else:
    print("Isento do Serviço Militar")
