# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from mesa import Mesa
from carta import Carta, Guarda, Padre, Barao, Aia, Principe, Rei, Condessa, Princesa
#from server.controleServer import ControleServer

class ControleJogo():

    def __init__(self, controleServer):
        self.controleServer = controleServer

    def setMesa(self, mesa):
        self.__mesa = mesa
        self.__mesa.setDeck(self.__criarDeck())

    def gerenciarJogo(self):
        self.__mesa.iniciarJogo()
        while self.__mesa.getJogoEmExecucao():
            self.controleServer.iniciarRound()
            self.__mesa.iniciarRound()
            while self.__mesa.getRoundEmExecucao():
                self.__mesa.passarTurno()
                self.__acaoTurno()
                # verificar fim do round
                verFimRound = self.__mesa.verificarFimDoRound()
                if verFimRound == 1:
                    self.__mesa.fimRound()
                elif verFimRound == 2:
                    self.__compararCartas()
                    self.__mesa.fimRound()
            # fim de round
            ganhador = self.__mesa.getGanhadorDoRound()
            self.controleServer.apresentarGanhadorDoRound(ganhador.getNome(), ganhador.getPontos())
        # fim de jogo
        ganhador = self.__mesa.getGanhadorDoJogo()
        self.controleServer.apresentarGanhadorDoJogo(ganhador.getNome(), ganhador.getPontos())

    def __acaoTurno(self):
        jogadorTurno = self.__mesa.getJogadorTurno()
        # perde a protecao
        jogadorTurno.tirarProtecao()
        # pega uma carta
        self.__mesa.pegarCarta(jogadorTurno)
        # jogar uma carta
        error = True
        while error:
            carta_i = self.controleServer.jogadorEscolherCarta(
                jogadorTurno,
                [c.get_valor() for c in jogadorTurno.getCartasMao()]
                )
            error = self.__condicaoCondessa(jogadorTurno, carta_i)
            if error:
                self.controleServer.alertarSobreCondessa(jogadorTurno)
            else:
                carta_jogada = jogadorTurno.jogar_carta(carta_i)
                self.controleServer.anunciarCarta(jogadorTurno.getNome(), carta_jogada.get_nome())
                self.__acaoCarta(jogadorTurno, carta_jogada)

    def __acaoCarta(self, jogadorTurno, carta_jogada):
        carta_v = carta_jogada.get_valor()
        # jogador do turno escolhe o jogador alvo
        j_alvo = None
        if carta_v in [1,2,3,5,6]:      # guarda, padre, barao, principe, rei
            j_alvo = self.__selecionaJogador(jogadorTurno, carta_jogada)
        # acao da carta
        if j_alvo != None:
            # guarda
            valor = self.controleServer.selecionaValorGuarda(jogadorTurno) if (carta_v == 1) else -1
            # resultado da acao da carta
            result = carta_jogada.executar_acao(jogadorTurno, j_alvo, valor)
            if result:
                # Guarda
                if carta_v == 1:
                    # result = bool de se acusacao do j_alvo deu certo ou nao
                    self.controleServer.resultadoGuarda(result)
                    self.__matarJogador(j_alvo)
                # Padre
                elif carta_v == 2:
                    # result = carta da mao do j_alvo
                    self.controleServer.resultadoPadre(jogadorTurno, result.get_nome())
                # Barao
                elif carta_v == 3:
                    # result = jogador que tinha a menor mao
                    self.controleServer.resultadoBarao(result.getNome())
                    self.__matarJogador(result)
                # Aia
                elif carta_v == 4:
                    # result = jogador que recebeu a protecao
                    self.controleServer.resultadoAia(result.getNome())
                # Principe
                elif carta_v == 5:
                    # result = j_alvo
                    self.__mesa.jogadorDescartarMao(result)
                    self.__mesa.pegarCarta(result)
                    self.controleServer.resultadoPrincipe(result.getNome())
                # Rei
                elif carta_v == 6:
                    # result = j_alvo
                    self.controleServer.resultadoRei(result.getNome(), jogadorTurno.getNome())
                # Princesa
                elif carta_v == 8:
                    # result = j_origem
                    self.controleServer.resultadoPrincesa(result.getNome())
                    self.__matarJogador(result)


    def __selecionaJogador(self, jogadorTurno, carta_jogada):
        jogadores = self.__mesa.getJogadores()
        siMesmo = (carta_jogada.get_valor() == 5)    # principe
        #
        jogadores_texto = []
        possiveis = []
        for i in range(len(jogadores)):
            j = jogadores[i]
            j_texto = j.getNome()
            #
            if (not siMesmo) and j == jogadorTurno:
                j_texto += " (nao possivel)"
            elif not j.get_vivo():
                j_texto += " (morto)"
            elif j.getProtecao():
                j_texto += " (protegido)"
            else:
                possiveis.append(i)
            jogadores_texto.append(j_texto)
        #
        index_alvo = self.controleServer.selecionaJogador(jogadorTurno,
                                                          jogadores_texto,
                                                          possiveis,
                                                          carta_jogada.getFraseInicio())
        if index_alvo:
            return jogadores[index_alvo]
        return None

    def __matarJogador(self, jogador):
        jogador.morre()
        self.controleServer.anunciarMorto(jogador.getNome())

    def __condicaoCondessa(self, jogadorTurno, index):
        cartasMao = jogadorTurno.getCartasMao()
        if jogadorTurno.sizeCartasMao() > 1:
            if isinstance(cartasMao[index], Rei) or isinstance(cartasMao[index], Principe):
                if isinstance(cartasMao[(index+1)%2], Condessa):
                    return True
        return False

    def __compararCartas(self):
        self.controleServer.anunciarCompararCartas()
        j_maior = None
        v_maior = None
        j_vivos = [j for j in self.__jogadores if j.get_vivo()]
        for j in j_vivos:
            valor = j.getCartasMao()[0].get_valor()
            # primeiro jogador a ser testado
            if not j_maior:
                j_maior = j
                v_maior = valor
                continue
            # outros jogadores
            set_m = (j_maior.getNome(), j_maior.getCartasMao()[0].get_nome(),   v_maior)
            set_j = (j.getNome(),       j.getCartasMao()[0].get_nome(),         valor)
            #
            if valor > v_maior:
                self.controleServer.compararCartas(set_m, set_j, True)
                self.__matarJogador(j_maior)
                j_maior = j
                v_maior = valor
            elif valor == v_maior:
                self.controleServer.compararCartas(set_m, set_j, False)
                self.__matarJogador(j_maior)
                self.__matarJogador(j)
                j_maior = None


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
