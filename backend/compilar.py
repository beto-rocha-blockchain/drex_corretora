from solcx import compile_standard, install_solc

# Baixar a versão específica do solc
install_solc('0.8.0')

# Ler o contrato Solidity
with open("contract/Token.sol", "r") as file:
    contrato_source = file.read()

# Compilar o contrato
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Token.sol": {
            "content": contrato_source
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

# Exibir o resultado
print(compiled_sol)

# Salvar o bytecode e ABI
bytecode = compiled_sol['contracts']['Token.sol']['Token']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['Token.sol']['Token']['abi']

with open("Token_bytecode.txt", "w") as bytecode_file:
    bytecode_file.write(bytecode)

with open("Token_abi.json", "w") as abi_file:
    import json
    json.dump(abi, abi_file)

print("Compilação completa! Bytecode e ABI salvos.")
