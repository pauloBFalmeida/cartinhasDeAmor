import sqlite3
from sys import path
path.append('codigo')
from jogador import Jogador
from mesa import Mesa

class MapeadorJogador:
    
    def __init__(self):
        # usando sqlite para evitar ter que definir um servidor pro BD
        self.conn = sqlite3.connect('scoreboard.db')
        self.c = self.conn.cursor()
        self.__create_table_jogadores()

    def __create_table_jogadores(self):
        self.c.execute(f"""
            CREATE TABLE IF NOT EXISTS JOGADORES
            (id INTEGER PRIVATE KEY,
            nome TEXT UNIQUE,
            corR INTEGER,
            corG INTEGER,
            corB INTEGER,
            pontos INTEGER
            )
        """)

    def insert_into_table(self, list_jogadores):
        for j in list_jogadores:
            nome = j.getNome()
            cor = j.getCor()
            pontos = j.getPontos()
            try:
                self.c.execute(f"""
                    INSERT INTO JOGADORES
                        (nome, corR, corG, corB, pontos)
                    VALUES(
                        ?, ?, ?, ?, ?
                )""", [nome, cor[0], cor[1], cor[2] , pontos]
                )
            except:
                continue
            self.conn.commit()

    def read_query(self, query):
        self.c.execute(query)
        result = self.c.fetchall()
        self.conn.commit()
        return result

    def get_jogador(self, nome):
        jogador_data = self.read_query(
            f"""
            select * from JOGADORES where nome = '{nome}'
            """
        )
        if jogador_data != []:
            jogador_data = jogador_data[0]
            jogador = Jogador(nome=jogador_data[1], cor=(jogador_data[2], jogador_data[3], jogador_data[4]))
            return jogador
        else:
            return None

    def update_pontos(self, list_jogadores):
        for j in list_jogadores:
            self.c.execute(f"""
                UPDATE JOGADORES
                SET pontos = pontos + {j.getPontos()}
            """)
        self.conn.commit()

    def close(self):
        self.conn.close()


class MapeadorMesa:

    def __init__(self):
        # usando sqlite para evitar ter que definir um servidor pro BD
        self.conn = sqlite3.connect('scoreboard.db')
        self.c = self.conn.cursor()
        self.__create_table_mesa()
    
    def __create_table_mesa(self):
        self.c.execute(f"""
            CREATE TABLE IF NOT EXISTS JOGOS
            (id INTEGER PRIVATE KEY,
            jogadores TEXT,
            ganhador TEXT
            )
        """)
    
    def insert_into_table(self, mesa: Mesa):
        id = mesa.getId()
        jg_nome = mesa.getGanhadorDoJogo().getNome()
        j_list = mesa.getJogadores()
        jogadores = [j.getNome() for j in j_list] + ["" for _ in range(len(j_list), 4)]
        try:
            self.c.execute(f"""
                INSERT INTO JOGOS
                    (id, jg_nome, j0, j1, j2, j3)
                VALUES(
                    ?, ?, ?, ?, ?, ?
            )""", [id, jg_nome, j_list[0], j_list[1], j_list[2] , j_list[3]]
            )
        except:
            pass
        self.conn.commit()

    def get_mesa_data(self, id):
        mesa_data = self.read_query(
            f"""
            select * from JOGOS where id = '{id}'
            """
        )
        if mesa_data != []:
            mesa_data = mesa_data[0]
            return mesa_data
        else:
            return None

    def close(self):
        self.conn.close()