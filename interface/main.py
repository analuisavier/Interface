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
root.configure(bg="#F0F0F0")
label = tk.Label(root, text="Bem-vindo ao Mood Tracker!", font=("Arial", 16), bg="#F0F0F0")
label.pack(pady=20)
root.mainloop()


# (prática) Altere o texto de boas‑vindas para incluir a data atual (use datetime).

from datetime import datetime

root = tk.Tk()
data_atual = datetime.now().strftime("%d/%m/%Y")
label = tk.Label(root, text=f"Bem-vindo ao Mood Tracker! Hoje é {data_atual}", font=("Arial", 16), bg="#F0F0F0")
label.pack(pady=20)
root.mainloop()


# (prática) Modifique a cor de fundo para um tom laranja.

root = tk.Tk()
root.configure(bg="#FFA500")
data_atual = datetime.now().strftime("%d/%m/%Y")
label = tk.Label(root, text=f"Bem-vindo ao Mood Tracker! Hoje é {data_atual}", font=("Arial", 16), bg="#FFA500")
label.pack(pady=20)
root.mainloop()


# Bloco 2: Botão de registrar humor
# (resolvido) Adicione um botão “Registrar Humor” que imprima no console “Humor registrado!”:
import tkinter as tk

momentos = []

def registrar():
    # Captura o momento atual
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    momentos.append(agora)
    print("Humor registrado!")
    print(f"Momento: {agora}")
    label_status.config(text="✅ Humor registrado com sucesso!", 
                       fg="green", font=("Arial", 12, "bold"))

btn_registrar = tk.Button(root, text="Registrar Humor", command=registrar)
btn_registrar.pack(pady=10)

root.mainloop()

# (prática) Crie um botão "Imprimir Data" que imprime a data de hoje no console.

def imprimir_data():
    data_atual = datetime.now().strftime("%d/%m/%Y")
    print(data_atual)
    label_feedback.config(text=f"📅 Hoje é {data_atual}", 
                         fg="blue", font=("Arial", 12, "bold"))


btn_data = tk.Button(root, text="Imprimir Data", command=imprimir_data)
btn_data.pack(pady=10)

root.mainloop()

# (prática) Crie um botão "Mostrar Histórico" que imprime no console os momentos que você registrou o humor.

def mostrar_historico():
    print("Histórico de humor:")
    if momentos:
        for i, momento in enumerate(momentos, 1):
            print(f"{i}. {momento}")
        label_info.config(text=f"📋 Histórico mostrado! Total: {len(momentos)} registros", 
                         fg="purple", font=("Arial", 12, "bold"))
        else:
        print("Nenhum registro encontrado.")
        label_info.config(text="❌ Nenhum registro encontrado", 
                         fg="red", font=("Arial", 12))


# Criar o botão para mostrar histórico
btn_historico = tk.Button(root, text="Mostrar Histórico", command=mostrar_historico)
btn_historico.pack(pady=5)

root.mainloop()

# Bloco 3: Layout básico
# (resolvido) Use Frame/pack para empilhar um Label e o botão de registrar humor:
import tkinter as tk


root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=20)


lbl = tk.Label(frame, text="Como você se sente hoje?")
lbl.pack()


btn = tk.Button(frame, text="Registrar Humor", command=lambda: None)
btn.pack(pady=5)


root.mainloop()

# (prática) Organize um Entry (TextField) e um botão na mesma Frame.


root = tk.Tk()
root.title("Entry e Botão")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame)
entry.pack(side="left", padx=5)

btn = tk.Button(frame, text="Registrar Humor", command=lambda: None)
btn.pack(side="left", padx=5)  

root.mainloop()


# (prática) Empilhe um OptionMenu (dropdown) e um botão na Frame.

import tkinter as tk

root = tk.Tk()
root.title("OptionMenu e Botão")

frame = tk.Frame(root)
frame.pack(pady=20)

humor_var = tk.StringVar(root)
humor_var.set("😀") 

opcoes_humor = ["😀", "😔", "🙃", "😴", "😡"]

def on_humor_select(valor):
    print(f"Humor selecionado: {valor}")

dropdown = tk.OptionMenu(frame, humor_var, *opcoes_humor, command=on_humor_select)
dropdown.config(width=10)
dropdown.pack(pady=5)  

def salvar_humor():
    humor_atual = humor_var.get()
    print(f"Humor salvo: {humor_atual}")

