# coding: utf-8
from codigo.interfaceUsuario import InterfaceUsuario
from codigo.jogador import Jogador
from codigo.mesa import Mesa
from codigo.carta import Carta, Guarda, Padre, Barao, Aia, Principe, Rei, Condessa, Princesa
from codigo.controleRede import ControleRede

class ControleJogo():

    def __init__(self, controleRede):
        self.controleRede = controleRede

    def setMesa(self, mesa):
        self.__mesa = mesa
        self.__mesa.setDeck(self.__criarDeck())

    def gerenciarJogo(self):
        self.__mesa.iniciarJogo()
        while self.__mesa.getJogoEmExecucao():
            self.controleRede.iniciarRound()
            self.__mesa.iniciarRound()
            while self.__mesa.getRoundEmExecucao():
                self.__mesa.passarTurno()
                self.__acaoTurno()
                # verificar fim do round
                verFimRound = self.__mesa.verificarFimDoRound()
                if verFimRound == 1:
                    self.__mesa.fimRound()
                elif verFimRound == 2:
                    j_ganhador = self.__mesa.compararCartas()
                    self.controleRede.compararCartas(j_ganhador, self.__mesa.getJogadores())
                    for j in self.__mesa.getJogadores():
                        if j != j_ganhador:
                            self.__matarJogador(j)
                    self.__mesa.fimRound()
            # fim de round
            ganhador = self.__mesa.getGanhadorDoRound()
            self.controleRede.apresentarGanhadorDoRound(ganhador)
        # fim de jogo
        ganhador = self.__mesa.getGanhadorDoJogo()
        self.controleRede.apresentarGanhadorDoJogo(ganhador)

    def __acaoTurno(self):
        jogadorTurno = self.__mesa.getJogadorTurno()
        # perde a protecao
        jogadorTurno.tirarProtecao()
        # pega uma carta
        self.__mesa.pegarCarta(jogadorTurno)
        # jogar uma carta
        error = True
        while error:
            carta_i = self.controleRede.jogadorEscolherCarta(jogadorTurno)
            error = self.__condicaoCondessa(jogadorTurno, carta_i)
            if error:
                self.controleRede.alertarSobreCondessa(jogadorTurno)
            else:
                carta_jogada = jogadorTurno.jogar_carta(carta_i)
                self.controleRede.jogarCarta(jogadorTurno, carta_jogada)
                self.__acaoCarta(jogadorTurno, carta_jogada)

    def __acaoCarta(self, jogadorTurno, carta_jogada):
        jogadores = self.__mesa.getJogadores()
        carta_v = carta_jogada.get_valor()
        j_alvo, valor = 0, 0
        if carta_v in [1,2,3,5,6]:
            siMesmo = carta_v == 5              # principe
            j_alvo = self.controleRede.selecionaJogador(jogadorTurno, jogadores, siMesmo, carta_jogada.getFraseInicio())
            if carta_v == 1 and j_alvo != None: # guarda
                valor = self.controleRede.selecionaValorGuarda(jogadorTurno)
        if j_alvo != None:
            result = carta_jogada.executar_acao(jogadorTurno, j_alvo, valor)
            # Guarda
            if   carta_v == 1:
                self.controleRede.resultadoGuarda(result)
                if result:
                    self.__matarJogador(j_alvo)
            # Padre
            elif carta_v == 2:
                self.controleRede.resultadoPadre(result)
            # Barao
            elif carta_v == 3:
                self.controleRede.resultadoBarao(result)
                if result != None:
                    self.__matarJogador(result)
            # Aia
            elif carta_v == 4:
                self.controleRede.resultadoAia(result)
            # Principe
            elif carta_v == 5:
                self.__mesa.jogadorDescartarMao(result)
                self.__mesa.pegarCarta(result)
                self.controleRede.resultadoPrincipe(result)
            # Rei
            elif carta_v == 6:
                self.controleRede.resultadoRei(result, jogadorTurno)
            # Princesa
            elif carta_v == 8:
                self.controleRede.resultadoPrincesa(result)
                self.__matarJogador(result)

    def __matarJogador(self, jogador):
        jogador.morre()
        self.controleRede.anunciarMorto(jogador)

    def __condicaoCondessa(self, jogadorTurno, index):
        cartasMao = jogadorTurno.getCartasMao()
        if jogadorTurno.sizeCartasMao() > 1:
            if isinstance(cartasMao[index], Rei) or isinstance(cartasMao[index], Principe):
                if isinstance(cartasMao[(index+1)%2], Condessa):
                    return True
        return False

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
        # set controle de jogo
        for c in deck:
            c.set_controleJogo(self)
        return deck
