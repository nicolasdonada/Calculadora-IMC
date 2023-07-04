from tkinter import *

class CalculadoraIMC:
    def __init__(self):


        self.janela = Tk()
        self.janela.title("Calculadora de IMC")
        self.janela.geometry("500x275")
        self.janela.config(bg="#333333")
        self.janela.resizable(width=False, height=False)

        self.interface()

        self.janela.mainloop()
    
    def interface(self):

        self.label1 = Label(self.janela, width=20, height=2, text="Insira sua altura(M):", bg="white", font="Arial 10")
        self.label1.place(x=20, y=20)

        self.entry1 = Entry(self.janela, width=10)
        self.entry1.pack(anchor="center", pady=26)
    # ----------------------------------------

        self.label2 = Label(self.janela, width=20, height=2, text="Insira seu peso(Kg):", bg="white", font="Arial 10")
        self.label2.place(x=20, y=80)

        self.entry2 = Entry(self.janela, width=10)
        self.entry2.pack(anchor="center", pady=18)
    # ----------------------------------------

        self.frame1 = Frame(self.janela, width=180, height=200, bg="#3396F5")
        self.frame1.place(x=300, y=20)

        self.labelframe1 = Label(self.janela, height=2, anchor="center", text="Seu IMC:", fg="black", bg="#3396F5", font="Arial 20")
        self.labelframe1.place(x=330, y=20)

        self.labelframe2 = Label(self.janela, height=1, anchor="center", text="00.00", fg="black", bg="#3396F5", font="digital 40")
        self.labelframe2.place(x=322, y=90)
    # ----------------------------------------

        self.botao1 = Button(self.janela, width=20, height=2, text="Calcular", relief="flat", command=self.calcular)
        self.botao1.place(x=20, y=181)

        self.label3 = Label(self.janela, width=22, height=2, text="Classificação:", fg="white", bg="#333333")
        self.label3.place(x=20, y=140)

    def calcular(self):
        peso = float(self.entry2.get())
        altura = float(self.entry1.get())
        imc = f"{peso / (altura * altura):.2f}"
        imc1 = peso / (altura * altura)

        self.labelframe2["text"] = str(imc)

        if imc1 <= 18.4:
            self.label3["text"] = "Classifição: Magreza"
        
        if imc1 >= 18.5 and imc1 <= 24.9:
            self.label3["text"] = "Classifição: Normal"

        if imc1 >= 25 and imc1 <= 29.9:
            self.label3["text"] = "Classifição: Sobrepeso"
        
        if imc1 >= 30 and imc1 <= 34.9:
            self.label3["text"] = "Classifição: Obesidade grau I"
        
        if imc1 >= 35 and imc1 <= 39.9:
            self.label3["text"] = "Classifição: Obesidade grau II"

        if imc1 > 40:
            self.label3["text"] = "Classifição: Obesidade grau III"
        

Cal = CalculadoraIMC()