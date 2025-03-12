import pytest
from web3 import Web3
from eth_account import Account
from app import verificar_login, login_usuario  # Importe as funções do seu código

# Teste para verificar se a chave privada é válida
def test_verificar_login_valido():
    chave_privada = "0x4c0883a69102937d6231471b5a0f61e9db0cfd4892067c205deaa7d1b8316b004"  # Exemplo de chave privada
    valido, endereco = verificar_login(chave_privada)
    assert valido is True
    assert Web3.isAddress(endereco)

# Teste para verificar se a chave privada inválida retorna erro
def test_verificar_login_invalido():
    chave_privada = "0x1234"  # Chave privada inválida
    valido, mensagem = verificar_login(chave_privada)
    assert valido is False
    assert "chave privada inválida" in mensagem

# Teste para o endpoint de login (simulando API com Flask)
def test_login_usuario():
    chave_privada = "0x4c0883a69102937d6231471b5a0f61e9db0cfd4892067c205deaa7d1b8316b004"
    response = login_usuario(chave_privada)
    assert response.status_code == 200
    assert "endereco" in response.get_json()

    # Teste de chave inválida
    chave_privada_invalida = "0x1234"
    response = login_usuario(chave_privada_invalida)
    assert response.status_code == 400
    assert "mensagem" in response.get_json()