btn_salvar = tk.Button(frame, text="Salvar Humor", command=salvar_humor)
btn_salvar.pack(pady=5)

root.mainloop()


# Bloco 4: Evento de clique altera texto
# (resolvido) Faça o botão atualizar o Label para “Humor registrado!”:
import tkinter as tk


root = tk.Tk()
msg = tk.Label(root, text="")
msg.pack(pady=10)


def on_click():
    msg.config(text="Humor registrado!")


btn = tk.Button(root, text="Registrar Humor", command=on_click)
btn.pack()


root.mainloop()


# (prática) Faça o botão atualizar para “Salvo com sucesso!” no Label.

root = tk.Tk()
msg = tk.Label(root, text="")
msg.pack(pady=10)

def on_click_salvar():
    msg.config(text="Salvo com sucesso!")
    
btn_salvar = tk.Button(root, text="Salvar", command=on_click_salvar)
btn_salvar.pack(pady=5) 

root.mainloop()   

# (prática) Faça o botão atualizar para “Gravado com sucesso!” no Label.

root = tk.Tk()
msg = tk.Label(root, text="")
msg.pack(pady=10)

def on_click_gravar():
    msg.config(text="Gravado com sucesso!")

btn_gravar = tk.Button(root, text="Gravar", command=on_click_gravar)
btn_gravar.pack(pady=5)

root.mainloop()

# ------------------------------
# PARTE 2: COMPONENTES E NAVEGAÇÃO (Mood Tracker)
# Objetivo: adicionar seleção de humor e tela de histórico.
# ------------------------------


# Bloco 1: Dropdown de humor
# (resolvido) Adicione um OptionMenu com emojis e imprima seleção:
import tkinter as tk


def on_select(value):
    print(value)


root = tk.Tk()
var = tk.StringVar(root)
var.set("😀")
opts = ["😀", "😔", "🙃"]
menu = tk.OptionMenu(root, var, *opts, command=on_select)
menu.pack(pady=10)
root.mainloop()


# (prática) Crie um OptionMenu de clima ["☀️","🌧️","❄️"] que imprima escolha.


def on_clima_select(value):    
    print(f"Clima selecionado: {value}")

root = tk.Tk()
var_clima = tk.StringVar(root)
var_clima.set("☀️")
opts_clima = ["☀️", "🌧️", "❄️"]
menu_clima = tk.OptionMenu(root, var_clima, *opts_clima, command=on_clima_select)
menu_clima.pack(pady=10)
root.mainloop()


# (prática) Crie um OptionMenu de níveis de energia ["Alto","Médio","Baixo"].
def on_energia_select(value):    
    print(f"Nível de energia selecionado: {value}")

root = tk.Tk()
var_energia = tk.StringVar(root)
var_energia.set("Alto")
opts_energia = ["Alto", "Médio", "Baixo"]
menu_energia = tk.OptionMenu(root, var_energia, *opts_energia, command=on_energia_select)
menu_energia.pack(pady=10)
root.mainloop()

# Bloco 2: Checkbox múltipla escolha
# 1. (resolvido) Adicione três Checkbutton para sintomas e imprima lista selecionada:
import tkinter as tk


root = tk.Tk()
sintomas = ["Dor de cabeça", "Fome", "Sono"]
vars = []
def on_change():
    sel = [s for v, s in zip(vars, sintomas) if v.get()]
    print(sel)


for s in sintomas:
    v = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=s, variable=v, command=on_change)
    chk.pack(anchor="w")
    vars.append(v)


root.mainloop()


# (prática) Crie Checkbutton para atividades ["Caminhada","Leitura","Música"].

root = tk.Tk()
root.title("Atividades e Humor Físico")

tk.Label(root, text="Selecione suas atividades:", font=("Arial", 12, "bold")).pack(pady=(10,5))

vars_atividade = []
atividades = ["Caminhada", "Leitura", "Música"]

def on_atividade_change():
    sel = [a for v, a in zip(vars_atividade, atividades) if v.get()]
    print(f"Atividades selecionadas: {sel}")

for a in atividades:
    v = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=a, variable=v, command=on_atividade_change)
    chk.pack(anchor="w", padx=20)
    vars_atividade.append(v)

root.mainloop()    

# (prática) Crie Checkbutton para humor físico ["Bem","Regular","Mal"].

root = tk.Tk()
root.title("Humor Físico")

