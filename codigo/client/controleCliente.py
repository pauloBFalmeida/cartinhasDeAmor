# coding: utf-8
from sys import path
path.append('codigo')
import jsonpickle
from jogador import Jogador
from carta import Carta
from server.interfaceRede import InterfaceRede
from client.interfaceUsuario import InterfaceUsuario

class ControleCliente():

    def __init__(self, interfaceRede, interfaceUsuario, meuIp=None):
        self.__interRede = interfaceRede
        self.__interUsuario = interfaceUsuario
        self.meuIp = meuIp if meuIp else self.__interRede.getIp()
        self.__cmd = ['cmd']
        self.__ret = ['ret']
        self.__msg = ['msg']
        self.__jogadores = []

    def getIp(self):
        return self.meuIp

    def setHostIp(self, ip):
        self.__hostIp = ip

    def obterJogadores(self):
        self.__enviar(self.__cmd+"jogadores")
        self.__jogadores = list()

    def main(self):
        while True:
            entrada = self.__esperarResposta()
            self.__processar(entrada)

    def __processar(self, entrada):
        if entrada[0] == "cmd":
            self.__processarCmd(entrada[1:])
        elif entrada[1] == "msg":
            pass
    
    def decode_list(self, entrada):
        args = []
        for i in entrada[2:]:
            args.append(jsonpickle.decode(entrada[i]))
        return args

    def __processarCmd(self, comandos):
        if comandos[0] == "iniciarRound":
            self.__iniciarRound()
        elif comandos[0] == "apresentarGanhadorDoJogo":
            args = self.decode_list(comandos)
            self.apresentarGanhadorDoJogo(args[0])
        elif comandos[0] == "apresentarGanhadorDoRound":
            args = self.decode_list(comandos)
            self.apresentarGanhadorDoRound(args[0])
        elif comandos[0] == "compararCartas":
            args = self.decode_list(comandos)
            self.compararCartas(args[0], args[1])
        elif comandos[0] == "jogarCarta":
            args = self.decode_list(comandos)
            self.jogarCarta(args[0], args[1])
        elif comandos[0] == "selecionaJogador":
            args = self.decode_list(comandos)
            self.selecionaJogador(args[0], args[1], args[2], args[3])
        elif comandos[0] == "selecionaValorGuarda":
            args = self.decode_list(comandos)
            self.selecionaValorGuarda(args[0])
        elif comandos[0] == "jogadorEscolherCarta":
            args = self.decode_list(comandos)
            self.jogadorEscolherCarta(args[0])
        elif comandos[0] == "alertarSobreCondessa":
            args = self.decode_list(comandos)
            self.alertarSobreCondessa(args[0])
        elif comandos[0] == "anunciarMorto":
            args = self.decode_list(comandos)
            self.anunciarMorto(args[0],)
        elif comandos[0] == "resultadoGuarda":
            args = self.decode_list(comandos)
            self.resultadoGuarda(args[0])
        elif comandos[0] == "resultadoPadre":
            args = self.decode_list(comandos)
            self.resultadoPadre(args[0])
        elif comandos[0] == "resultadoBarao":
            args = self.decode_list(comandos)
            self.decode_list(args[0])
        elif comandos[0] == "resultadoAia":
            args = self.decode_list(comandos)
            self.resultadoAia(args[0])
        elif comandos[0] == "resultadoPrincipe":
            args = self.decode_list(comandos)
            self.resultadoPrincipe(args[0])
        elif comandos[0] == "resultadoRei":
            args = self.decode_list(comandos)
            self.resultadoRei(args[0], args[1])
        elif comandos[0] == "resultadoPrincesa":
            args = self.decode_list(comandos)
            self.resultadoPrincesa(args[0])
        

    def __iniciarRound(self):
        self.__interUsuario.iniciarRound()

    def compararCartas(self, j_ganhador, jogadores):
        self.__interUsuario.compararCartas(j_ganhador, jogadores)
    
    def apresentarGanhadorDoRound(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoRound(ganhador)

    def apresentarGanhadorDoJogo(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoJogo(ganhador)

    def jogadorEscolherCarta(self, jogadorTurno):
        ret = self.__interUsuario.jogadorEscolherCarta(jogadorTurno)
        self.__interRede.clienteEnviar(ret)
        
    def alertarSobreCondessa(self, jogadorTurno):
        self.__interUsuario.alertarSobreCondessa(jogadorTurno)

    def jogarCarta(self, jogadorTurno, carta_jogada):
        self.__interUsuario.jogarCarta(jogadorTurno, carta_jogada)

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        ret = self.__interUsuario.selecionaJogador(jogadorTurno, jogadores, siMesmo, fraseInicio)
        self.__interRede.clienteEnviar(ret)

    def selecionaValorGuarda(self, jogadorTurno):
        ret = self.__interUsuario.selecionaValorGuarda(jogadorTurno)
        self.__interRede.clienteEnviar(ret)

    def resultadoGuarda(self, result):
        self.__interUsuario.resultadoGuarda(result)

    def resultadoPadre(self, result):
        self.__interUsuario.resultadoPadre(result)

    def resultadoBarao(self, result):
        self.__interUsuario.resultadoBarao(result)

    def resultadoAia(self, result):
        self.__interUsuario.resultadoAia(result)

    def resultadoPrincipe(self, result):
        self.__interUsuario.resultadoPrincipe(result)

    def resultadoRei(self, result, jogadorTurno):
        self.__interUsuario.resultadoRei(jogadorTurno)

    def resultadoPrincesa(self, result):
        self.__interUsuario.resultadoPrincesa(result)

    def anunciarMorto(self, jogador):
        self.__interUsuario.anunciarMorto(jogador)
    

    def __enviar(self, lista):
        self.interRede.clienteEnviar(lista)

    def __esperarResposta(self):
        reply = None
        tentativas = 100
        while not reply and tentativas > 0:
            reply = self.interRede.clienteReceber()
            tentativas -= 1
        return reply