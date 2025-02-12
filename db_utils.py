import sqlite3
from contextlib import closing
from datetime import datetime

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
        cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Descricao TEXT,
            Funcionario TEXT,
            Data TEXT
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS funcionarios (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            Cargo TEXT,
            Setor TEXT           
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

def consultar_servicos(ativo=1):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        query = "SELECT * FROM servicos WHERE Ativo = ?" if ativo is not None else "SELECT * FROM servicos"
        return conn.execute(query, (ativo,)).fetchall()

def adicionar_tarefas():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        return [{"ID": row[0], "Descrição": row[1], "Funcionário": row[2], "Data": row[3]} for row in tarefas]

def inserir_tarefa(descricao, funcionario):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tarefas (Descricao, Funcionario, Data) 
            VALUES (?, ?, ?)
        """, (descricao, funcionario, datetime.now().strftime("%d-%m-%Y | %H:%M:%S")))
        conn.commit()