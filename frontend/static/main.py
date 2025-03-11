import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from web3_interface import Web3Interface

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inicializando a interface do Web3
        self.web3_interface = Web3Interface()

        self.setWindowTitle('Corretora DREX')
        self.setGeometry(100, 100, 400, 300)

        # Layout
        self.layout = QVBoxLayout()

        # Campo de endereço e chave privada
        self.endereco_label = QLabel('Endereço:')
        self.layout.addWidget(self.endereco_label)
        self.endereco_input = QLineEdit()
        self.layout.addWidget(self.endereco_input)

        self.chave_privada_label = QLabel('Chave Privada:')
        self.layout.addWidget(self.chave_privada_label)
        self.chave_privada_input = QLineEdit()
        self.layout.addWidget(self.chave_privada_input)

        # Botão de Login
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        # Botão para Criar Nova Carteira
        self.cadastrar_button = QPushButton('Cadastrar Nova Carteira')
        self.cadastrar_button.clicked.connect(self.registrar_usuario)
        self.layout.addWidget(self.cadastrar_button)

        # Resultados de status
        self.status_label = QLabel('')
        self.layout.addWidget(self.status_label)

        # Centralizando o layout
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def login(self):
        chave_privada = self.chave_privada_input.text()

        # Verifica o login utilizando a chave privada
        valido, mensagem = self.web3_interface.login_usuario(chave_privada)

        if valido:
            self.status_label.setText(f'Login Bem-Sucedido! Endereço: {mensagem}')
        else:
            self.status_label.setText(f'Erro: {mensagem}')

    def registrar_usuario(self):
        # Cria uma nova conta
        endereco, chave_privada = self.web3_interface.registrar_usuario()
        self.status_label.setText(f'Nova Carteira Criada!\nEndereço: {endereco}\nChave Privada: {chave_privada}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
