import pytest
from web3 import Web3
from solcx import compile_standard
from web3.middleware import geth_poa_middleware

# Configure o Web3 e a conexão com o nó (RPC)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Substitua pelo seu nó Ethereum local
w3.middleware_stack.inject(geth_poa_middleware, layer=0)

# Compilando o contrato Solidity para obter o bytecode
def compile_contract(source):
    compiled = compile_standard({
        "language": "Solidity",
        "sources": {
            "DrexAuth.sol": {
                "content": source
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "evm.bytecode"]
                }
            }
        }
    })
    return compiled['contracts']['DrexAuth.sol']['DrexAuth']

# Teste para o contrato de autenticação (DrexAuth)
def test_deploy_drex_auth():
    with open('contracts/DrexAuth.sol', 'r') as file:
        contract_source = file.read()
    
    compiled_contract = compile_contract(contract_source)
    bytecode = compiled_contract['evm']['bytecode']['object']
    abi = compiled_contract['abi']

    # Crie o contrato
    DrexAuth = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = DrexAuth.constructor().transact({'from': w3.eth.accounts[0]})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    assert tx_receipt.status == 1  # 1 significa sucesso

# Teste para verificar uma função do contrato (exemplo de função)
def test_function_in_contract():
    with open('contracts/DrexAuth.sol', 'r') as file:
        contract_source = file.read()
    
    compiled_contract = compile_contract(contract_source)
    bytecode = compiled_contract['evm']['bytecode']['object']
    abi = compiled_contract['abi']

    DrexAuth = w3.eth.contract(abi=abi, bytecode=bytecode)
    contract_address = w3.toChecksumAddress("0x...")  # Insira o endereço do contrato implantado
    contract_instance = w3.eth.contract(address=contract_address, abi=abi)

    # Teste se a função 'getUser' (exemplo) retorna o valor esperado
    user_info = contract_instance.functions.getUser().call()
    assert user_info == {"address": "0x..."}  # Exemplo de resposta esperada
