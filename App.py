import re
from tkinter import *
from Contact import Contact

class Application(Frame):
  def __init__(self, master):
    super().__init__(master)
    
    self.container1 = Frame(master)
    self.container1.grid(column=0, row=0, sticky=(N, S, E, W))
    self.container1.columnconfigure(0, weight=2)
    self.container1.rowconfigure(0, weight=1)

    self.labelSearch = Label(self.container1, text="Searching by id")
    self.labelSearch.grid(column=0, row=0, columnspan=3, sticky=(N, S, E, W))

    self.labelId = Label(self.container1, text="Id")
    self.labelId.grid(column=0, row=1, sticky=(N,S,W,E))

    self.inputId = Entry(self.container1)
    self.inputId.grid(column=1, row=1, sticky=(E, W))

    self.buttonSearchId = Button(self.container1, text="Search")
    self.buttonSearchId["command"] = self.searchId
    self.buttonSearchId.grid(column=2, row=1, sticky=(N, S, E, W))

    for child in self.container1.winfo_children(): 
      child.grid_configure(padx=3, pady=3)

    self.container2 = Frame(master)
    self.container2.grid(column=0, row=2, sticky=(N, S, E, W))
    self.container2.columnconfigure(0, weight=2)
    self.container2.rowconfigure(0, weight=1)

    self.labelContact = Label(self.container2, text="Contact")
    self.labelContact.grid(column=0, row=0, columnspan=3)

    self.labelName = Label(self.container2, text="Name")
    self.labelName.grid(column=0, row=1, sticky=(N, S, E, W))

    self.inputName = Entry(self.container2)
    self.inputName.grid(column=1, row=1, sticky=(N, S, E, W))

    self.labelNameError = Label(self.container2, text="")
    self.labelNameError["width"] = 15
    self.labelNameError.grid(column=2, row=1, sticky=(N, S, E, W))

    self.labelNumber = Label(self.container2, text="Number")
    self.labelNumber.grid(column=0, row=2, sticky=(N, S, E, W))

    self.inputNumber = Entry(self.container2)
    self.inputNumber.grid(column=1, row=2, sticky=(N, S, E, W))

    self.labelNumberError = Label(self.container2, text="")
    self.labelNumberError["width"] = 15
    self.labelNumberError.grid(column=2, row=2, sticky=(N, S, E, W))

    self.labelEmail = Label(self.container2, text="Email")
    self.labelEmail.grid(column=0, row=3, sticky=(N, S, E, W))

    self.inputEmail = Entry(self.container2)
    self.inputEmail.grid(column=1, row=3, columnspan=2, sticky=(N, S, E, W))

    self.labelEmailError = Label(self.container2, text="")
    self.labelEmailError["width"] = 15
    self.labelEmailError.grid(column=2, row=3, sticky=(N, S, E, W))

    for child in self.container2.winfo_children(): 
      child.grid_configure(padx=1, pady=1)

    self.container3 = Frame(master)
    self.container3.grid(column=0, row=5, sticky=(N, W, E, S))
    self.container2.columnconfigure(0, weight=2)
    self.container2.rowconfigure(0, weight=1)

    self.buttonInsert = Button(self.container3, width=10, text="Inserir")
    self.buttonInsert["command"] = self.insert
    self.buttonInsert.grid(column=1, row=3, sticky=(E))

    self.buttonRemove = Button(self.container3, width=10, text="Remover")
    self.buttonRemove["command"] = self.delete
    self.buttonRemove.grid(column=2, row=3, sticky=(W))

    self.buttonAlter = Button(self.container3, width=10, text="Alterar")
    self.buttonAlter["command"] = self.alter
    self.buttonAlter.grid(column=3, row=3, sticky=(W))

    self.buttonReport = Button(self.container3, width=10, text="Relatório")
    self.buttonReport["command"] = self.report
    self.buttonReport.grid(column=4, row=3, sticky=(W))

    for child in self.container3.winfo_children(): 
      child.grid_configure(padx=3, pady=3)
  
  def searchId(self):
    #validate(self)
    print(self.inputId.get())

  
  def insert():
    print("Insert")
  
  def delete():
    print("Delete")
  
  def alter():
    print("Alter")
  
  def report():
    print("Report")

root = Tk()
root.title("Agenda")

myApp = Application(root)

myApp.mainloop()
