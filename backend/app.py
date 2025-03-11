from flask import Flask, request, jsonify, send_from_directory
from web3 import Web3
from eth_account import Account
import json
import os
from auth import login_usuario, registrar_usuario  # Importando as funções de auth.py

app = Flask(__name__, static_folder='static')

# Conectar ao nó Ethereum local (Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Função para criar carteira
def criar_carteira():
    nova_conta = Account.create()
    endereco = nova_conta.address
    chave_privada = nova_conta.key.hex()
    return endereco, chave_privada

# Rota para a criação de carteira
@app.route('/criar_carteira', methods=['POST'])
def criar_carteira_api():
    endereco, chave_privada = criar_carteira()
    return jsonify({"endereco": endereco, "chave_privada": chave_privada}), 200

# Rota para login de usuário - Chamando a função do auth.py
@app.route('/login', methods=['POST'])
def login():
    chave_privada = request.json.get('chave_privada')
    return login_usuario(chave_privada)

# Rota para registrar novo usuário - Chamando a função do auth.py
@app.route('/registrar', methods=['POST'])
def registrar():
    return registrar_usuario()

# Rota para servir o frontend HTML
@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
