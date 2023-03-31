from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableView, QLineEdit
from PyQt5.QtWidgets import QApplication
import sys
import auxiliar


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 300
        self.left = 1000
        self.largura = 800
        self.altura = 700
        self.elementos()
        self.carregar_janela()

    def carregar_janela(self):
        self.setFixedSize(self.largura, self.altura)
        self.setStyleSheet(f"QMainWindow{{background-color: rgb(125, 166, 184);border: 0px}}")
        self.setGeometry(self.left, self.topo, self.largura, self.altura)
        self.show()

    def elementos(self):
        self.criar = QPushButton("criar",self)
        self.criar.move(120,600)
        self.criar.resize(150,60)
        self.criar.setStyleSheet("QPushButton{padding: 15%;background-color: rgb(124, 169, 242);color: BLACK;font-size:22px;}")
        self.criar.clicked.connect(self.criar_materia)

        self.marcarx = QPushButton("marcar x",self)
        self.marcarx.move(320,600)
        self.marcarx.resize(150,60)
        self.marcarx.setStyleSheet("QPushButton{padding: 15%;background-color: rgb(124, 169, 242);color: BLACK;font-size:22px;}")
        self.marcarx.clicked.connect(self.marcar_materia)

        self.desmarcax = QPushButton("desmarcar x",self)
        self.desmarcax.move(520,600)
        self.desmarcax.resize(150,60)
        self.desmarcax.setStyleSheet("QPushButton{padding: 15%;background-color: rgb(124, 169, 242);color: BLACK;font-size:22px;}")
        self.desmarcax.clicked.connect(self.desmarcar_materia)

        self.txt1 = QLineEdit("Nome:",self)
        self.txt1.move(180,560)
        self.txt1.resize(120,30)
        self.txt1.setEnabled(False)

        self.nome = QLineEdit(self)
        self.nome.move(320,560)
        self.nome.resize(300,30)

        self.aux = auxiliar.Materias()
        self.aux.criar_tabela()

        self.criaTabela()

    def criar_materia(self):
        self.aux.inserir_materia(self.nome.text(),"",self.tabela.currentIndex().siblingAtColumn(0).data())
        self.preenche()

    def marcar_materia(self):
        self.aux.marcar_materia(self.tabela.currentIndex().siblingAtColumn(0).data())
        self.preenche()

    def desmarcar_materia(self):
        self.aux.desmarcar_materia(self.tabela.currentIndex().siblingAtColumn(0).data())
        self.preenche()

    def criaTabela(self):
        self.tabela = QTableView(self)
        self.tabela.move(160, 50)
        self.tabela.resize(475, 500)
        self.preenche()

    def preenche(self):
        lista = self.aux.listar_materias()
        self.model = auxiliar.Tabela(lista)
        self.tabela.setModel(self.model)
        self.tabela.reset()


app = QApplication(sys.argv)
tela = Tela()
app.exec()