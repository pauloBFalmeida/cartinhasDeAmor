class Carta:

    def __init__(self,id, valor, nome, im_verso, im_frente):
        self.id = id
        self.valor = valor
        # desnecessario ;-;
        self.nome = nome
        self.im_verso = im_verso
        self.im_frente = im_frente

# class Mensagem:
#
#     def __init__(self, origem, cor, texto):
#         # ID do jogador que enviou
#         self.origem = origem
#         self.cor = cor
#         # corpo da mensagem
#         self.texto = texto

class Guarda(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 1, 'Guarda', im_verso, im_frente)

class Padre(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 2, 'Padre', im_verso, im_frente)

class Barao(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 3, 'Barão', im_verso, im_frente)

class Aia(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 4, 'Aia', im_verso, im_frente)

class Principe(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 5, 'Príncipe', im_verso, im_frente)

class Rei(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 6, 'Rei', im_verso, im_frente)

class Condessa(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 8, 'Condessa', im_verso, im_frente)

class Princesa(Carta):

    def __init__(self, id, im_verso, im_frente):
        super().__init__(id, 9, 'Princesa', im_verso, im_frente)
