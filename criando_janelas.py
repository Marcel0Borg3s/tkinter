import tkinter as tk
from tkinter import Label, Frame, Entry, Button
from imc_calc import calcular_imc


def calcular():
    try:
        peso = float(peso_kg.get())
        altura = float(altura_cm.get()) 
        idade_valor = int(idade.get())

        resultado = calcular_imc(peso, altura, idade_valor)
        resultado_label.config(text=resultado)

    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos.")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de IMC") # Cria o título da janela


# Conteúdo da janela

# Label: onde Label (rótulo/etiqeta), e o grid vai posicionar na coluna e linha indicada 
frame = Frame(janela, padx=10, pady=10)
frame.grid(column=0, row=0) 

# Pad x e y é para espaçar dentro da janela // colunmspan=2 é pq tem 2 colunas, para centralizar entre as 2
Label(frame, text="    Digite os dados abaixo para saber seu IMC:    ", font=("Arial", 12), pady=5).grid(column=1, row=0, columnspan=2) 
Label(frame, text="    Sempre utilize ponto '.' para calcular", font=("Arial", 10), pady=10).grid(column=1, row=1, columnspan=2) 

Label(frame, text="Qual é o seu peso? (kg) ").grid(column=1, sticky="w", row=4)
# Adicionando o input:
peso_kg = Entry(frame)
peso_kg.grid(column=2, row=4) 

Label(frame, text="Qual é o sua altura?").grid(column=1, sticky="w", row=5)
# Adicionando o input:
altura_cm = Entry(frame)
altura_cm.grid(column=2, row=5)

Label(frame, text="Qual é sua idade? ").grid(column=1, sticky="w", row=6)
# Adicionando o input:
idade = Entry(frame)
idade.grid(column=2, row=6)

# Botão para criar o calculo
Button(frame, text="Calcular", padx= 10, pady=5, command=calcular).grid(column=1, row=12, columnspan=2)

# Rótulo para exibir o resultado
resultado_label = Label(frame, text="", font=("Arial", 12), pady=12)
resultado_label.grid(column=1, row=15, columnspan=2)


janela.mainloop()
