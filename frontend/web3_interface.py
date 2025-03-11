from web3 import Web3
from eth_account import Account
import json

class Web3Interface:
    def __init__(self):
        # Inicializa a conexão com o nó local da blockchain DREX (substitua pelo URL correto)
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        
        # Verifica se a conexão foi bem-sucedida
        if not self.web3.isConnected():
            raise Exception("Falha na conexão com o nó Web3!")

        # Contratos (Se necessário, carregar ABI e bytecode compilados aqui)
        self.drex_auth_contract = None
        self.token_exchange_contract = None
        self.nft_marketplace_contract = None

    def login_usuario(self, chave_privada):
        """
        Realiza o login do usuário utilizando a chave privada.
        Retorna verdadeiro se o login for bem-sucedido, e o endereço.
        """
        try:
            conta = Account.from_key(chave_privada)
            endereco = conta.address
            return True, endereco
        except Exception as e:
            return False, str(e)

    def registrar_usuario(self):
        """
        Cria uma nova conta na blockchain DREX.
        Retorna o endereço da conta e a chave privada.
        """
        nova_conta = Account.create()
        endereco = nova_conta.address
        chave_privada = nova_conta.privateKey.hex()
        return endereco, chave_privada
