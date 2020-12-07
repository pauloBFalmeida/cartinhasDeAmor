import sqlite3
from jogador import Jogador

class MapeadorJogador:
    
    def __init__(self):
        # usando sqlite para evitar ter que definir um servidor pro BD
        self.conn = sqlite3.connect('bancoDeDados.db')
        self.c = self.conn.cursor()

    def __create_table_jogadores(self):
        self.c.execute(f"""
            CREATE TABLE IF NOT EXISTS JOGADORES
            (id INTEGER PRIMARY KEY,
            nome TEXT,
            cor TEXT
            )
        """)

    def __insert_into_table(self, list_jogadores):
        for j in list_jogadores:
            self.c.execute(f"""
                INSERT INTO JOGADORES
                    (id_jogador, nome, cor)
                VALUES(
                    ?, ?, ?
                )""",
                (j.getId(), j.getNome(), j.getCor())
            )
        self.conn.commit()
        self.c.close()

    def read_query(self, query):
        self.c.execute(query)
        result = self.c.fetchall()
        self.conn.commit()
        return result

    def get_jogador(self, id):
        return self.read_query(
            f"""
            Select * from JOGADORES where id={id}
            """
        )[0]