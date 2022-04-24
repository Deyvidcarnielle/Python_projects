import tkinter
import tkinter as tk


class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PenseBem")
        self.root.geometry("400x150")
        self.buttonA = tk.Button(self.root,
                                 text="Cabide",
                                 bg="red",
                                 fg="black").place(x=20, y=40)

        self.buttonB = tk.Button(self.root,
                                text="Menino",
                                bg="yellow",
                                fg="black").place(x=90, y=40)

        self.buttonC = tk.Button(self.root,
                                 text="Gato",
                                 bg="blue",
                                 fg="black").place(x=165, y=40)

        self.buttonD = tk.Button(self.root,
                                 text="Portão",
                                 bg="green",
                                 fg="black").place(x=220, y=40)

        self.texto = tk.Label(self.root, text='Cabide')
        self.texto.place(x=20, y=10)

        self.texto = tk.Label(self.root, text='Menino')
        self.texto.place(x=90, y=10)

        self.texto = tk.Label(self.root, text='Gato')
        self.texto.place(x=165, y=10)

        self.texto = tk.Label(self.root, text='Portão')
        self.texto.place(x=220, y=10)




        self.root.mainloop()

app=Test()


