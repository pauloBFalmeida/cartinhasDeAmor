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
            (nome TEXT,
            corR INTEGER,
            corG INTEGER,
            corB INTEGER,
            pontos INTEGER,
            PRIMARY KEY(nome)
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
            jogador = Jogador(nome=jogador_data[0], cor=(jogador_data[1], jogador_data[2], jogador_data[3]))
            return jogador
        else:
            return None

    def get_pontos_jogador(self, nome):
        jogador_data = self.read_query(
            f"""
            select * from JOGADORES where nome = '{nome}'
            """
        )
        if jogador_data != []:
            jogador_data = jogador_data[0]
            return jogador_data[4]
        else:
            return None

    def get_top_5(self):
        top_5_nome_pontos = self.c.execute(f"""
            SELECT nome, pontos from JOGADORES
            ORDER BY pontos DESC
        """
        )
        top_5_nome_pontos = self.c.fetchall()[:5]
        if top_5_nome_pontos:
            return top_5_nome_pontos
        else:
            return None

    def update_pontos(self, list_jogadores):
        for j in list_jogadores:
            self.c.execute(f"""
                UPDATE JOGADORES
                SET pontos = pontos + {j.getPontos()} where nome = '{j.getNome()}'
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
            CREATE TABLE IF NOT EXISTS MESAS
            (id INTEGER PRIMARY KEY,
            ganhador TEXT,
            pontos INTEGER,
            jog1 TEXT,
            jog2 TEXT,
            jog3 TEXT,
            jog4 TEXT,
            FOREIGN KEY(jog1) REFERENCES JOGADORES(nome)
            FOREIGN KEY(jog2) REFERENCES JOGADORES(nome)
            FOREIGN KEY(jog3) REFERENCES JOGADORES(nome)
            FOREIGN KEY(jog4) REFERENCES JOGADORES(nome)
            FOREIGN KEY(ganhador) REFERENCES JOGADORES(nome)
            )
        """)
    
    def insert_into_table(self, mesa: Mesa):
        id = self.get_size()
        jg_nome = mesa.getGanhadorDoJogo().getNome()
        pontos = mesa.getPontosPartida()
        j_list = mesa.getJogadores()
        nome_jogador = [j.getNome() for j in j_list] + [None for _ in range(len(j_list), 4)]
        try:
            self.c.execute(f"""
                INSERT INTO MESAS
                    (id, ganhador, pontos, jog1, jog2, jog3, jog4)
                VALUES(
                    ?, ?, ?, ?, ?, ?, ?
            )""", [id, jg_nome, pontos, nome_jogador[0], nome_jogador[1], nome_jogador[2] , nome_jogador[3]]
            )
        except:
            pass
        self.conn.commit()

    def read_query(self, query):
        self.c.execute(query)
        result = self.c.fetchall()
        self.conn.commit()
        return result
        
    def get_mesa_data(self, id):
        mesa_data = self.read_query(
            f"""
            select * from MESAS where id = '{id}'
            """
        )
        if mesa_data != []:
            mesa_data = mesa_data[0]
            return mesa_data
        else:
            return None

    def get_size(self):
        self.c.execute("SELECT max(id) from MESAS")
        maior = self.c.fetchone()[0]
        n = maior if maior else 0
        return n + 1

    def close(self):
        self.conn.close()