
monstros = ["monstro","Rei","Rei","monstro"]

def atacar():
    print("atacar monstro")

def defender():
    print("defender o rei")

for n in monstros :
    if n == "monstro":
        atacar()
    elif n == "Rei":
        defender()
