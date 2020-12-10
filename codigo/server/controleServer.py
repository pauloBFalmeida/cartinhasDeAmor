# coding: utf-8
import jsonpickle
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from server.interfaceRede import InterfaceRede
from server.mapper import MapeadorJogador, MapeadorMesa

class ControleServer():

    def __init__(self, interfaceRede: InterfaceRede, meuIp=None):
        self.__interRede = interfaceRede
        self.meuIp = meuIp if meuIp else self.__interRede.getIp()
        self.__cmd = 'cmd'
        self.__ret = 'ret'
        self.__msg = 'msg'
        self.__jogadores_ip = {}
        self.__jogadores = []
        self.__retJogadorEscolherCarta = None
        self.__retSelecionaJogador = None
        self.__retSelecionaValorGuarda = None
        self.cores = [(200,200,200),
                      (200,100,100),
                      (100,0,0),
                      (100,200,100),
                      (0,100,0),
                      (100,100,200),
                      (0,0,100)]
        self.__jogo_iniciado = False
        self.__tabela_jogadores = MapeadorJogador()
        self.__tabela_mesa = MapeadorMesa()

    def getJogadores(self):
        return self.__jogadores

    def setMesa(self, mesa):
        self.__mesa = mesa

# ======== Processar ==============

    def __processar(self, entrada, id):
        comando = entrada.pop(0)
        if comando == self.__cmd:
            self.__processarCmd(entrada, id)
        elif comando == self.__ret:
            self.__processarRet(entrada)
        elif comando == self.__msg:
            pass

    def __processarRet(self, entrada):
        comando = entrada.pop(0)
        if comando == "jogadorEscolherCarta":
            self.__retJogadorEscolherCarta = entrada[0]
        elif comando == "selecionaJogador":
            self.__retSelecionaJogador = entrada[0]
        elif comando == "selecionaValorGuarda":
            self.__retSelecionaValorGuarda = entrada[0]

    def __processarCmd(self, entrada, id):
        comando = entrada.pop(0)
        if comando == "criarJogador":
            nome = entrada[0]
            self.__criarJogador(nome, id)

    def __criarJogador(self, nome, id):
        if len(nome) < 1:
            nome = 'jogador_'+str(id)
        j = self.__tabela_jogadores.get_jogador(nome)
        if j == None:
            j = Jogador(nome, self.cores[id])
        j.setId(id)
        self.__jogadores.append(j)
        self.__atualizarJogadores_ip()


