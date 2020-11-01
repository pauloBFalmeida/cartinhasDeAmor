# coding: utf-8
from sys import path
path.append('codigo')
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

    def __processarCmd(self, comandos):
        if comandos[0] == "iniciarRound":
            self.__iniciarRound()
        if comandos[0] == "compararCartas":
            pass


    def __iniciarRound(self):
        self.__interUsuario.iniciarRound()

    def compararCartas(self, j_ganhador, jogadores):
        self.__interUsuario.compararCartas(j_ganhador, jogadores)
    
    def apresentarGanhadorDoRound(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoRound(ganhador)

    def apresentarGanhadorDoJogo(self, ganhador):
        self.__interUsuario.apresentarGanhadorDoJogo(ganhador)

    def jogadorEscolherCarta(self, jogadorTurno):
        self.__interUsuario.jogadorEscolherCarta(jogadorTurno)

    def alertarSobreCondessa(self, jogadorTurno):
        self.__interUsuario.alertarSobreCondessa(jogadorTurno)

    def jogarCarta(self, jogadorTurno, carta_jogada):
        self.__interUsuario.jogarCarta(jogadorTurno, carta_jogada)

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        send_back = self.__interUsuario.selecionaJogador(jogadorTurno, jogadores, siMesmo, fraseInicio)
        self.__interRede.clienteEnviar(send_back)

    def selecionaValorGuarda(self, jogadorTurno):
        self.__interUsuario.selecionaValorGuarda(jogadorTurno)

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
    






    def __jogadorTurnoEnviar(jogadorTurno, texto):
        id = jogadorTurno.getId()
        ip = self.__jogadores_ip[id]
        self.__interRede.enviar(ip, texto)

    def __jogadorTurnoEnviarLista(jogadorTurno, l):
        id = jogadorTurno.getId()
        ip = self.__jogadores_ip[id]
        self.__interRede.enviar(ip, l)

    def __enviar(self, texto):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.__interRede.enviar(ip, texto)

    def __enviarJogador(self, j):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.__interRede.enviar(ip, j)

    def __enviarCarta(self, c):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.__interRede.enviar(ip, c)

    def __enviarLista(self, l):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.__interRede.interfaceRede(ip, l)

    def __esperarResposta(self):
        return ""
    