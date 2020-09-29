# coding: utf-8
from random import shuffle
from jogador import *
from cartas import *

class Mesa():

    def __init__(self, id):
        self.__id = id
        self.__maxPontos = 3
        self.__jogadores = []
        # teste
        for i in range(5):
            self.addJogador(Jogador(i, 'nome'+str(i), 0, self))
        self.__jogadorTurno = None
        self.__partidaIniciada = False
        self.__deck = self.__criarDeck()
        self.__lixo = []
        self.iniciarPartida()
    
    def iniciarPartida(self):
        self.__embaralharDeck()
        self.__distribuirCartas()
        self.__jogadorTurno = self.__jogadores[0]
        # teste
        for j in self.__jogadores:
            print(j.getCartaMao().get_nome())

    def passarTurno(self):
        ultimo_i = self.__jogadores.index(self.__jogadorTurno)
        proximo_i = -1
        qtdJogadores = len(self.__jogadores)
        for i in range(1, qtdJogadores):
            index = (ultimo_i + i) % qtdJogadores
            if self.__jogadores[index].get_vivo():
                proximo_i = index
        # todos os outros jogadores mortos
        if proximo_i == -1:
            self.__fimPartida()
        # proximo jogador vivo
        else:
            self.__jogadorTurno = self.__jogadores[proximo_i]
            self.__acaoTurno()

    def __acaoTurno(self):
        self.__jogadorTurno.toggle()


    def __fimPartida(self):
        algumVivo = False
        for j in self.__jogadores:
            if j.get_vivo():
                algumVivo = True
                print('vitoria de')
                print(j.getNome())
                #j.addPonto()
                if j.getPontos() == self.__maxPontos:
                    print('final do game')
        if not algumVivo:
            print('ngm venceu esse round')

        
        

    def addJogador(self, jogador):
        self.__jogadores.append(jogador)

    def pegarCarta(self, jogador):
        if len(self.__deck) > 0:
            jogador.pegarCarta(self.__deck.pop(0))
        else:
            self.__fimPartidaCompararCartas()

    def __fimPartidaCompararCartas(self):
        valor_maior = -1
        jogador_maior = None
        for j in self.__jogadores:
            if j.get_vivo():
                valor = j.getCartaMao().get_valor()
                if valor > valor_maior:
                    valor_maior = valor
                    # mata o antigo maior
                    if jogador_maior != None: jogador_maior.morre()
                    jogador_maior = j
                elif valor == valor_maior:
                    # mata ambos
                    jogador_maior.morre()
                    j.morre()
                else:
                    j.morre()
        self.__fimPartida()

    def jogarCartaFora(self, carta):
        self.__lixo.append(carta)

    def __embaralharDeck(self):
        shuffle(self.__deck)

    def __distribuirCartas(self):
        for j in self.__jogadores: j.pegarCarta(self.__deck.pop(0))

    def __criarDeck(self):
        deck = []
        # Guarda
        for _ in range(5):
            deck.append(Guarda(None, None))
        # Padre
        for _ in range(2):
            deck.append(Padre(None, None))
        # Barao
        for _ in range(2):
            deck.append(Barao(None, None))
        # Aia
        for _ in range(2):
            deck.append(Aia(None, None))
        # Principe
        for _ in range(2):
            deck.append(Principe(None, None))
        # Rei
        for _ in range(1):
            deck.append(Rei(None, None))
        # Condessa
        for _ in range(1):
            deck.append(Condessa(None, None))
        # Princesa
        for _ in range(1):
            deck.append(Princesa(None, None))
        return deck

    def getId(self):
        return self.__id

Mesa(1)