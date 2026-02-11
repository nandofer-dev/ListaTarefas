import sqlite3
from datetime import datetime

class TarefaModel:
    def __init__(self, db_name='tarefas.db'):
        self.db_name = db_name

        # Configuração para permitir múltiplas threads no Flask
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        query = """
    CREATE TABLE IF NOT EXISTS tarefas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia TEXT NOT NULL,
    tipo_atividade TEXT NOT NULL,
    descricao TEXT,
    data_prazo DATETIME NOT NULL,
    status TEXT DEFAULT 'Pendente',
    )
    """
        self.cursor.execute(query)
        self.conn.commit()