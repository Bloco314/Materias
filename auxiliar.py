import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class Materias:
    def criar_tabela(self):
        conn = sqlite3.connect('meubanco.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS MATERIA(nome TEXT PRIMARY KEY,marcado TEXT ,prerequisito TEXT);")

    def listar_materias(self):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM MATERIA")
            lista = [("Nome", "Marcado", "pre requisito")]
            for linha in cursor.fetchall():
                lista.append(linha)
            return lista
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return [("erro no sql")]

    def inserir_materia(self, nome, marcado, pre):
        try:
            if pre == "Nome":
                pre = None
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO MATERIA (nome, marcado, prerequisito) VALUES (?,?,?)""", (nome, marcado, pre))
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def marcar_materia(self, nome):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE MATERIA SET marcado = ? WHERE nome = ?", ("X", nome))
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False

    def desmarcar_materia(self, nome):
        try:
            conn = sqlite3.connect('meubanco.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE MATERIA SET marcado = ? WHERE nome = ?", ("", nome))
            conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            return False


class Tabela(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(Tabela, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
