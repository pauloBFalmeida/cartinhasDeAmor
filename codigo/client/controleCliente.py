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
        self.__cmd = 'cmd:'
        self.__ret = 'ret:'
        self.__msg = 'msg:'
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
        entrada = entrada.split(':')
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
        self.__enviar(self.__cmd+"compararCartas")
        self.__enviarJogador(j_ganhador)
        self.__enviarLista(jogadores)   #self.__mesa.getJogadores()
    
    def apresentarGanhadorDoRound(self, ganhador):
        self.__enviar(self.__cmd+"apresentarGanhadorDoRound")
        self.__enviarJogador(ganhador)

    def apresentarGanhadorDoJogo(self, ganhador):
        self.__enviar(self.__cmd+"apresentarGanhadorDoJogo")
        self.__enviarJogador(ganhador)

    def jogadorEscolherCarta(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, self.__cmd+"jogadorEscolherCarta")
        index_carta = self.__esperarResposta()
        return index_carta

    def alertarSobreCondessa(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, self.__cmd+"alertarSobreCondessa")

    def jogarCarta(self, jogadorTurno, carta_jogada):
        self.__enviar(self.__cmd+"jogarCarta")
        self.__enviarJogador(jogadorTurno)
        self.__enviarCarta(carta_jogada)

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        self.__jogadorTurnoEnviar(self.__cmd+"selecionaJogador"+":"+str(siMesmo)+":"+fraseInicio)
        self.__jogadorTurnoEnviarLista(jogadores)   #carta_jogada.getFraseInicio()
        index_jogador = self.__esperarResposta()
        return index_jogador

    def selecionaValorGuarda(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, self.__cmd+"selecionaValorGuarda")
        id_carta = self.__esperarResposta()
        return id_carta

    def resultadoGuarda(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoGuarda"+':'+id1)

    def resultadoPadre(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoPadre"+':'+id1)

    def resultadoBarao(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoBarao"+':'+id1)

    def resultadoAia(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoAia"+':'+id1)

    def resultadoPrincipe(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoPrincipe"+':'+id1)

    def resultadoRei(self, result, jogadorTurno):
        id1 = result.getId()
        id2 = jogadorTurno.getId()
        self.__enviar(self.__cmd+"resultadoRei"+':'+id1+':'+id2)

    def resultadoPrincesa(self, result):
        id1 = result.getId()
        self.__enviar(self.__cmd+"resultadoPrincesa"+':'+id1)

    def anunciarMorto(self, jogador):
        self.__enviar(self.__cmd+"anunciarMorto")
        self.__enviarJogador(jogador)

    
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
            self.__interRede.enviar(ip, l)

    def __esperarResposta(self):
        return None
    