vars_humor = []
humores = ["Bem", "Regular", "Mal"]

def on_humor_change():
    sel = [h for v, h in zip(vars_humor, humores) if v.get()]
    print(f"Humor físico: {sel}")

for h in humores:
    v = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=h, variable=v, command=on_humor_change)
    chk.pack(anchor="w")
    vars_humor.append(v)

root.mainloop()

# Bloco 3: Navegação Home/Histórico
# (resolvido) Use Frames e botão para alternar entre Home e Histórico:
import tkinter as tk


root = tk.Tk()
home_frame = tk.Frame(root)
hist_frame = tk.Frame(root)


tk.Label(home_frame, text="Home: registre seu humor").pack()
tk.Label(hist_frame, text="Histórico: Sem registros").pack()


def show_home():
    hist_frame.pack_forget()
    home_frame.pack()


def show_history():
    home_frame.pack_forget()
    hist_frame.pack()


btn_h = tk.Button(root, text="Home", command=show_home)
btn_h.pack(side="left")
btn_hist = tk.Button(root, text="Histórico", command=show_history)
btn_hist.pack(side="left")


show_home()
root.mainloop()


# (prática) Na view Histórico, liste 3 registros de humor simulados (use Label).


root = tk.Tk()
root.title("Mood Tracker - Navegação")

home_frame = tk.Frame(root)
hist_frame = tk.Frame(root)

# Home Frame
tk.Label(home_frame, text="Home: registre seu humor", font=("Arial", 14)).pack(pady=20)

# Histórico Frame com registros simulados
tk.Label(hist_frame, text="Histórico de Humor", font=("Arial", 14, "bold")).pack(pady=10)

# 3 registros simulados
registros = [
    "21/07/2025 09:30 - 😀 Feliz",
    "20/07/2025 15:45 - 😔 Triste", 
    "19/07/2025 12:20 - 🙃 Neutro"
]

for registro in registros:
    tk.Label(hist_frame, text=registro, font=("Arial", 11), 
             bg="#F0F0F0", relief="solid", borderwidth=1).pack(pady=5, padx=20, fill="x")

def show_home():
    hist_frame.pack_forget()
    home_frame.pack()

def show_history():
    home_frame.pack_forget()
    hist_frame.pack()

# Botões de navegação
btn_home = tk.Button(root, text="Home", command=show_home)
btn_home.pack(side="left")
btn_hist = tk.Button(root, text="Histórico", command=show_history)
btn_hist.pack(side="left")

show_home()
root.mainloop()

# (prática) Adicione botão “Voltar” em cada view para navegar.

root = tk.Tk()
root.title("Mood Tracker - Com Botão Voltar")

home_frame = tk.Frame(root)
hist_frame = tk.Frame(root)

# Home Frame com botão para ir ao histórico
tk.Label(home_frame, text="Home: registre seu humor", font=("Arial", 14)).pack(pady=20)
btn_ir_hist = tk.Button(home_frame, text="Ver Histórico", command=lambda: show_history())
btn_ir_hist.pack(pady=10)

# Histórico Frame com botão voltar
tk.Label(hist_frame, text="Histórico de Humor", font=("Arial", 14, "bold")).pack(pady=10)

registros = [
    "21/07/2025 09:30 - 😀 Feliz",
    "20/07/2025 15:45 - 😔 Triste", 
    "19/07/2025 12:20 - 🙃 Neutro"
]

for registro in registros:
    tk.Label(hist_frame, text=registro, font=("Arial", 11)).pack(pady=3)

# Botão Voltar no histórico
btn_voltar = tk.Button(hist_frame, text="← Voltar para Home", command=lambda: show_home())
btn_voltar.pack(pady=15)

def show_home():
    hist_frame.pack_forget()
    home_frame.pack()

def show_history():
    home_frame.pack_forget()
    hist_frame.pack()

show_home()
root.mainloop()


# Bloco 4: Lista de registros
# (resolvido) Exiba uma lista de Radiobuttons e imprima seleção:
import tkinter as tk


root = tk.Tk()
var = tk.StringVar()
for emoji in ["😀","😔","🙃"]:
    rb = tk.Radiobutton(root, text=emoji, variable=var, value=emoji,
                        command=lambda: print("Selecionado:", var.get()))
    rb.pack(anchor="w")
root.mainloop()


# (prática) Crie lista de dias da semana com Radiobuttons.

