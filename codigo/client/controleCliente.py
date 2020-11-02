# coding: utf-8
import jsonpickle
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from server.interfaceRede import InterfaceRede
from client.interfaceUsuario import InterfaceUsuario

class ControleCliente():

    def __init__(self, interfaceRede, interfaceUsuario):
        self.__interRede = interfaceRede
        self.__interUsuario = interfaceUsuario
        self.__cmd = 'cmd'
        self.__ret = 'ret'
        self.__msg = 'msg'
        self.__id = -1

    def setHostIp(self, ip):
        self.__hostIp = ip

    def conectarServer(self):
        self.__interRede.startClient(self.__hostIp)

    def criarJogador(self):
        id = 0
        nome = self.__interUsuario.nomeJogador(id)
        self.__enviar([self.__cmd,'criarJogador',nome])

    def getId(self):
        self.__enviar([self.__cmd,'id'])
        while self.__id == -1:
            self.__esperarResposta('id')
        return self.__id

    def main(self):
        while True:
            self.__esperarResposta(None)

    def desligar(self):
        self.__interRede.clienteEnd()

    def returnId(self):
        return self.__id
    
# ======== Processar ==============

    def __processar(self, entrada):
        comando = entrada.pop(0)
        if   comando == self.__cmd:
            self.__processarCmd(entrada)
        elif comando == self.__ret:
            self.__processarRet(entrada)
        elif comando == self.__msg:
            pass

    def __processarRet(self, entrada):
        comando = entrada.pop(0)
        if comando == "id":
            self.__id = entrada[0]

    def __processarCmd(self, entrada):
        comando = entrada.pop(0)
        if   comando == "iniciarRound":
            self.__iniciarRound()
        elif comando == "compararCartas":
            j_ganhador = jsonpickle.decode(entrada[0])
            jogadores = [jsonpickle.decode(j) for j in entrada[1]]
            self.__compararCartas(j_ganhador, jogadores)
        elif comando == "apresentarGanhadorDoRound":
            ganhador = jsonpickle.decode(entrada[0])
            self.__apresentarGanhadorDoRound(ganhador)
        elif comando == "apresentarGanhadorDoJogo":
            ganhador = jsonpickle.decode(entrada[0])
            self.__apresentarGanhadorDoJogo(ganhador)
        elif comando == "jogadorEscolherCarta":
            jogadorTurno = jsonpickle.decode(entrada[0])
            self.__jogadorEscolherCarta(jogadorTurno)
        elif comando == "alertarSobreCondessa":
            self.__alertarSobreCondessa()
        elif comando == "jogarCarta":
            jogadorTurno = jsonpickle.decode(entrada[0])
            carta_jogada = jsonpickle.decode(entrada[1])
            self.__jogarCarta(jogadorTurno, carta_jogada)
        elif comando == "selecionaJogador":
            jogadorTurno = jsonpickle.decode(entrada[0])
            jogadores = [jsonpickle.decode(j) for j in entrada[1]]
            siMesmo = entrada[2]
            fraseInicio = entrada[3]
            self.__selecionaJogador(jogadorTurno, jogadores, siMesmo, fraseInicio)
        elif comando == "selecionaValorGuarda":
            self.__selecionaValorGuarda()
        elif comando == "resultadoGuarda":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoGuarda(result)
        elif comando == "resultadoPadre":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoPadre(result)
        elif comando == "resultadoBarao":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoBarao(result)
        elif comando == "resultadoAia":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoAia(result)
        elif comando == "resultadoPrincipe":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoPrincipe(result)
        elif comando == "resultadoRei":
            result = jsonpickle.decode(entrada[0])
            jogadorTurno  = jsonpickle.decode(entrada[1])
            self.__resultadoRei(result, jogadorTurno)
        elif comando == "resultadoPrincesa":
            result = jsonpickle.decode(entrada[0])
            self.__resultadoPrincesa(result)
        elif comando == "anunciarMorto":
            jogador = jsonpickle.decode(entrada[0])
            self.__anunciarMorto(jogador)
            
# ======== Funcoes com a interface usuario ==============

    def __iniciarRound(self):
        self.__interUsuario.iniciarRound()

    def __compararCartas(self, j_ganhador, jogadores):
        self.__interUsuario.compararCartas(j_ganhador, jogadores)
    
    def __apresentarGanhadorDoRound(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoRound(ganhador)

    def __apresentarGanhadorDoJogo(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoJogo(ganhador)

    def __jogadorEscolherCarta(self, jogadorTurno):
        ret = self.__interUsuario.jogadorEscolherCarta(jogadorTurno)
        self.__enviar([self.__ret, 'jogadorEscolherCarta', ret])
        
    def __alertarSobreCondessa(self):
        self.__interUsuario.alertarSobreCondessa()

    def __jogarCarta(self, jogadorTurno, carta_jogada):
        self.__interUsuario.jogarCarta(jogadorTurno, carta_jogada)

    def __selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        ret = self.__interUsuario.selecionaJogador(jogadorTurno, jogadores, siMesmo, fraseInicio)
        self.__enviar([self.__ret, 'selecionaJogador', ret])

    def __selecionaValorGuarda(self):
        ret = self.__interUsuario.selecionaValorGuarda()
        self.__enviar([self.__ret, 'selecionaValorGuarda', ret])

    def __resultadoGuarda(self, result):
        self.__interUsuario.resultadoGuarda(result)

    def __resultadoPadre(self, result):
        self.__interUsuario.resultadoPadre(result)

    def __resultadoBarao(self, result):
        self.__interUsuario.resultadoBarao(result)

    def __resultadoAia(self, result):
        self.__interUsuario.resultadoAia(result)

    def __resultadoPrincipe(self, result):
        self.__interUsuario.resultadoPrincipe(result)

    def __resultadoRei(self, result, jogadorTurno):
        self.__interUsuario.resultadoRei(jogadorTurno)

    def __resultadoPrincesa(self, result):
        self.__interUsuario.resultadoPrincesa(result)

    def __anunciarMorto(self, jogador):
        self.__interUsuario.anunciarMorto(jogador)
    
# ======== Rede ==============

    def __enviar(self, lista):
        self.__interRede.clienteEnviar(lista)

    def __esperarResposta(self, comando):
        comandoEsperado = False
        while comando or (not comandoEsperado):
            reply = None
            tentativas = 100
            while not reply and tentativas > 0:
                reply = self.__interRede.clienteReceber()
                tentativas -= 1
            if comando:
                comandoEsperado = (comando == reply[1])
            if reply:
                self.__processar(reply)
