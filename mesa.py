# coding: utf-8
from random import shuffle
from jogador import *
#from carta import *

class Mesa():

    def __init__(self, id):
        self.__id = id
        self.__jogadores = []
        self.__turno = None
        self.__partidaIniciada = False
        self.__deck = self.__criarDeck()
        print(self.__deck)
        self.__lixo = []
        self.__embaralhar()

    def addJogador(self, jogador):
        self.__jogadores.append(jogador)

    def iniciarPartida(self):
        self.__turno = self.__jogadores[0]

    def passarTurno(self):
        i = (self.__jogadores.index(self.__turno)+1 ) % len(self.__jogadores)
        self.__turno = self.__jogadores[i]

    def __embaralhar(self):
        self.__deck = shuffle(self.__deck)

    def __criarDeck(self):
        deck = []
        # Guarda
        for _ in range(5):
            deck.append(1)
        # Padre
        for _ in range(2):
            deck.append(2)
        # Barao
        for _ in range(2):
            deck.append(3)
        # Empregada
        for _ in range(2):
            deck.append(4)
        # Principe
        for _ in range(2):
            deck.append(5)
        # Rei
        for _ in range(1):
            deck.append(6)
        # Condessa
        for _ in range(1):
            deck.append(7)
        # Princesa
        for _ in range(1):
            deck.append(8)

    def getId(self):
        return self.__id

Mesa(1)