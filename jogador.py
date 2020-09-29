import cartas

# coding: utf-8
class Jogador():

    def __init__(self, id, nome, cor, mesa):
        self.__id = id
        self.__nome = nome
        self.__pontos = 0
        self.__imagem = None
        self.__cartasMao = []
        self.__cor = cor
        self.__vivo = True
        self.__protected = False

    def setMesa(self, mesa):
        self.__mesa = mesa

    def receberCarta(self, carta):
        self.__cartasMao.append(carta)

    def addPontos(self, p):
        self.__pontos += p

    def getCartaMao(self):
        return self.__cartasMao[0]

    def getCartasMao(self):
        return self.__cartasMao

    def get_vivo(self):
        return self.__vivo

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getPontos(self):
        return self.__pontos

    def getCor(self):
        return self.__cor

    def get_hand(self):
        return self.__cartasMao

    def set_hand(self, nova_mao):
        self.__cartasMao = nova_mao

    def get_mesa(self):
        return self.__mesa

    def morre(self):
        self.__vivo = False

    def darProtecao(self):
        self.__protected = True

    def tirarProtecao(self):
        self.__protected = False

    def discard(self):
        self.__mesa.jogarCartaFora(__cartasMao.pop())

    def jogar_carta(self, index):
        if isinstance(__cartasMao[index], cartas.Rei) or isinstance(__cartasMao[index], cartas.Princepe):
            if isinstance(__cartasMao[(index+1)%2], cartas.Condessa):
                return False
        descarte = self.__cartasMao.pop(index)
        self.__mesa.jogarCartaFora(descarte)
        if isinstance(descarte, cartas.Princesa):
            self.morre()
        else:
            descarte.executar_acao()
        return True
