usuario = input("Digite o usuário de e-mail:")
servidor = input("Digite o servidor:")
dominio = input("Digite o domínio:")

email = "{0}@{1}.{2}"

print("O email é:", email.format(usuario, servidor, dominio))