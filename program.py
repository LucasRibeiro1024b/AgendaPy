from tkinter import *
from functools import partial

#funções

def bt_click(but):
    lb["text"] = "Posso enviar agora, nice man "

def bt_color():
    cores = {"blue", "red", "black", "green"}
    janela["background"] = "black"

#botões e janelas

janela = Tk()

intro = Label(janela, text="Sistema de cadastro de telefone")
intro.place(x=75, y=10)

butt1 = Button(janela, width=30, text="change text and send text")
butt1["command"] = partial(bt_click, butt1)
butt1.place(x=10, y=100)

butt2 = Button(janela, width=10, text="Change color", command=bt_color)
butt2.place(x=10, y=50)

lb = Label(janela, text="Teste")
lb.place(x=10, y=150)


#tamanho da janela e loop do programa
janela.geometry("350x400+200+200")
janela.mainloop()
