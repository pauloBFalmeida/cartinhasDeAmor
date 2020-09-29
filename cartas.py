import jogador

class Carta:

    def __init__(self, valor, nome, im_verso, im_frente):
        self.__valor = valor
        # desnecessario ;-;
        self.__nome = nome
        self.__im_verso = im_verso
        self.__im_frente = im_frente

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def executar_acao():

# class Mensagem:
#
#     def __init__(self, origem, cor, texto):
#         # ID do jogador que enviou
#         self.origem = origem
#         self.cor = cor
#         # corpo da mensagem
#         self.texto = texto

class Guarda(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(1, 'Guarda', im_verso, im_frente)

    def acuse(jogador, card_type):
        if isinstance(jogador.get_hand()[0],card_type):
            jogador.morre()
            return True
        return False

class Padre(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(2, 'Padre', im_verso, im_frente)

    def see_hand(jogador):
        return jgoador.get_hand()[0]


class Barao(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(3, 'Barão', im_verso, im_frente)

    def compare_hands(j_origem, j_alvo):
        if j_origem.get_hand()[0].get_valor() == j_alvo.get_hand()[0].get_valor():
            return False
        elif j_origem.get_hand()[0].get_valor() > j_alvo.get_hand()[0].get_valor():
            j_alvo.morre()
            return True
        else:
            j_origem.morre()
            return True


class Aia(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(4, 'Aia', im_verso, im_frente)

class Principe(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(5, 'Príncipe', im_verso, im_frente)

class Rei(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(6, 'Rei', im_verso, im_frente)

class Condessa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(8, 'Condessa', im_verso, im_frente)

class Princesa(Carta):

    def __init__(self, im_verso, im_frente):
        super().__init__(9, 'Princesa', im_verso, im_frente)
