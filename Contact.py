from Database import Database

class Contact(object):

  def __init__(self, idContact = 0, name = "", number = "", email = ""):
    self.info = {}
    self.idContact = idContact
    self.name = name
    self.number = number
    self.email = email

  def insertContact(self):
    db = Database()

    try:
      c = db.conexao.cursor()

      c.execute("""
      INSERT INTO contacts (name, number, email) VALUES (?, ?, ?)""",
      (self.name, self.number, self.email))

      db.conexao.commit()
      c.close()

      return "Registered with success!"
    except:
      return "Something went wrong."

  def updateContact(self):
    db = Database()

    try:
      c = db.conexao.cursor()

      c.execute("""
            UPDATE contacts
            SET name = (?), number = (?), email = (?)
            WHERE id = (?)""",
        (self.name, self.number, self.email, self.idContact))

      db.conexao.commit()
      c.close()

      return "Contact succesfuly updated."
    except:
      return "Something went wrong."
  
  def deleteContact(self):
    db = Database()

    # try:
    c = db.conexao.cursor()
    
    c.execute("""DELETE FROM contacts WHERE id = (?)""", (self.idContact))

    db.conexao.commit()
    c.close()

    #   return "Contact deleted."
    # except:
    #   return "Something went wrong."

  def searchContact(self):
    db = Database()

    try:
      c = db.conexao.cursor()

      c.execute("""
        SELECT * FROM contacts WHERE id=?;
        """, (self.idContact))

      for linha in c.fetchall():
        self.name = linha[1]
        self.number = linha[2]
        self.email = linha[3]

      c.close()
      return "Searched with success!"
    except:
      return "Something went wrong."
