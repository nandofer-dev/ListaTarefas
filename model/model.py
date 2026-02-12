import sqlite3
from datetime import datetime

class TarefaModel:
    def __init__(self, db_name='tarefas.db'):
        self.db_name = db_name

        # Configuração para permitir múltiplas threads no Flask
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    # FUNCIONALIDADES DO BANCO DE DADOS
    def criar_tabela(self):
        query = """
    CREATE TABLE IF NOT EXISTS tarefas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    materia TEXT NOT NULL,
    tipo_atividade TEXT NOT NULL,
    descricao TEXT,
    data_prazo DATETIME NOT NULL,
    status TEXT DEFAULT 'Pendente'
    )
    """
        self.cursor.execute(query)
        self.conn.commit()


    def listar_tarefas(self):
        try:
            # 1. Prepara a busca (SELECT * busca todas as colunas)
            query = "SELECT * FROM tarefas"
            self.cursor.execute(query)

            # 2. Pega todos os resultados e transforma em uma lista do Python
            tarefas = self.cursor.fetchall()

            return tarefas

        except Exception as e:
            print("Erro ao listar tarefas:", e)
            return []

    def adicionar_tarefa(self, materia, tipo_atividade, descricao, data_prazo):
        try:
            # O status começa como 'Pendente'
            status = "Pendente"

            # 1. A Query SQL usando placeholders (?) para segurança
            query = "INSERT INTO tarefas (materia, tipo_atividade, descricao, data_prazo, status) VALUES (?, ?, ?, ?, ?)"

            # 2. Executando e passando os valores como uma tupla
            self.cursor.execute(query, (materia, tipo_atividade, descricao, data_prazo, status))

            #. Confirmar a gravação no arquivo
            self.conn.commit()

            return True
        except Exception as e:
            print("Erro ao adicionar tarefa:", e)
            return False
        
    def excluir_tarefa(self, tarefa_id):
        try:
            # 1. A Query SQL para deletar baseado no ID único.
            query = "DELETE FROM tarefas WHERE id = ?"

            # 2. Executa passando o ID da tarefa que deseja remover
            self.cursor.execute(query, (tarefa_id,))

            # 3. Confirma a remoção definitiva do banco
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print(f"[!] Aviso: Nenhuma tarefa encontrada com o ID {tarefa_id}")
                return False
            return True
            
        except Exception as e:
            print("Erro ao excluir tarefa:", e)