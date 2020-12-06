# coding: utf-8
import jsonpickle
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from server.interfaceRede import InterfaceRede

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

    def addJogadorIdIp(self, id, ip):
        self.__jogadores_ip[id] = ip

    def getJogadores(self):
        return self.__jogadores

    def iniciarRound(self):
        self.__enviar([self.__cmd,"iniciarRound"])

# ======== Processar ==============

    def __processar(self, entrada):
        comando = entrada.pop(0)
        if comando == self.__cmd:
            self.__processarCmd(entrada)
        elif comando == self.__ret:
            print()
            print('retorno server')
            print(entrada)
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

    def __processarCmd(self, entrada):
        comando = entrada.pop(0)
        if comando == "criarJogador":
            nome = entrada[0]
            id = len(self.__jogadores)
            if len(nome) < 1:
                nome = 'jogador_'+str(id)
            j = Jogador(id, nome, self.cores[id])
            self.__jogadores.append(j)
            self.__atualizarJogadores_ip()

# ============= enviar ================

    def anunciarCompararCartas(self):
        self.__enviar([self.__cmd,"anunciarCompararCartas"])

    def compararCartas(self, set_m, set_j, ganhador_j):
        self.__enviar([self.__cmd,"compararCartas", set_m, set_j, ganhador_j])
    
    def apresentarGanhadorDoRound(self, jg_nome, jg_pontos):
        self.__enviar([self.__cmd,"apresentarGanhadorDoRound", jg_nome, jg_pontos])

    def apresentarGanhadorDoJogo(self, jg_nome, jg_pontos):
        self.__enviar([self.__cmd,"apresentarGanhadorDoJogo", jg_nome, jg_pontos])

    def jogadorEscolherCarta(self, jogadorTurno, cartasMao_tipos):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"jogadorEscolherCarta", cartasMao_tipos])
        # esperar resposta
        self.esperarResposta("jogadorEscolherCarta")
        index_carta = self.__retJogadorEscolherCarta
        self.__retJogadorEscolherCarta = None
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
        self.__retSelecionaJogador = None
        return index_jogador

    def selecionaValorGuarda(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaValorGuarda"])
        # esperar resposta
        self.esperarResposta("selecionaValorGuarda")
        id_carta = self.__retSelecionaValorGuarda
        self.__retSelecionaValorGuarda = None
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

    def resultadoPrincesa(self, j_nome):
        self.__enviar([self.__cmd,"resultadoPrincesa", j_nome])

    def anunciarMorto(self, j_nome):
        self.__enviar([self.__cmd,"anunciarMorto", j_nome])

    def atualizarPlacar(self, placar):
        self.__enviar([self.__cmd, "atualizarPlacar", placar])

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
        print()
        print('enviar server')
        print('id'+str(id))
        print(lista)
        self.__interRede.serverEnviar(self.__jogadores_ip[id], lista)

    def __atualizarJogadores_ip(self):
        self.__jogadores_ip = self.__interRede.getJogadores_ip()

    # espera pela resposta
    def esperarResposta(self, comando):
        reply = None
        comandoEsperado = False
        while not comandoEsperado:
            reply = self.__interRede.serverReceber()
            if reply:
                comandoEsperado = (comando == reply[1]) if comando else True
        # processar reply
        if reply:
            self.__processar(reply)

# ============= CHAT ================

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        mensagem = ['msg', jogador.get_nome(), msg.get_cor(), msg.get_texto()]
        self.__enviar(mensagem)