root = tk.Tk()
root.title("Seletor de Dia da Semana")

tk.Label(root, text="Selecione o dia da semana:", font=("Arial", 12, "bold")).pack(pady=10)

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", 
               "Sexta-feira", "Sábado", "Domingo"]

var_dia = tk.StringVar()
var_dia.set("Segunda-feira")  # valor padrão

def on_dia_select():
    print(f"Dia selecionado: {var_dia.get()}")

for dia in dias_semana:
    rb = tk.Radiobutton(root, text=dia, variable=var_dia, value=dia, command=on_dia_select)
    rb.pack(anchor="w", padx=20, pady=2)

root.mainloop()

# (prática) Crie lista de cores com Radiobuttons.

root = tk.Tk()
root.title("Seletor de Cores")

tk.Label(root, text="Escolha sua cor favorita:", font=("Arial", 12, "bold")).pack(pady=10)

cores = ["🔴 Vermelho", "🔵 Azul", "🟢 Verde", "🟡 Amarelo", "🟣 Roxo", "🟠 Laranja"]

var_cor = tk.StringVar()
var_cor.set("🔴 Vermelho")  # valor padrão

def on_cor_select():
    print(f"Cor selecionada: {var_cor.get()}")

for cor in cores:
    rb = tk.Radiobutton(root, text=cor, variable=var_cor, value=cor, command=on_cor_select)
    rb.pack(anchor="w", padx=20, pady=2)

root.mainloop()

# Bloco 5: Slider para intensidade
# (resolvido) Adicione um Scale de 1–10 que imprime valor:
import tkinter as tk


def on_slide(v):
    print(v)


root = tk.Tk()
s = tk.Scale(root, from_=1, to=10, orient="horizontal", command=on_slide)
s.pack(pady=10)
root.mainloop()


# (prática) Crie um Scale vertical de 0–100.

def on_slide_vertical(valor):
    print(f"Valor vertical: {valor}")

root = tk.Tk()
root.title("Scale Vertical 0-100")

tk.Label(root, text="Escala Vertical (0-100):", font=("Arial", 12)).pack(pady=10)

# Scale vertical de 0 a 100
scale_vertical = tk.Scale(root, from_=0, to=100, orient="vertical", 
                         command=on_slide_vertical, length=300)
scale_vertical.set(50)  # valor inicial
scale_vertical.pack(pady=20)

root.mainloop()

# (prática) Crie Scale para ajustar opacidade de um Label (use .config(fg=...) com valor de escala).


def ajustar_opacidade(valor):
    # Converte valor 0-100 para intensidade de cinza (0-255)
    intensidade = int((int(valor) / 100) * 255)
    cor_hex = f"#{intensidade:02x}{intensidade:02x}{intensidade:02x}"
    
    # Atualiza a cor do label (mais claro = menos opaco)
    label_opacidade.config(fg=cor_hex)
    label_valor.config(text=f"Opacidade: {valor}%")

root = tk.Tk()
root.title("Controle de Opacidade")
root.configure(bg="white")

# Label que terá a opacidade ajustada
label_opacidade = tk.Label(root, text="TEXTO COM OPACIDADE VARIÁVEL", 
                          font=("Arial", 16, "bold"), bg="white")
label_opacidade.pack(pady=20)

# Label para mostrar valor atual
label_valor = tk.Label(root, text="Opacidade: 50%", font=("Arial", 10))
label_valor.pack()

# Scale horizontal para controlar opacidade
tk.Label(root, text="Ajuste a opacidade:", font=("Arial", 12)).pack(pady=(20,5))
scale_opacidade = tk.Scale(root, from_=0, to=100, orient="horizontal", 
                          command=ajustar_opacidade, length=300)
scale_opacidade.set(50)  # valor inicial (50% de opacidade)
scale_opacidade.pack(pady=10)

# Definir cor inicial
ajustar_opacidade(50)

root.mainloop()


# ------------------------------
# PARTE 3: GRÁFICOS E COMPONENTES AVANÇADOS
# ------------------------------
# Objetivo: visualizar tendências de humor


# CONFIGURAÇÃO
# você irá precisar instalar o matplotlib, no terminal digite:
# pip instal matplotlib


# Bloco 1: Gráfico de barras de humor semanal
# (resolvido) Exiba um bar chart com matplotlib dentro de um Canvas Tk:
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)
data = [2,1,3]; labels = ["😀","😔","🙃"]
ax.bar(labels, data)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()


