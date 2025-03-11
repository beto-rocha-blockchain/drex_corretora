from solcx import compile_standard, install_solc
import os

# Verifique se o solc está instalado, caso contrário, instale-o
install_solc('0.8.0')

# Diretório contendo os contratos
contratos_dir = './contracts'

# Função para compilar os contratos Solidity
def compilar_contratos():
    contratos_compilados = {}
    
    for filename in os.listdir(contratos_dir):
        if filename.endswith(".sol"):
            contrato_path = os.path.join(contratos_dir, filename)
            with open(contrato_path, 'r') as file:
                contrato_source = file.read()

            # Compilar o contrato
            compiled = compile_standard({
                "language": "Solidity",
                "sources": {
                    filename: {
                        "content": contrato_source
                    }
                },
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ["abi", "evm.bytecode", "evm.deployedBytecode"]
                        }
                    }
                }
            }, solc_version='0.8.0')

            contratos_compilados[filename] = compiled

    # Salvar os contratos compilados em arquivos
    for contrato, data in contratos_compilados.items():
        contrato_nome = contrato.replace('.sol', '')
        output_dir = f'./compiled_contracts/{contrato_nome}'

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # ABI
        with open(f'{output_dir}/abi.json', 'w') as abi_file:
            abi_file.write(str(data['contracts'][contrato]['abi']))

        # Bytecode
        with open(f'{output_dir}/bytecode.txt', 'w') as bytecode_file:
            bytecode_file.write(data['contracts'][contrato]['evm']['bytecode']['object'])

        print(f"Contrato {contrato_nome} compilado com sucesso!")

# Executar a função de compilação
if __name__ == '__main__':
    compilar_contratos()
