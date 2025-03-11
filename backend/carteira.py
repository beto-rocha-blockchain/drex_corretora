from web3 import Web3
from eth_account import Account

# Criar uma nova carteira
def criar_carteira():
    nova_conta = Account.create()  # Gera um par de chaves
    endereco = nova_conta.address  # Endereço público da carteira
    chave_privada = nova_conta.key.hex()  # Chave privada

    print(f"🪙 Carteira criada com sucesso!")
    print(f"🔹 Endereço: {endereco}")
    print(f"🔑 Chave Privada (Guarde isso!): {chave_privada}")

    return endereco, chave_privada

# Criar e imprimir uma nova carteira
if __name__ == "__main__":
    criar_carteira()
