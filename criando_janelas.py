import tkinter as tk
from tkinter import Label

janela = tk.Tk()
janela.title("Calculadora de IMC") # Cria o título da janela

# Conteúdo da janela

# Label: onde Label (rótulo/etiqeta), e o grid vai posicionar na coluna e linha indicada 
Label(janela, text="    Digite os dados abaixo para saber seu IMC:    ", font=("Arial", 12)).grid(column=2, row=2) 

janela.mainloop()
