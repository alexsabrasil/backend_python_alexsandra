import sqlite3
from sqlite3 import Connection
from typing import List, Tuple

DB_NAME = "livros.db"

def conectar() -> Connection:
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    # tabela de livros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL UNIQUE,
            titulo TEXT NOT NULL
        );
    """)
    # tabela de usuarios (desafio)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

# funções utilitárias simples (opcionais)
def executar(query: str, params: Tuple = ()):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def consultar(query: str, params: Tuple = ()) -> List[Tuple]:
    conn = conectar()
    cur = conn.cursor()
    cur.execute(query, params)
    resultados = cur.fetchall()
    conn.close()
    return resultados