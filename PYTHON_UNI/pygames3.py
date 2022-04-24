nome = "hero"
vida = 10
vivo = True

def main():
    print("Olá aventureiro, oque deseja?")
    print("")
    print("missões:")
    print("1 - Caçar goblins.")
    print("2 - Comprar armas.")
    print("3 - Resgatar inocentes.")
    print("")

    resposta = input("Eu quero:")

    if resposta == "1":
        print("Há goblins na colina de Dreiskoll.")

    elif resposta == "2":
        print("Há um ferreiro no fim da rua.")


    elif resposta == "3":
        print("Civis desapareceram na floresta de Kantro.")

    else:
        print("Não posso te ajudar.")
main()