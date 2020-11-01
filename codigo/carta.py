# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador

class Carta():

    def __init__(self, valor, nome, im_verso, im_frente):
        self.__valor = valor
        self.__nome = nome
        self.__im_verso = im_verso
        self.__im_frente = im_frente
        self.__jogador = None

    def set_controleJogo(self, controle):
        self.__controleJogo = controle

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def set_jogador(self, jogador):
        self.__jogador = jogador

    def get_jogador(self):
        return self.__jogador

    def executar_acao(self, j_origem, j_alvo, valor): pass

    def getFraseInicio(self): return ""

class Guarda(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(1, 'Guarda', im_verso, im_frente)

    def acuse(self, j_alvo, card_valor):
        if j_alvo.getCartasMao()[0].get_valor() == card_valor:
            return True
        return False

    def executar_acao(self, j_origem, j_alvo, valor):
        return self.acuse(j_alvo, valor)

    def getFraseInicio(self):
        return "acusar"

class Padre(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(2, 'Padre', im_verso, im_frente)

    def see_hand(self, jogador):
        return jogador.getCartasMao()[0]

    def executar_acao(self, j_origem, j_alvo, valor):
        return self.see_hand(j_alvo)

    def getFraseInicio(self):
        return "ver mao"


class Barao(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(3, 'Barão', im_verso, im_frente)

    def compare_hands(self, j_origem, j_alvo):
        valor_origem = j_origem.getCartasMao()[0].get_valor()
        valor_alvo = j_alvo.getCartasMao()[0].get_valor()
        if valor_origem < valor_alvo:
            return j_origem
        elif valor_origem > valor_alvo:
            return j_alvo
        else:
            return None

    def executar_acao(self, j_origem, j_alvo, valor):
        return self.compare_hands(j_origem, j_alvo)

    def getFraseInicio(self):
        return "comparar as maos"

class Aia(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(4, 'Aia', im_verso, im_frente)

    def executar_acao(self, j_origem, j_alvo, valor):
        j_origem.darProtecao()
        return j_origem
    
class Principe(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(5, 'Príncipe', im_verso, im_frente)

    def executar_acao(self, j_origem, j_alvo, valor):
        return j_alvo

    def getFraseInicio(self):
        return "pegar nova mao"

class Rei(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(6, 'Rei', im_verso, im_frente)

    def trade_cards(self, j_origem, j_alvo):
        temp = j_origem.getCartasMao()
        j_origem.setCartasMao(j_alvo.getCartasMao())
        j_alvo.setCartasMao(temp)

    def executar_acao(self, j_origem, j_alvo, valor):
        self.trade_cards(j_origem, j_alvo)
        return j_alvo
        
    def getFraseInicio(self):
        return "trocarem as maos"

class Condessa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(7, 'Condessa', im_verso, im_frente)

class Princesa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(8, 'Princesa', im_verso, im_frente)

    def executar_acao(self, j_origem, j_alvo, valor):
        return j_origem


### PREMIUM EDITION - caso decidamos implementar essas classe###
#
#class Assassino(Carta):
#
#class Bobo(Carta):
#
#class Cardeal(Carta):
#
#class Baronesa(Carta):
#
#class Bajulador(Carta):
#
#class Conde(Carta):
#
#class Polícia(Carta):
#
#class Consorte(Carta):
#
#class Bispo(Carta):
#    