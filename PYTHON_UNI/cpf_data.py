data = input("Digite sua data de nascimento, ex;20042002 :")
cpf = input("Digite seu cpf:")

print(data[0:2], "/", data[2:4], "/", data[4:8])  #método com espaços entre numero e barra

cpf2 = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]       #método sem espaços

print(cpf2)