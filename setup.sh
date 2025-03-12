#!/bin/bash

# Instalar dependências do Python
echo "Instalando dependências do Python..."
pip install -r requirements.txt

# Instalar dependências do Node.js (Frontend)
echo "Instalando dependências do Node.js..."
cd frontend
npm install

# Compilar os contratos Solidity
echo "Compilando contratos Solidity..."
python ../compile_contracts.py

echo "Configuração concluída!"
