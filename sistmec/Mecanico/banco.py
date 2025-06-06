import sqlite3

class Banco:
    def __init__(self, db_name='mecanico.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS servicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                problema TEXT NOT NULL,
                valor REAL NOT NULL,
                data TEXT NOT NULL,
                status TEXT NOT NULL
            );
        """)
        self.conn.commit()

    def inserir_servico(self, cliente, problema, valor, data, status):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO servicos (cliente, problema, valor, data, status)
            VALUES (?, ?, ?, ?, ?);
        """, (cliente, problema, valor, data, status))
        self.conn.commit()

    def listar_servicos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM servicos")
        return cursor.fetchall()

    def atualizar_servico(self, id_, cliente, problema, valor, data, status):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE servicos
            SET cliente=?, problema=?, valor=?, data=?, status=?
            WHERE id=?;
        """, (cliente, problema, valor, data, status, id_))
        self.conn.commit()

    def remover_servico(self, id_):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM servicos WHERE id=?;", (id_,))
        self.conn.commit()
