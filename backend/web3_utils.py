from web3 import Web3

# Conectar-se ao nó local ou a um nó remoto (dependendo da sua configuração)
def conectar_web3():
    """
    Função para conectar ao nó Ethereum/DREX usando Web3.
    """
    # Exemplo de nó local, modifique para seu nó ou URL RPC
    url = "http://127.0.0.1:8545"  # Altere para o seu nó ou RPC se necessário
    web3 = Web3(Web3.HTTPProvider(url))

    if web3.isConnected():
        print("Conexão bem-sucedida com o nó.")
    else:
        print("Falha na conexão com o nó.")
    
    return web3


# Função para verificar o saldo de uma conta
def verificar_saldo(web3, endereco):
    """
    Função para verificar o saldo de uma conta na blockchain.
    """
    try:
        saldo = web3.eth.get_balance(endereco)  # Retorna o saldo em Wei
        saldo_eth = web3.fromWei(saldo, 'ether')  # Converte para Ether
        return saldo_eth
    except Exception as e:
        return f"Erro ao verificar saldo: {str(e)}"


# Função para enviar uma transação (transferir ETH)
def enviar_transacao(web3, chave_privada, endereco_destino, valor_eth):
    """
    Função para enviar uma transação de ETH para outra conta.
    """
    try:
        # Criação da conta a partir da chave privada
        conta = web3.eth.account.privateKeyToAccount(chave_privada)
        endereco_origem = conta.address
        
        # Convertendo o valor de Ether para Wei
        valor_wei = web3.toWei(valor_eth, 'ether')

        # Construção da transação
        transacao = {
            'to': endereco_destino,
            'from': endereco_origem,
            'value': valor_wei,
            'gas': 2000000,  # Defina o valor de gás necessário
            'gasPrice': web3.toWei('20', 'gwei'),  # Defina o preço do gás
            'nonce': web3.eth.getTransactionCount(endereco_origem),
            'chainId': 1  # Para a mainnet Ethereum, use 1. Para DREX, ajuste conforme necessário.
        }

        # Assinando a transação com a chave privada
        transacao_assinada = web3.eth.account.signTransaction(transacao, chave_privada)

        # Enviando a transação
        tx_hash = web3.eth.sendRawTransaction(transacao_assinada.rawTransaction)

        # Retorna o hash da transação
        return web3.toHex(tx_hash)
    
    except Exception as e:
        return f"Erro ao enviar transação: {str(e)}"


# Função para obter o histórico de transações (se possível)
def obter_historico_transacoes(web3, endereco):
    """
    Função para obter o histórico de transações de uma conta.
    """
    try:
        # Para obter transações, pode ser necessário usar APIs externas ou armazenar informações no contrato inteligente
        # Web3.py não tem suporte nativo para o histórico de transações, então você pode precisar de outra solução
        return f"Histórico de transações para o endereço {endereco} ainda não implementado."
    except Exception as e:
        return f"Erro ao obter histórico de transações: {str(e)}"
