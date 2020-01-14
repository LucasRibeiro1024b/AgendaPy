from tkinter import *
import os
import sqlite3
import re

janela = Tk()

pasta = "/home/lucas/Documents/TKINTER"
arquivo = 'base.db'
diretorio = os.listdir(pasta)
if arquivo not in diretorio:
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE Contatos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        numero TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)
    
#functions
'''
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
'''
def limpar():
    Id_text.delete(0, END)
    nome_text.delete(0, END)
    numero_text.delete(0, END)
    email_text.delete(0, END)
    nome_error["text"] = ""
    numero_error["text"] = ""
    email_error["text"] = ""

def inserir():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    
    id_c = int(Id_text.get())
    name_c = nome_text.get()
    numero_c = numero_text.get()
    email_c = email_text.get()

    all_valid = True

    if len(name_c) <= 40:
        nome_error["text"] = "OK!"
    else:
        all_valid = False
        nome_error["text"] = "ERROR"
        nome_text["background"] = "red"
    
    if re.match(r'[1-9]{2}[0-9]{9}', numero_c) and len(numero_c) == 11:
        numero_error["text"] = "OK!"
    else:
        all_valid = False
        numero_error["text"] = "ERROR"
        numero_text["background"] = "red"

    if re.match(r'^[\w-]+@[a-z\d]+\.[\w]{3}', email_c):
        email_error["text"] = "OK!"
    else:
        all_valid = False
        email_error["text"] = "ERROR"
        email_text["background"] = "red"

    if all_valid:
        cursor.execute("""
        INSERT INTO Contatos (id, nome, numero, email) VALUES (?, ?, ?, ?)""",
        (id_c, name_c, numero_c, email_c))

        conn.commit()

        limpar()

    conn.close()
    
def remover():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    
    id_c = Id_text.get()
    cursor.execute("""
    DELETE FROM Contatos WHERE id = ?
    """, (id_c))
    
    conn.commit()
    conn.close()
    
    limpar()


def alterar():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()

    id_c = int(Id_text.get())
    name_c = nome_text.get()
    numero_c = numero_text.get()
    email_c = email_text.get()

    all_valid = True

    if len(name_c) <= 40:
        nome_error["text"] = "OK!"
    else:
        all_valid = False
        nome_error["text"] = "ERROR"
        nome_text["background"] = "red"
    
    if re.match(r'[1-9]{2}[0-9]{9}', numero_c) and len(numero_c) == 11:
        numero_error["text"] = "OK!"
    else:
        all_valid = False
        numero_error["text"] = "ERROR"
        numero_text["background"] = "red"

    if re.match(r'^[\w-]+@[a-z\d]+\.[\w]{3}', email_c):
        email_error["text"] = "OK!"
    else:
        all_valid = False
        email_error["text"] = "ERROR"
        email_text["background"] = "red"

    if all_valid:
        cursor.execute("""
            UPDATE Contatos
            SET nome = ?, numero = ?, email = ?
            WHERE id = ?""",
        (name_c, numero_c, email_c, id_c))

        conn.commit()

        limpar()
    
    conn.close()

def search_id():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    
    id_c = int(Id_text.get())

    try:
        cursor.execute("""
        SELECT * FROM Contatos WHERE id=?;
        """, (id_c,))
    
        for linha in cursor.fetchall():
            if (linha[0] == id_c):
                test = True
                nome_text.delete(0, END)
                nome_text.insert(END, linha[1])
    
                numero_text.delete(0, END)
                numero_text.insert(END, linha[2])
            
                email_text.delete(0, END)
                email_text.insert(END, linha[3])
                
    except:
        limpar()
        
    conn.close()

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

alterar_bt = Button(janela, width=10, text="Alterar", command=alterar)
alterar_bt.place(x=230, y=200)

nome_lb = Label(janela, text="Nome")
nome_lb.place(x=10, y=110)
nome_text = Entry(janela)
nome_text["width"] = "30"
nome_text.place(x=70, y=110)
nome_error = Label(janela, text="")
nome_error.place(x=350, y=110)

numero_lb = Label(janela, text="Numero")
numero_lb.place(x=10, y=140)
numero_text = Entry(janela)
numero_text["width"] = "30"
numero_text.place(x=70, y=140)
numero_error = Label(janela, text="")
numero_error.place(x=350, y=140)

email_lb = Label(janela, text="Email")
email_lb.place(x=10, y=170)
email_text = Entry(janela)
email_text["width"] = "30"
email_text.place(x=70, y=170)
email_error = Label(janela, text="")
email_error.place(x=350, y=170)

'''
delbd_bt = Button(janela, width=6, text="Delete BD", command=del_bd)
delbd_bt.place(x=85, y=310)
'''

#tamanho da janela e loop do programa
janela.geometry("400x280+100+200")
janela.mainloop()
conn.close()
