from tkinter import *

def bt_click():
    print("bt click")
    lb["text"] = "Funcionou!!"

def bt_color():
    janela["background"] = "red"

janela = Tk()

bt = Button(janela, width=10, text="OK", command=bt_click)
bt.place(x=10, y=100)

bt2 = Button(janela, width=10, text="OK", command=bt_color)
bt2.place(x=10, y=50)

lb = Label(janela, text="Teste")
lb.place(x=10, y=150)

janela.geometry("300x600+200+200")
janela.mainloop()
