import sqlite3
import os

class Database():
  def __init__(self):
    self.conexao = sqlite3.connect("base.db")
    self.create_table()

  def create_table(self):
    c = self.conexao.cursor()

    c.execute("""
      CREATE TABLE IF NOT EXISTS contacts (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          number TEXT NOT NULL,
          email TEXT NOT NULL
      );
    """)
    self.conexao.commit()

    c.close()