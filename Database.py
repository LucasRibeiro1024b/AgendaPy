import sqlite3
import os

class Database():
  def __init__(self):
    self.conexao = sqlite3.connect("base.db")
    self.create_table()

  def create_table(self):
    c = self.conexao.cursor()

    folder = os.getcwd()
    dbFile = 'base.db'
    address = os.listdir(folder)

    if dbFile not in address:
      c.execute("""
        CREATE TABLE Contatos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero TEXT NOT NULL,
            email TEXT NOT NULL
        );
      """)
      self.conexao.commit()

    c.close()