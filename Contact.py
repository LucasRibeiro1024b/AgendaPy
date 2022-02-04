from Database import Database

class Contact(object):

  def __init__(self, idContato = 0, nome = "", numero = "", email = ""):
    self.info = {}
    self.idContato = idContato
    self.nome = nome
    self.numero = numero
    self.email = email

  def inserirContact(self, arg):
    db = Database()

    #try:
    c = db.conexao.cursor()

    c.execute("""
    INSERT INTO Contatos (nome, numero, email) VALUES (?, ?, ?)""",
    (self.nome, self.numero, self.email))

    db.conexao.commit()
    c.close()

    #   return "Lembrete cadastrado com sucesso!"
    # except:
    #   return "Ocorreu um erro durante a inserção do lembrete."

  def atualizarLembrete(self):
      db = Database()

      try:
          c = db.conexao.cursor()

          c.execute("UPDATE lembretes SET dataLembrete = {}, textoLembrete = {}, concluidoLembrete = {} WHERE idLembrete = {}".format(self.dataLembrete, self.textoLembrete, self.concluidoLembrete, self.idLembrete))

          db.conexao.commit()
          c.close()

          return "Atualização de lembrete concluída com sucesso!"
      except:
          return "Ocorreu um erro durante a atualização do lembrete."
  
  def deletarContact(self):
      db = Database()

      try:
          c = db.conexao.cursor()
          
          c.execute("DELETE FROM lembretes WHERE idLembrete = {}".format(self.idLembrete))

          db.conexao.commit()
          c.close()

          return "Lembrete excluído com sucesso!"
      except:
          return "Ocorreu um erro durante a exclusão do lembrete."

  def buscarContato(self):
      db = Database()

      try:
          c = db.conexao.cursor()

          c.execute("SELECT * FROM lembretes WHERE idLembrete = {}".format(self.idLembrete))

          for linha in c:
              self.idLembrete = linha[0]
              self.dataLembrete = linha[1]
              self.textoLembrete = linha[2]
              self.concluidoLembrete = linha[3]

          c.close()

          return "Busca realizada com sucesso!"
      except:
          return "Ocorreu um erro durante a busca do lembrete."