# 2. (prática) Ajuste dados para proporções diárias de ontem.

from datetime import timedelta

root = tk.Tk()
root.title("Proporções de Humor - Ontem")

fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)

# Dados simulados para "ontem" - proporções mais realistas
data = [8, 3, 2]  # Feliz: 8 momentos, Triste: 3, Neutro: 2
labels = ["😀", "😔", "🙃"]

# Calcular data de ontem
ontem = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")

ax.bar(labels, data, color=['#FFD700', '#87CEEB', '#DDA0DD'])
ax.set_title(f"Humor de {ontem}")
ax.set_ylabel("Número de registros")

# Adicionar valores nas barras
for i, v in enumerate(data):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()

# 3. (prática) Alterne ordem das barras (descrescente).

root = tk.Tk()
root.title("Humor - Ordem Decrescente")

fig = Figure(figsize=(4,3))
ax = fig.add_subplot(111)

# Dados originais
data_original = [2, 1, 3]
labels_original = ["😀", "😔", "🙃"]

# Criar pares (valor, label) e ordenar por valor decrescente
pares = list(zip(data_original, labels_original))
pares_ordenados = sorted(pares, key=lambda x: x[0], reverse=True)

# Separar novamente em listas ordenadas
data_ordenada = [par[0] for par in pares_ordenados]
labels_ordenadas = [par[1] for par in pares_ordenados]

# Cores diferentes para cada barra
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1']

ax.bar(labels_ordenadas, data_ordenada, color=cores)
ax.set_title("Humor Semanal (Decrescente)")
ax.set_ylabel("Frequência")

# Adicionar valores nas barras
for i, v in enumerate(data_ordenada):
    ax.text(i, v + 0.05, str(v), ha='center', va='bottom', fontweight='bold')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()

# Bloco 2: Gráfico de pizza dos humores
# (resolvido) Exiba um pie chart:
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
fig = Figure(figsize=(3,3))
ax = fig.add_subplot(111)
values = [50,30,20]; labels = ["😀","😔","🙃"]
ax.pie(values, labels=labels, autopct='%1.1f%%')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()


# (prática) Modifique valores para refletir dados reais.

root = tk.Tk()
root.title("Distribuição Real de Humor")

fig = Figure(figsize=(4,4))
ax = fig.add_subplot(111)

# Dados mais realistas baseados em uma semana típica
values = [45, 25, 20, 10]  # percentuais mais realistas
labels = ["😀 Feliz", "😔 Triste", "🙃 Neutro", "😴 Cansado"]
colors = ['#FFD700', '#87CEEB', '#DDA0DD', '#F0E68C']

# Criar gráfico de pizza com dados reais
wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', 
                                  colors=colors, startangle=90)

ax.set_title("Distribuição Semanal de Humor\n(Dados Realistas)", 
             fontsize=12, fontweight='bold')

# Melhorar a aparência do texto
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()


# (prática) Adicione texto central indicando total de registros.

root = tk.Tk()
root.title("Pizza com Total Central")

fig = Figure(figsize=(4,4))
ax = fig.add_subplot(111)

# Dados com números absolutos para calcular total
registros_absolutos = [25, 15, 12, 8]  # números reais de registros
labels = ["😀", "😔", "🙃", "😴"]
colors = ['#FFD700', '#87CEEB', '#DDA0DD', '#F0E68C']

# Calcular total de registros
total_registros = sum(registros_absolutos)

# Criar pizza com buraco no centro (donut chart)
wedges, texts, autotexts = ax.pie(registros_absolutos, labels=labels, 
                                  autopct='%1.1f%%', colors=colors,
                                  pctdistance=0.85, startangle=90,
                                  wedgeprops=dict(width=0.5))

