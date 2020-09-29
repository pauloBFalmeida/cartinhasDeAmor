# coding: utf-8
from random import shuffle
from jogador import *
from cartas import *

class Mesa():

    def __init__(self, id):
        self.__id = id
        self.__maxPontos = 3
        self.__jogadores = []
        ## teste
        #for i in range(5):
        #    self.addJogador(Jogador(i, 'nome'+str(i), 0))
        self.__jogadorTurno = None
        self.__partidaIniciada = False
        self.__deck = self.__criarDeck()
        self.__lixo = []
        #self.iniciarPartida()
    
    def iniciarPartida(self):
        self.__partidaIniciada = True
        self.__embaralharDeck()
        self.__distribuirCartas()
        for j in self.__jogadores:
            j.set_vivo(True)
        print("INICIANDO PARTIDA")
        self.__jogadorTurno = self.__jogadores[-1]
        while self.__partidaIniciada:
            self.__passarTurno()
            self.__acaoTurno()


    def __passarTurno(self):
        ultimo_i = self.__jogadores.index(self.__jogadorTurno)
        vivos = [j.get_vivo() for j in self.__jogadores]
        # menos de 2 vivos
        if sum(vivos) < 2:
            self.__fimPartida()
        else:
            qtdJogadores = len(self.__jogadores)
            curr_i = -1
            for i in range(1, qtdJogadores):
                curr_i = (ultimo_i + i) % qtdJogadores
                if vivos[curr_i]:
                    break
            # proximo jogador
            self.__jogadorTurno = self.__jogadores[curr_i]

    def __acaoTurno(self):
        print()
        self.__jogadorTurno.tirarProtecao()
        self.pegarCarta(self.__jogadorTurno)
        if len(self.__jogadorTurno.getCartasMao()) == 0: self.__jogadorTurno.morre()
        self.__jogadorEscolheCarta()

    def __fimPartida(self):
        self.__partidaIniciada = False
        ganhador = None
        for j in self.__jogadores:
            if j.get_vivo():
                ganhador = j
                print('vitoria de ' + j.getNome())
                j.addPontos(1)
        # nenhum ganhador
        if ganhador == None:
            print('ngm venceu esse round')
        # final do game
        if ganhador != None and j.getPontos() >= self.__maxPontos:
            print('final do game')
        # preparar proxima partida
        else:
            for j in self.__jogadores:
                j.limparMao()
            self.__deck += self.__lixo
            self.iniciarPartida()

    def __jogadorEscolheCarta(self):
        possivel = False
        while not possivel:
            print(self.__jogadorTurno.getNome()+' escolha uma carta')
            for i in range(len(self.__jogadorTurno.getCartasMao())):
                print(str(i)+' '+self.__jogadorTurno.getCartasMao()[i].get_nome())
            i = int(input())
            if i >= 0 and i < len(self.__jogadorTurno.getCartasMao()):
                possivel = self.__jogadorTurno.jogar_carta(i)

    def addJogador(self, jogador):
        jogador.setMesa(self)
        self.__jogadores.append(jogador)

    def pegarCarta(self, jogador):
        if len(self.__deck) > 0:
            jogador.receberCarta(self.__deck.pop(0))
        else:
            self.__fimPartidaCompararCartas()

    def __fimPartidaCompararCartas(self):
        valor_maior = -1
        jogador_maior = None
        for j in self.__jogadores:
            if j.get_vivo():
                valor = j.getCartasMao()[0].get_valor()
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
        for j in self.__jogadores: j.receberCarta(self.__deck.pop(0))

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
    
    def getJogadores(self):
        return self.__jogadores
