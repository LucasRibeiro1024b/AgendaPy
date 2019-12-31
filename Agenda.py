from tkinter import *
from functools import partial
from random import *
import os
import sqlite3

janela = Tk()
conn = sqlite3.connect("base.db")

#Functions

def create_bd():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE Contatos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        numero INTEGER,
        email TEXT NOT NULL
    );
    """)

    print("Tabela criada")

def del_bd():
    pasta = "/home/lucas/Documents/TKINTER"
    arquivo = 'base.db'
    diretorio = os.listdir(pasta)
    if arquivo in diretorio:
        os.remove('{}/{}' .format(pasta, arquivo))
        print('removido')
        conn.close()
    else:
        print('Arquivo não encontrado')

#funções
def inserir():
    name_c = nome_text.get()
    numero_c = int(numero_text.get())
    email_c = email_text.get()

    cursor.execute("""
    INSERT INTO Contatos (nome, numero, email) VALUES (?, ?, ?)""",
    (name_c, numero_c, email.c))

    conn.commit()
    
def remover():
    id_c = Id_text.get()
    cursor.execute("""
    DELETE FROM Contatos WHERE id = ?
    """, (id_c))
    
    conn.commit()

def search_id():
    id_c = int(Id_text.get())
    

#Head
    
intro = Label(janela, text="Agenda")
intro.place(x=75, y=10)

Id_lb = Label(janela, text="ID")
Id_lb.place(x=10, y=40)
Id_text = Entry(janela)
Id_text["width"] = "10"
Id_text.place(x=80, y=40)

search_id = Button(janela, width=10, text="Pesquisar ID", command=search_id)
search_id.place(x=175, y=40)

#Body

inserir_bt = Button(janela, width=10, text="Inserir", command=inserir)
inserir_bt.place(x=10, y=200)

remover_bt = Button(janela, width=10, text="Remover", command=remover)
remover_bt.place(x=120, y=200)

nome_lb = Label(janela, text="Nome")
nome_lb.place(x=10, y=110)
nome_text = Entry(janela)
nome_text["width"] = "30"
nome_text.place(x=70, y=110)

numero_lb = Label(janela, text="Numero")
numero_lb.place(x=10, y=140)
numero_text = Entry(janela)
numero_text["width"] = "30"
numero_text.place(x=70, y=140)

email_lb = Label(janela, text="Email")
email_lb.place(x=10, y=170)
email_text = Entry(janela)
email_text["width"] = "30"
email_text.place(x=70, y=170)

bd_bt = Button(janela, width=6, text="Criar BD", command=create_bd)
bd_bt.place(x=10, y=310)

delbd_bt = Button(janela, width=6, text="Delete BD", command=del_bd)
delbd_bt.place(x=85, y=310)

#Testing field

Log_lb = Label(janela, text="Log")
Log_lb.place(x=10, y=350)

#tamanho da janela e loop do programa
janela.geometry("350x400+200+200")
janela.mainloop()
conn.close()
