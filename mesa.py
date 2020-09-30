# coding: utf-8
import jogador
import carta
from random import shuffle

class Mesa():

    def __init__(self, id):
        self.__id = id
        self.__maxPontos = 3
        self.__jogadores = []
        self.__jogoEmExecucao = False
        self.__roundEmExecucao = False
        self.__ganhadorDoJogo = None
        self.__ganhadorDoRound = None
        self.__lixo = []
        self.__jogadorTurno = None

    def iniciarJogo(self):
        self.__jogoEmExecucao = True

    def iniciarRound(self):
        self.__roundEmExecucao = True
        self.__embaralharDeck()
        self.__distribuirCartas()
        for j in self.__jogadores:
            j.set_vivo(True)
        self.__jogadorTurno = self.__jogadores[-1]

    def zerarPontos(self):
        self.__fimDeJogo = False
        for j in self.__jogadores:
            j.zerarPontos()

    def passarTurno(self):
        ultimo_i = self.__jogadores.index(self.__jogadorTurno)
        qtdJogadores = len(self.__jogadores)
        for i in range(1, qtdJogadores):
            curr_i = (ultimo_i + i) % qtdJogadores
            if self.__jogadores[curr_i].get_vivo():
                # proximo jogador vivo
                self.__jogadorTurno = self.__jogadores[curr_i]
                break
       
    def verificarFimDoRound(self):
        # menos de 2 vivos
        if sum([j.get_vivo() for j in self.__jogadores]) < 2:
            return 1
        # sem cartas restantes no deck
        elif len(self.__deck) == 0:
            return 2
        return 0

    def fimRound(self):
        self.__roundEmExecucao = False
        for j in self.__jogadores:
            if j.get_vivo():
                j.addPontos(1)
                self.__ganhadorDoRound = j
                if j.getPontos() >= self.__maxPontos:
                    self.__ganhadorDoJogo = j
                    self.__jogoEmExecucao = False
        # preparar proxima round
        for j in self.__jogadores:
            self.jogadorDescartarMao(j)
        self.__deck += self.__lixo

    def compararCartas(self):
        valor_maior = -1
        jogador_maior = None
        for j in self.__jogadores:
            if j.get_vivo():
                valor = j.getCartasMao()[0].get_valor()
                if valor > valor_maior:
                    valor_maior = valor
                    jogador_maior = j
                elif valor == valor_maior:
                    jogador_maior = None
        return jogador_maior

    def addJogador(self, jogador):
        self.__jogadores.append(jogador)

    def pegarCarta(self, jogador):
        if len(self.__deck) > 0:
            jogador.receberCarta(self.__deck.pop(0))

    def jogadorDescartarMao(self, j):
        self.__lixo += j.limparMao()

    def __embaralharDeck(self):
        shuffle(self.__deck)

    def __distribuirCartas(self):
        for j in self.__jogadores: j.receberCarta(self.__deck.pop(0))

    def setDeck(self, deck):
        self.__deck = deck

    def getId(self):
        return self.__id
    
    def getJogadores(self):
        return self.__jogadores
    
    def getJogadorTurno(self):
        return self.__jogadorTurno
    
    def getJogoEmExecucao(self):
        return self.__jogoEmExecucao
        
    def getRoundEmExecucao(self):
        return self.__roundEmExecucao

    def getGanhadorDoJogo(self):
        return self.__ganhadorDoJogo

    def getGanhadorDoRound(self):
        return self.__ganhadorDoRound