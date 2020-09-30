# coding: utf-8
#from carta import Carta

class Jogador():

    def __init__(self, id, nome, cor):
        self.__id = id
        self.__nome = nome
        self.__cor = cor
        self.__pontos = 0
        self.__imagem = None
        self.__cartasMao = []
        self.__vivo = True
        self.__protected = False

    def receberCarta(self, carta):
        carta.set_jogador(self)
        self.__cartasMao.append(carta)

    def addPontos(self, p):
        self.__pontos += p

    def sizeCartasMao(self):
        return len(self.__cartasMao)

    def getCartasMao(self):
        return self.__cartasMao

    def setCartasMao(self, cartas):
        self.__cartasMao = cartas

    def get_vivo(self):
        return self.__vivo

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getPontos(self):
        return self.__pontos

    def zerarPontos(self):
        self.__pontos = 0

    def getCor(self):
        return self.__cor

    def get_hand(self):
        return self.__cartasMao

    def set_hand(self, nova_mao):
        self.__cartasMao = nova_mao

    def morre(self):
        self.__vivo = False

    def set_vivo(self, v):
        self.__vivo = v

    def darProtecao(self):
        self.__protected = True

    def tirarProtecao(self):
        self.__protected = False

    def getProtecao(self):
        return self.__protected

    def limparMao(self):
        cartas = list(self.__cartasMao)
        self.__cartasMao.clear()
        return cartas

    def jogar_carta(self, index):
        carta_descarte = self.__cartasMao.pop(index)
        return carta_descarte
