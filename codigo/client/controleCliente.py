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

    def setHostIp(self, ip):
        self.__hostIp = ip

    def conectarServer(self):
        self.__interRede.startClient(self.__hostIp)

    def main(self):
        while True:
            entrada = self.__esperarResposta()
            self.__processar(entrada)

    def __processar(self, entrada):
        if entrada[0] == self.__cmd:
            self.__processarCmd(entrada[1:])
        elif entrada[1] == self.__msg:
            pass

    
    def __processarCmd(self, entrada):
        comando = entrada.pop(0)
        if comando == "iniciarRound":
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
            jogadorTurno = jsonpickle.decode(entrada[0])
            self.__alertarSobreCondessa(jogadorTurno)
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
            jogadorTurno = jsonpickle.decode(entrada[0])
            self.__selecionaValorGuarda(jogadorTurno)
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
        self.__enviar([self.__ret]+ret)
        
    def __alertarSobreCondessa(self, jogadorTurno):
        self.__interUsuario.alertarSobreCondessa()

    def __jogarCarta(self, jogadorTurno, carta_jogada):
        self.__interUsuario.jogarCarta(jogadorTurno, carta_jogada)

    def __selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        ret = self.__interUsuario.selecionaJogador(jogadorTurno, jogadores, siMesmo, fraseInicio)
        self.__enviar([self.__ret]+ret)

    def __selecionaValorGuarda(self, jogadorTurno):
        ret = self.__interUsuario.selecionaValorGuarda()
        self.__enviar([self.__ret]+ret)

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
    

    def __enviar(self, lista):
        self.__interRede.clienteEnviar(lista)

    def __esperarResposta(self):
        reply = None
        tentativas = 100
        while not reply and tentativas > 0:
            reply = self.interRede.clienteReceber()
            tentativas -= 1
        return reply