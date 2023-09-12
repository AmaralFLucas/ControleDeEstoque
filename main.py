import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QHBoxLayout,
                               QVBoxLayout, QTableWidget, QAbstractItemView, QPushButton, QLabel, QLineEdit, QWidget)


class EstoqueApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Controle de Estoque')
        self.setGeometry(100, 100, 800, 400)

        layout_principal = QHBoxLayout()
        layout_esquerda = QVBoxLayout()
        layout_direita = QVBoxLayout()
        layout_botoes = QHBoxLayout()

        #Tabela de produtos
        self.tbl_produtos = QTableWidget()
        #Removemos o header vertical da tabela
        self.tbl_produtos.verticalHeader().setVisible(False)
        #Marcamos que as células não serão editáveis
        self.tbl_produtos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #Definimos que ao clicar em alguma célula a linha inteira seja selecionada
        self.tbl_produtos.setSelectionBehavior(QAbstractItemView.SelectRows)
        #Adicionamos a tabela ao layout da direita
        layout_direita.addWidget(self.tbl_produtos)

        #Criação dos botões
        self.btn_cadastrar = QPushButton('Cadastrar')
        self.btn_remover = QPushButton('Remover')
        self.btn_editar = QPushButton('Editar')

        #Adicionar os botões editar e remover ao layout de botões
        layout_botoes.addWidget(self.btn_editar)
        layout_botoes.addWidget(self.btn_remover)

        #Criamos os campos para inserção dos dados e suas labels
        self.lbl_nome = QLabel('Nome do produto')
        self.txt_nome = QLineEdit()
        self.lbl_preco = QLabel('Preço do produto')
        self.txt_preco = QLineEdit()
        self.lbl_quantidade = QLabel('Quantidade em estoque')
        self.txt_quantidade = QLineEdit()
        self.lbl_data = QLabel('Data de validade')
        self.txt_data = QLineEdit()
        self.lbl_categoria = QLabel('Categoria')
        self.txt_categoria = QLineEdit()
        self.lbl_fornecedor = QLabel('Fornecedor')
        self.txt_fornecedor = QLineEdit()

        #Adicionamos os dados acima
        layout_esquerda.addWidget(self.lbl_nome)
        layout_esquerda.addWidget(self.txt_nome)
        layout_esquerda.addWidget(self.lbl_preco)
        layout_esquerda.addWidget(self.txt_preco)
        layout_esquerda.addWidget(self.lbl_quantidade)
        layout_esquerda.addWidget(self.txt_quantidade)
        layout_esquerda.addWidget(self.lbl_data)
        layout_esquerda.addWidget(self.txt_data)
        layout_esquerda.addWidget(self.lbl_categoria)
        layout_esquerda.addWidget(self.txt_categoria)
        layout_esquerda.addWidget(self.lbl_fornecedor)
        layout_esquerda.addWidget(self.txt_fornecedor)
        layout_esquerda.addWidget(self.btn_cadastrar)
        layout_esquerda.addLayout(layout_botoes)

        #Adicionamos os layouts esquerda e direita ao layout principal
        layout_principal.addLayout(layout_esquerda)
        layout_principal.addLayout(layout_direita)
        #Adicionar os layouts à janela principal
        central_widget = QWidget()
        central_widget.setLayout(layout_principal)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EstoqueApp()
    window.show()
    sys.exit(app.exec())