import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / '2 clientes.sqlite')
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_muitos(conexao, cursor, lista_dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', lista_dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome')

#inserir_registro(conexao, cursor, "Guilherme", "Guilherme@email.com")
#inserir_registro(conexao, cursor, "Erick", "Erick@email.com")
#atualizar_registro(conexao, cursor, "Eldrich", "Eldrich@email.com", 2)
#excluir_registro(conexao, cursor, 1)

lista_dados = [
    ("Guilherme","gui@email"),
    ("Chappie","cha@email"),
    ("Melanie","mel@email"),
]

#inserir_registro(conexao, cursor, lista_dados)

print(dict(recuperar_cliente(cursor, 5)))
print(list(listar_clientes(cursor)))