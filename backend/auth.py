from eth_account import Account
from web3 import Web3
from flask import jsonify
from db import registrar_usuario, verificar_chave_privada, buscar_usuario
import json

# Função para verificar a chave privada do usuário e fazer o login
def verificar_login(chave_privada):
    """
    Função que verifica se a chave privada fornecida é válida e retorna o endereço correspondente.
    """
    try:
        # Criação da conta a partir da chave privada
        conta = Account.from_key(chave_privada)
        endereco = conta.address
        
        # Verifica se a chave privada está registrada no banco de dados
        usuario = verificar_chave_privada(chave_privada)
        if usuario:
            return True, endereco
        else:
            return False, "Chave privada inválida ou não registrada."
    except Exception as e:
        return False, str(e)


# Função para realizar o login usando a chave privada
def login_usuario(chave_privada):
    """
    Função que realiza o login do usuário a partir da chave privada.
    """
    # Verifica se a chave privada é válida e registrada no banco
    valido, resultado = verificar_login(chave_privada)
    
    if valido:
        return jsonify({"status": "sucesso", "endereco": resultado}), 200
    else:
        return jsonify({"status": "erro", "mensagem": resultado}), 400

# Função para registrar um novo usuário (Criar uma nova conta)
def registrar_usuario_api(nome, email):
    """
    Função que cria uma nova carteira e registra o usuário no banco de dados.
    """
    nova_conta = Account.create()
    endereco = nova_conta.address
    chave_privada = nova_conta.key.hex()

    # Registra o novo usuário no banco de dados
    registrar_usuario(endereco, chave_privada, nome, email)

    return jsonify({
        "status": "sucesso",
        "endereco": endereco,
        "chave_privada": chave_privada
    }), 200