# Adicionar texto central com total
centro_texto = f'Total\n{total_registros}\nregistros'
ax.text(0, 0, centro_texto, horizontalalignment='center', 
        verticalalignment='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))

ax.set_title("Registros de Humor da Semana", fontsize=14, fontweight='bold')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()

# Bloco 3: Tabela de registros
# (resolvido) Crie uma tabela simples com ttk.Treeview:
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
cols = ("Dia","Humor")
tree = ttk.Treeview(root, columns=cols, show="headings")
for c in cols: tree.heading(c, text=c)
rows = [("Segunda","😀"),("Terça","😔"),("Quarta","🙃")]
for r in rows: tree.insert("", tk.END, values=r)
tree.pack()
root.mainloop()


# (prática) Adicione coluna "Intensidade" com valores.

root = tk.Tk()
root.title("Tabela com Intensidade")

# Definir colunas incluindo "Intensidade"
cols = ("Dia", "Humor", "Intensidade")
tree = ttk.Treeview(root, columns=cols, show="headings")

# Configurar cabeçalhos das colunas
for c in cols: 
    tree.heading(c, text=c)
    tree.column(c, width=120, anchor="center")

# Dados com coluna de intensidade (escala 1-10)
rows = [
    ("Segunda", "😀", "8"),
    ("Terça", "😔", "3"),
    ("Quarta", "🙃", "6"),
    ("Quinta", "😀", "9"),
    ("Sexta", "😔", "4"),
    ("Sábado", "😀", "7"),
    ("Domingo", "🙃", "5")
]

for r in rows: 
    tree.insert("", tk.END, values=r)

tree.pack(pady=20, padx=20)
root.mainloop()

# (prática) Ordene linhas por dia da semana.

root = tk.Tk()
root.title("Tabela Ordenada por Dia")

cols = ("Dia", "Humor", "Intensidade")
tree = ttk.Treeview(root, columns=cols, show="headings")

for c in cols: 
    tree.heading(c, text=c)
    tree.column(c, width=120, anchor="center")

# Dados desordenados originalmente
dados_desordenados = [
    ("Sexta", "😔", "4"),
    ("Segunda", "😀", "8"),
    ("Domingo", "🙃", "5"),
    ("Quarta", "🙃", "6"),
    ("Terça", "😔", "3"),
    ("Sábado", "😀", "7"),
    ("Quinta", "😀", "9")
]

# Ordem correta dos dias da semana
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

# Função para ordenar por dia da semana
def ordenar_por_dia(item):
    dia = item[0]
    return ordem_dias.index(dia) if dia in ordem_dias else 999

# Ordenar os dados por dia da semana
dados_ordenados = sorted(dados_desordenados, key=ordenar_por_dia)

# Inserir dados ordenados na tabela
for r in dados_ordenados: 
    tree.insert("", tk.END, values=r)

# Adicionar label explicativo
tk.Label(root, text="Registros ordenados por ordem dos dias da semana", 
         font=("Arial", 12, "bold")).pack(pady=10)

tree.pack(pady=10, padx=20)
root.mainloop()

# Bloco 4: Canvas para trend line
# (resolvido) Desenhe uma linha conectando pontos no Canvas Tkinter:
import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200, bg="#FFF")
canvas.pack()
points = [(50,150),(100,100),(150,120),(200,80)]
for i in range(len(points)-1):
    canvas.create_line(*points[i], *points[i+1], width=2, fill="#FF0000")
root.mainloop()


# (prática) Ajuste cor da linha para azul.


root = tk.Tk()
root.title("Linha de Tendência - Azul")

canvas = tk.Canvas(root, width=400, height=200, bg="#FFF")
canvas.pack()

points = [(50,150), (100,100), (150,120), (200,80)]

# Linha azul em vez de vermelha
for i in range(len(points)-1):
    canvas.create_line(*points[i], *points[i+1], width=3, fill="#0066CC")

# Adicionar título
canvas.create_text(200, 20, text="Tendência de Humor - Semana", 
                  font=("Arial", 12, "bold"), fill="#0066CC")

root.mainloop()


# (prática) Desenhe círculos nos pontos da linha (use create_oval).

root = tk.Tk()
root.title("Linha com Pontos Circulares")

canvas = tk.Canvas(root, width=400, height=200, bg="#FFF")
canvas.pack()

points = [(50,150), (100,100), (150,120), (200,80)]

# Desenhar linha azul
for i in range(len(points)-1):
    canvas.create_line(*points[i], *points[i+1], width=3, fill="#0066CC")

# Desenhar círculos nos pontos
raio = 6
for x, y in points:
    canvas.create_oval(x-raio, y-raio, x+raio, y+raio, 
                      fill="#FF6600", outline="#0066CC", width=2)

# Adicionar labels nos pontos
labels = ["Seg", "Ter", "Qua", "Qui"]
for i, (x, y) in enumerate(points):
    if i < len(labels):
        canvas.create_text(x, y-20, text=labels[i], 
                          font=("Arial", 9, "bold"), fill="#333")

root.mainloop()