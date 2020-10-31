# coding: utf-8
from codigo.interfaceRede import InterfaceRede
from codigo.jogador import Jogador
from codigo.carta import Carta

class ControleServer():

    def __init__(self, interfaceRede, meuIp=None):
        self.interRede = interfaceRede
        self.meuIp = meuIp if meuIp else self.interRede.getIp()
        self.__cmd = 'cmd:'

    def getIp(self):
        return self.meuIp

    def __enviar(self, texto):
        self.interRede.enviar(self.host_ip, texto)

    def __enviarJogador(self, j):
        self.interRede.enviar(self.host_ip, j)

    def __enviarCarta(self, c):
        self.interRede.enviar(self.host_ip, c)

    def __enviarLista(self, l):
        self.interRede.enviar(self.host_ip, l)
    
    def iniciarRound(self):
        self.__enviar(self.__cmd+"iniciarRound")

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
        self.__enviar(self.__cmd+"jogadorEscolherCarta")
        self.__enviarJogador(jogadorTurno)

    def alertarSobreCondessa(self):
        self.__enviar(self.__cmd+"alertarSobreCondessa")

    def jogarCarta(self, jogadorTurno, carta_jogada):
        self.__enviar(self.__cmd+"jogadorEscolherCarta")
        self.__enviarJogador(jogadorTurno)
        self.__enviarCarta(jogadorTurno)

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        self.__enviar(self.__cmd+"selecionaJogador"+":"+str(siMesmo)+":"+fraseInicio)
        self.__enviarJogador(jogadorTurno)
        self.__enviarLista(jogadores)   #carta_jogada.getFraseInicio()

    def selecionaValorGuarda(self):
        self.__enviar(self.__cmd+"selecionaValorGuarda")

    def resultadoGuarda(self, result):
        self.__enviar(self.__cmd+"resultadoGuarda"+':'+result)

    def resultadoPadre(self, result):
        self.__enviar(self.__cmd+"resultadoPadre"+':'+result)

    def resultadoBarao(self, result):
        self.__enviar(self.__cmd+"resultadoBarao"+':'+result)

    def resultadoAia(self, result):
        self.__enviar(self.__cmd+"resultadoAia"+':'+result)

    def resultadoPrincipe(self, result):
        self.__enviar(self.__cmd+"resultadoPrincipe"+':'+result)

    def resultadoRei(self, result, jogadorTurno):
        self.__enviar(self.__cmd+"resultadoRei"+':'+result)
        self.__enviarJogador(jogadorTurno)

    def resultadoPrincesa(self, result):
        self.__enviar(self.__cmd+"resultadoPrincesa"+':'+result)

    def anunciarMorto(self, jogador):
        self.__enviar(self.__cmd+"anunciarMorto")
        self.__enviarJogador(jogador)