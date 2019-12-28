from tkinter import *
from functools import partial
from random import *

#Importando biblioteca base do sql
import sqlite3
conn = sqlite3.connect("base.db")
cursor = conn.cursor()

def create_bd():
    cursor.execute("""CREATE TABLE Contatos (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               numero INTEGER,
               email TEXT NOT NULL
               );""")
    print("Tabela criada")


janela = Tk()

#funções
def inserir():
    print("Inserir contato")

def bt_click(but):
    print(but)
    lb["text"] = "Posso enviar agora, nice man "

def bt_color():
    cores = ["blue", "red", "black", "green"]
    i = randint(0, 3)
    janela["background"] = cores[i]

def bt_get():
    lb["text"] = textfield.get()

#Head
    
intro = Label(janela, text="Sistema de cadastro de telefone")
intro.place(x=75, y=10)

pos = Label(janela, text="Codigo :")
pos.place(x=20, y=30)

textfield = Entry(janela)
textfield["width"] = "10"
textfield.place(x=80, y=30)

bott3 = Button(janela, width=10, text="Click do Entry", command=bt_get)
bott3.place(x=175, y=30)

#Body

butt2 = Button(janela, width=10, text="Change color", command=bt_color)
butt2.place(x=10, y=55)

butt1 = Button(janela, width=30, text="change text and send text")
#butt1["command"] = partial(bt_click, butt1)
butt1.place(x=10, y=95)


id_lb = Label(janela, text="Id")
id_lb.place(x=10, y=130)
id_text = Entry(janela)
id_text["width"] = "10"
id_text.place(x=70, y=130)

nome_lb = Label(janela, text="Nome")
nome_lb.place(x=10, y=155)
nome_text = Entry(janela)
nome_text["width"] = "30"
nome_text.place(x=70, y=155)

numero_lb = Label(janela, text="Numero")
numero_lb.place(x=10, y=180)
numero_text = Entry(janela)
numero_text["width"] = "30"
numero_text.place(x=70, y=180)

email_lb = Label(janela, text="Email")
email_lb.place(x=10, y=205)
email_text = Entry(janela)
email_text["width"] = "30"
email_text.place(x=70, y=205)

bd_bt = Button(janela, width=10, text="Criar BD", command=create_bd)
bd_bt.place(x=120, y=350)

#Testing field

lb = Label(janela, text="Teste")
lb.place(x=10, y=350)

#tamanho da janela e loop do programa
janela.geometry("350x400+200+200")
janela.mainloop()
conn.close()
