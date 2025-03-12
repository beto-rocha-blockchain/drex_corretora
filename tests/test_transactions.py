import pytest
from web3 import Web3

# Configuração do Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Conecte-se ao seu nó local
w3.eth.defaultAccount = w3.eth.accounts[0]

# Teste de envio de transação simples
def test_send_transaction():
    nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)
    tx = {
        'nonce': nonce,
        'to': w3.eth.accounts[1],  # Endereço de destino
        'value': w3.toWei(0.1, 'ether'),  # Valor em Ether
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei')
    }

    # Assine e envie a transação
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=w3.eth.accounts[0])
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Verifique se a transação foi confirmada
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    assert tx_receipt.status == 1  # Status 1 significa sucesso

# Teste de saldo após transação
def test_balance_after_transaction():
    sender_balance_before = w3.eth.getBalance(w3.eth.accounts[0])
    receiver_balance_before = w3.eth.getBalance(w3.eth.accounts[1])

    # Envie uma transação
    nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)
    tx = {
        'nonce': nonce,
        'to': w3.eth.accounts[1],
        'value': w3.toWei(0.1, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei')
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key=w3.eth.accounts[0])
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    w3.eth.waitForTransactionReceipt(tx_hash)

    sender_balance_after = w3.eth.getBalance(w3.eth.accounts[0])
    receiver_balance_after = w3.eth.getBalance(w3.eth.accounts[1])

    # Verifique se o saldo foi atualizado corretamente
    assert sender_balance_after == sender_balance_before - w3.toWei(0.1, 'ether')
    assert receiver_balance_after == receiver_balance_before + w3.toWei(0.1, 'ether')