# ============= enviar ================

    def iniciarRound(self):
        if not self.__jogo_iniciado:
            self.__jogo_iniciado = True
            self.__tabela_jogadores.insert_into_table(self.__jogadores)
        # enviar inicio de jogo pros jogadores
        self.__enviar([self.__cmd,"iniciarRound"])
        self.__jogadoresAtualizarMao()

    def anunciarCompararCartas(self):
        self.__enviar([self.__cmd,"anunciarCompararCartas"])

    def compararCartas(self, set_m, set_j, ganhador_j):
        self.__enviar([self.__cmd,"compararCartas", set_m, set_j, ganhador_j])
    
    def apresentarGanhadorDoRound(self, jg_nome, jg_pontos):
        self.__enviar([self.__cmd,"apresentarGanhadorDoRound", jg_nome, jg_pontos])

    def apresentarGanhadorDoJogo(self, jg_nome, jg_pontos):
        self.__finalRound()
        self.__enviar([self.__cmd,"apresentarGanhadorDoJogo", jg_nome, jg_pontos])

    def jogadorEscolherCarta(self, jogadorTurno, cartasMao_tipos):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"jogadorEscolherCarta", cartasMao_tipos])
        # esperar resposta
        self.esperarResposta("jogadorEscolherCarta")
        index_carta = self.__retJogadorEscolherCarta
        return index_carta

    def alertarSobreCondessa(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"alertarSobreCondessa"])

    def anunciarCarta(self, j_nome, c_nome):
        self.__enviar([self.__cmd,"anunciarCarta", j_nome, c_nome])

    def selecionaJogador(self, jogadorTurno, jogadores_texto, possiveis, fraseInicio):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaJogador", jogadores_texto, possiveis, fraseInicio])
        # esperar resposta
        self.esperarResposta("selecionaJogador")
        index_jogador = self.__retSelecionaJogador
        return index_jogador

    def selecionaValorGuarda(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaValorGuarda"])
        # esperar resposta
        self.esperarResposta("selecionaValorGuarda")
        id_carta = self.__retSelecionaValorGuarda
        return id_carta

    def resultadoGuarda(self, resultAcusacao):
        self.__enviar([self.__cmd,"resultadoGuarda", resultAcusacao])

    def resultadoPadre(self, jogadorTurno, c_nome):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"resultadoPadre", c_nome])

    def resultadoBarao(self, j_nome):
        self.__enviar([self.__cmd,"resultadoBarao", j_nome])

    def resultadoAia(self, j_nome):
        self.__enviar([self.__cmd,"resultadoAia", j_nome])

    def resultadoPrincipe(self, j_nome):
        self.__enviar([self.__cmd,"resultadoPrincipe", j_nome])

    def resultadoRei(self, j1_nome, j2_nome):
        self.__enviar([self.__cmd,"resultadoRei", j1_nome, j2_nome])
        self.__jogadoresAtualizarMao()

    def resultadoPrincesa(self, j_nome):
        self.__enviar([self.__cmd,"resultadoPrincesa", j_nome])

    def anunciarMorto(self, j_nome):
        self.__enviar([self.__cmd,"anunciarMorto", j_nome])

    def exibirMorto(self, j_id):
        self.__enviarJogadorEspecifico(j_id, [self.__cmd,"exibirMorto"])

    def atualizarPlacar(self, placar):
        self.__enviar([self.__cmd, "atualizarPlacar", placar])

    def __jogadoresAtualizarMao(self):
        for j in self.__jogadores:
            cartas_tipo = [c.get_valor() for c in j.getCartasMao()]
            self.__enviarJogadorEspecifico(j.getId(), [self.__cmd,"mostrarMao",cartas_tipo])

    def __finalRound(self):
        self.__tabela_jogadores.update_pontos(self.__jogadores)
        self.__tabela_mesa.insert_into_table(self.__mesa)
        #
        score = self.__tabela_jogadores.get_top_5()
        texto = "Scoreboard:"
        for s in score:
            texto += '\n' + s[0] + ' com ' + str(s[1]) + " pontos"
        self.__enviar([self.__cmd, "topscore", texto])
        #
        self.__tabela_jogadores.close()
        self.__tabela_mesa.close()

# ============= Rede ================

    # enviar para todos os jogadores
    def __enviar(self, lista):
        for id in self.__jogadores_ip:
            self.__enviarJogadorEspecifico(id, lista)
            #self.__interRede.serverEnviar(self.__jogadores_ip[id], lista)

    # enviar para o jogador do turno
    def __jogadorTurnoEnviar(self, jogadorTurno, lista):
        self.__enviarJogadorEspecifico(jogadorTurno.getId(), lista)

    def __enviarJogadorEspecifico(self, id, lista):
        self.__interRede.serverEnviar(self.__jogadores_ip[id], lista)

    def __atualizarJogadores_ip(self):
        self.__jogadores_ip = self.__interRede.getJogadores_ip()

    # espera pela resposta
    def esperarResposta(self, comando):
        reply = None
        comandoEsperado = False
        while not comandoEsperado:
            #reply = self.__interRede.serverReceber()
            reply, id = self.__interRede.serverReceberId()
            if reply:
                comandoEsperado = (comando == reply[1]) if comando else True
        # processar reply
        if reply:
            self.__processar(reply, id)

# ============= CHAT ================

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        mensagem = ['msg', jogador.get_nome(), msg.get_cor(), msg.get_texto()]
        self.__enviar(mensagem)
