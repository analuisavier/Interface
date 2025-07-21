# -*- coding: utf-8 -*-
"""
Aula Prática de UI com Tkinter: Mood Tracker App
3 partes, cada uma com 5 blocos de 3 exercícios (1 resolvido + 2 similares)
Objetivo: construir um app para registrar e visualizar o humor diário.


"""
# ------------------------------
# PARTE 1: SETUP, JANELA E BOTÃO (Mood Tracker)
# Narrativa: iniciar o Mood Tracker com um botão para registrar humor.
# ------------------------------


# Bloco 1: Janela e título do app
# 1. (resolvido) Crie a janela com título "Mood Tracker" e cor de fundo clara.

import tkinter as tk


root = tk.Tk()
root.title("Mood Tracker")
root.configure(bg="#FF8800")
label = tk.Label(root, text="Bem-vindo ao Mood Tracker!", font=("Arial", 16), bg="#F0F0F0")
label.pack(pady=20)
root.mainloop()

# 2. (prática) Altere o texto de boas‑vindas para incluir a data atual (use datetime).

import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
root = tk.Tk()
root.title("Mood Tracker")
root.configure(bg="#FFA500")
label = tk.Label(
    root, 
    text=f"Bem-vindo ao Mood Tracker! Hoje é {date}", 
    font=("Arial", 16), 
    bg="#F0F0F0"
    )
label.pack(pady=20)
root.mainloop()

# 3. (prática) Modifique a cor de fundo para um tom pastel diferente.

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
root = tk.Tk()
root.title("Mood Tracker")
root.configure(bg="#FF8800")
label = tk.Label(
    root, 
    text=f"Bem-vindo ao Mood Tracker! Hoje é {date}", 
    font=("Arial", 16), 
    bg="#FF8800"
    )
label.pack(pady=20)
root.mainloop()

# Bloco 2: Botão de registrar humor
# (resolvido) Adicione um botão “Registrar Humor” que imprima no console “Humor registrado!”:
import tkinter as tk


def registrar():
    print("Humor registrado!")


root = tk.Tk()
btn = tk.Button(root, text="Registrar Humor", command=registrar)
btn.pack(pady=10)
root.mainloop()


# 2. (prática) Crie um botão "Salvar Humor" que imprime "Salvo!" no console.

def salvo():
    print("Salvo!")

root = tk.Tk()
btn = tk.Button(root, text="salvar", command=salvo)
btn.pack(pady=10)
root.mainloop()


# 3. (prática) Crie um botão "Gravar Humor" que imprime "Gravado!" no console.

def gravar():
    print("Gravado!")

btn = tk.Button(root, text="Gravar Humor", command=gravar)
btn.pack(pady=10)
root.mainloop()

# (prática) Crie um botão "Imprimir Data" que imprime a data de hoje no console.

def imprimir():
    print(f"A Data de hoje é {date}")


date = datetime.datetime.now().strftime("%d-%m-%y")
btn = tk.Button(root, text="imprimir data", command=imprimir) 
btn.pack(pady=10)
root.mainloop()   

# (prática) Crie um botão "Mostrar Histórico" que imprime no console os momentos que você registrou o humor.

def mostrar():
    print()

