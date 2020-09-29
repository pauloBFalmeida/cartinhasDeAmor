# coding: utf-8
from random import shuffle
from jogador import *
from cartas import *

class Mesa():

    def __init__(self, id):
        self.__id = id
        self.__jogadores = []
        # teste
        for i in range(5):
            self.addJogador(Jogador(i, 'nome'+str(i), 0, self))

        self.__jogadorTurno = None
        self.__partidaIniciada = False
        self.__deck = self.__criarDeck()
        self.__lixo = []
        self.__embaralhar()
        self.__distribuirCartas()
        self.iniciarPartida()
        # teste
        for j in self.__jogadores:
            print(j.getCartaMao().get_nome())

    
    def iniciarPartida(self):
        self.__jogadorTurno = self.__jogadores[0]

    def passarTurno(self):
        ultimo_i = self.__jogadores.index(self.__jogadorTurno)
        proximo_i = -1
        qtdJogadores = len(self.__jogadores)
        for i in range(1, qtdJogadores):
            index = (ultimo_i + i) % qtdJogadores
            if self.__jogadores[index].get_vivo():
                proximo_i = index
        if proximo_i == -1:
            self.__fimPartida()
        else:
            self.__jogadorTurno = self.__jogadores[proximo_i]


    def addJogador(self, jogador):
        self.__jogadores.append(jogador)

    def __fimPartida(self):
        print('final')


    def __embaralhar(self):
        shuffle(self.__deck)

    def pegarCarta(self, jogador):
        if len(self.__deck) > 0:
            jogador.pegarCarta(self.__deck.pop(0))
        else:
            # jogador com o valor mais alto ganha
            pass

    def jogarCartaFora(self, carta):
        self.__lixo.append(carta)

    def __distribuirCartas(self):
        for j in self.__jogadores:
            j.pegarCarta(self.__deck.pop(0))

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