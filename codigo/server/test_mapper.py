from mapper import MapeadorJogador
from sys import path
path.append('codigo')
from jogador import Jogador

def teste():
    j = Jogador(2, "Mateus", "azul")
    map = MapeadorJogador()
    map.insert_into_table([j])
    retorno = map.get_jogador('Mateus')
    print(retorno)

teste()