# coding: utf-8
from codigo.interfaceRede import InterfaceRede
from codigo.jogador import Jogador
from codigo.carta import Carta

class ControleServer():

    def __init__(self, interfaceRede, meuIp=None):
        self.interRede = interfaceRede
        self.meuIp = meuIp if meuIp else self.interRede.getIp()
        self.__cmd = 'cmd:'
        self.__jogadores_ip = {}

    def getIp(self):
        return self.meuIp

    def addJogadorIdIp(self, id, ip):
        self.__jogadores_ip[id] = ip

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
        self.interRede.enviar(ip, texto)

    def __jogadorTurnoEnviarLista(jogadorTurno, l):
        id = jogadorTurno.getId()
        ip = self.__jogadores_ip[id]
        self.interRede.enviar(ip, l)

    def __enviar(self, texto):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.interRede.enviar(ip, texto)

    def __enviarJogador(self, j):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.interRede.enviar(ip, j)

    def __enviarCarta(self, c):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.interRede.enviar(ip, c)

    def __enviarLista(self, l):
        for id in self.__jogadores_ip:
            ip = self.__jogadores_ip[id]
            self.interRede.enviar(ip, l)

    def __esperarResposta(self):
        return None
    