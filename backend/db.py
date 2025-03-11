import sqlite3
from eth_account import Account
import os

# Função para inicializar o banco de dados
def init_db():
    """Cria a tabela de usuários e carteiras, se não existir."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    # Criação da tabela de usuários
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endereco TEXT UNIQUE,
            chave_privada TEXT UNIQUE,
            nome TEXT,
            email TEXT
        )
    ''')
    
    # Salvar e fechar a conexão com o banco
    conn.commit()
    conn.close()

# Função para registrar um novo usuário
def registrar_usuario(endereco, chave_privada, nome, email):
    """Registra um novo usuário no banco de dados."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    try:
        # Inserir o novo usuário
        c.execute('''
            INSERT INTO usuarios (endereco, chave_privada, nome, email)
            VALUES (?, ?, ?, ?)
        ''', (endereco, chave_privada, nome, email))
        
        # Salvar e fechar a conexão
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro ao registrar usuário: {e}")
        conn.rollback()
    finally:
        conn.close()

# Função para buscar um usuário pelo endereço
def buscar_usuario(endereco):
    """Busca um usuário no banco de dados pelo seu endereço."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT * FROM usuarios WHERE endereco = ?
    ''', (endereco,))
    usuario = c.fetchone()
    
    conn.close()
    return usuario

# Função para verificar a chave privada de um usuário
def verificar_chave_privada(chave_privada):
    """Verifica se a chave privada existe no banco de dados."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT * FROM usuarios WHERE chave_privada = ?
    ''', (chave_privada,))
    usuario = c.fetchone()
    
    conn.close()
    return usuario

# Função para obter todos os usuários
def obter_usuarios():
    """Retorna todos os usuários no banco de dados."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT * FROM usuarios
    ''')
    usuarios = c.fetchall()
    
    conn.close()
    return usuarios

# Função para excluir um usuário
def excluir_usuario(endereco):
    """Exclui um usuário do banco de dados pelo seu endereço."""
    conn = sqlite3.connect('carteiras.db')
    c = conn.cursor()
    
    c.execute('''
        DELETE FROM usuarios WHERE endereco = ?
    ''', (endereco,))
    
    conn.commit()
    conn.close()