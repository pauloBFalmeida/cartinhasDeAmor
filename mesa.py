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
            self.addJogador(Jogador(i, 'nome'+str(i), 0))

        self.__jogadorTurno = None
        self.__partidaIniciada = False
        self.__deck = self.__criarDeck()
        self.__lixo = []
        self.__embaralhar()
        self.__distribuirCartas()
        # teste
        for j in self.__jogadores:
            print(j.getCartaMao().nome)


    
    def addJogador(self, jogador):
        self.__jogadores.append(jogador)

    def iniciarPartida(self):
        self.__jogadorTurno = self.__jogadores[0]

    def passarTurno(self):
        i = (self.__jogadores.index(self.__jogadorTurno)+1 ) % len(self.__jogadores)
        self.__jogadorTurno = self.__jogadores[i]

    def __embaralhar(self):
        shuffle(self.__deck)

    def pegarCarta(self):
        if len(self.__deck) > 0:
            self.__jogadorTurno.pegarCarta(self.__deck.pop(0))

    def jogarCartaFora(self, carta):
        self.__lixo.append(carta)

    def __distribuirCartas(self):
        for j in self.__jogadores:
            j.pegarCarta(self.__deck.pop(0))

    def __criarDeck(self):
        deck = []
        # Guarda
        for _ in range(5):
            deck.append(Guarda(1, None, None))
        # Padre
        for _ in range(2):
            deck.append(Padre(2, None, None))
        # Barao
        for _ in range(2):
            deck.append(Barao(3, None, None))
        # Aia
        for _ in range(2):
            deck.append(Aia(4, None, None))
        # Principe
        for _ in range(2):
            deck.append(Principe(5, None, None))
        # Rei
        for _ in range(1):
            deck.append(Rei(6, None, None))
        # Condessa
        for _ in range(1):
            deck.append(Condessa(7, None, None))
        # Princesa
        for _ in range(1):
            deck.append(Princesa(8, None, None))
        return deck

    def getId(self):
        return self.__id

Mesa(1)