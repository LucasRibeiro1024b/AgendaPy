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

    #The reason for a hidden id is because cleanInputs() is cleaning the id input and I can't get it to delete a contact, so I'm gonna store the previous id searched and use it in my delete method.
    self.hiddenId = 0

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
    self.container3.columnconfigure(0, weight=2)
    self.container3.rowconfigure(0, weight=1)

    self.buttonInsert = Button(self.container3, width=10, text="Insert")
    self.buttonInsert["command"] = self.insert
    self.buttonInsert.grid(column=1, row=3, sticky=(E))

    self.buttonRemove = Button(self.container3, width=10, text="Delete")
    self.buttonRemove["command"] = self.delete
    self.buttonRemove.grid(column=2, row=3, sticky=(W))

    self.buttonAlter = Button(self.container3, width=10, text="Update")
    self.buttonAlter["command"] = self.update
    self.buttonAlter.grid(column=3, row=3, sticky=(W))

    self.buttonReport = Button(self.container3, width=10, text="Contacts")
    self.buttonReport["command"] = self.report
    self.buttonReport.grid(column=4, row=3, sticky=(W))

    for child in self.container3.winfo_children(): 
      child.grid_configure(padx=3, pady=3)
    
    self.container4 = Frame(master)
    self.container4.grid(column=0, row=6, sticky=(N, S, E, W))
    self.container4.columnconfigure(0, weight=2)
    self.container4.rowconfigure(0, weight=1)

    self.labelResult = Label(self.container4, text="")
    self.labelResult.grid(column=0, row=0, columnspan=3)
    
  
  def searchId(self):
    ct = Contact()
    ct.idContact = self.inputId.get()
    self.hiddenId = self.inputId.get()

    self.labelResult["text"] = ct.searchContact()

    self.cleanInputs()

    self.inputName.insert(INSERT, ct.name)
    self.inputNumber.insert(INSERT, ct.number)
    self.inputEmail.insert(INSERT, ct.email)
  
  def insert(self):
    if (self.validateInputs()):
      ct = Contact()
      ct.name = self.inputName.get()
      ct.number = self.inputNumber.get()
      ct.email = self.inputEmail.get()

      self.labelResult["text"] = ct.insertContact()
      
      self.cleanInputs()
    else:
      self.labelResult["text"] = "Invalid inputs."

  
  def delete(self):
    ct = Contact()
    ct.idContact = self.hiddenId
    self.labelResult["text"] = ct.deleteContact()
  
  def update(self):
    if (self.validateInputs()):
      ct = Contact()
      ct.name = self.inputName.get()
      ct.number = self.inputNumber.get()
      ct.email = self.inputEmail.get()
      ct.idContact = self.hiddenId

      self.labelResult["text"] = ct.updateContact()
      self.cleanInputs()
    else:
      self.labelResult["text"] = "Invalid inputs."
      
  def report(self):
    root = Tk()
    root.title("Report")
    label = Label(root, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(root, text="Okay", command = root.destroy)
    B1.pack()
    popup.mainloop()

  def validateInputs(self):
    allValid = True

    if len(self.inputName.get()) <= 40:
      self.inputName["background"] = "white"
      self.labelNameError["text"] = "OK!"
    else:
      allValid = False
      self.inputName["background"] = "red"
      self.labelNameError["text"] = "ERROR"
    
    if re.match(r'[1-9]{2}[0-9]{9}', self.inputNumber.get()) and len(self.inputNumber.get()) == 11:
      self.labelNumberError["text"] = "OK!"
      self.inputNumber["background"] = "white"
    else:
      allValid = False
      self.labelNumberError["text"] = "ERROR"
      self.inputNumber["background"] = "red"

    if re.match(r'^[a-zA-Z0-9_.-]*@\w+([\.-]?\w+)*(\.\w{2,3})+$', self.inputEmail.get()):
      self.labelEmailError["text"] = "OK!"
      self.inputEmail["background"] = "white"
    else:
      allValid = False
      self.labelEmailError["text"] = "ERROR"
      self.inputEmail["background"] = "red"

    if allValid:
      return True
    else:
      return False

  def cleanInputs(self):
    self.inputId.delete(0, END)
    self.inputName.delete(0, END)
    self.inputNumber.delete(0, END)
    self.inputEmail.delete(0, END)
    self.labelNameError["text"] = ""
    self.labelNumberError["text"] = ""
    self.labelEmailError["text"] = ""
    self.inputName["background"] = "white"
    self.inputNumber["background"] = "white"
    self.inputEmail["background"] = "white"

root = Tk()
root.title("Agenda")
root.geometry("400x280+100+210")

myApp = Application(root)

myApp.mainloop()
