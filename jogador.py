# coding: utf-8
class Jogador():

    def __init__(self, id, nome, cor):
        self.__id = id
        self.__nome = nome
        self.__pontos = 0
        self.__imagem = None
        self.__cartasMao = []
        self.__cor = cor

    def pegarCarta(self, carta):
        self.__cartasMao.append(carta)

    
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getPontos(self):
        return self.__pontos

    def getCor(self):
        return self.__cor