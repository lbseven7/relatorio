import sqlite3
from contextlib import closing

DB_NAME = "servicos.db"

def criar_tabela_servicos():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS servicos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Empresa TEXT,
            Servico TEXT,
            Data TEXT,
            Setor TEXT,
            Quantidade INTEGER,
            Ativo INTEGER DEFAULT 1
        )""")
        conn.commit()

def inserir_servico(empresa, servico, data, setor, quantidade):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO servicos (Empresa, Servico, Data, Setor, Quantidade) 
            VALUES (?, ?, ?, ?, ?)
        """, (empresa, servico, data, setor, quantidade))
        conn.commit()

def atualizar_servico(id, empresa, servico, data, setor, quantidade):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE servicos
            SET Empresa = ?, Servico = ?, Data = ?, Setor = ?, Quantidade = ?
            WHERE ID = ?
        """, (empresa, servico, data, setor, quantidade, id))
        conn.commit()

def excluir_servico(id):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE servicos SET Ativo = 0 WHERE ID = ?", (id,))
        conn.commit()

def consultar_servicos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM servicos ORDER BY id ASC")
    dados = cursor.fetchall()
    conn.close()
    return dados
    # ESTAVA TRAZENDO SOMENTE DO ID 5 EM DIANTE NO DATAFRAME - RESOLVIDO COM O ORDER BY ID ASC
