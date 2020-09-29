import cartas

# coding: utf-8
class Jogador():

    def __init__(self, id, nome, cor):
        self.__id = id
        self.__nome = nome
        self.__pontos = 0
        self.__imagem = None
        self.__cartasMao = []
        self.__cor = cor
        self.__vivo = True

    def pegarCarta(self, carta):
        self.__cartasMao.append(carta)

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

    def morre(self):
        self.__vivo = False

    def jogar_carta(self, index):
        descarte = self.__cartasMao.pop(index)
        if isinstance(descarte, cartas.Princesa):
            self.morre()
        else:
            descarte.executar_acao()
