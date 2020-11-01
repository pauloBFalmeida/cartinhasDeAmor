# coding: utf-8
import jsonpickle
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta
from server.interfaceRede import InterfaceRede

class ControleServer():

    def __init__(self, interfaceRede: InterfaceRede, meuIp=None):
        self.interRede = interfaceRede
        self.meuIp = meuIp if meuIp else self.interRede.getIp()
        self.__cmd = 'cmd'
        self.__jogadores_ip = {}

    def getIp(self):
        return self.meuIp

    def addJogadorIdIp(self, id, ip):
        self.__jogadores_ip[id] = ip

    def iniciarRound(self):
        self.__enviar([self.__cmd,"iniciarRound"])

    def compararCartas(self, j_ganhador, jogadores):
        j_g_json = jsonpickle.encode(j_ganhador)
        js_json = [jsonpickle.encode(j) for j in jogadores]
        self.__enviar([self.__cmd,"compararCartas", j_g_json, js_json])
    
    def apresentarGanhadorDoRound(self, ganhador):
        g_json = jsonpickle.encode(ganhador)
        self.__enviar([self.__cmd,"apresentarGanhadorDoRound",g_json])

    def apresentarGanhadorDoJogo(self, ganhador):
        g_json = jsonpickle.encode(ganhador)
        self.__enviar([self.__cmd,"apresentarGanhadorDoJogo",g_json])

    def jogadorEscolherCarta(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"jogadorEscolherCarta"])
        index_carta = self.__esperarResposta()
        return index_carta

    def alertarSobreCondessa(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"alertarSobreCondessa"])

    def jogarCarta(self, jogadorTurno, carta_jogada):
        jt_json = jsonpickle.encode(jogadorTurno)
        c_json = jsonpickle.encode(carta_jogada)
        self.__enviar([self.__cmd,"jogarCarta",jt_json, c_json])

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        js_json = [jsonpickle.encode(j) for j in jogadores]
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaJogador",js_json,siMesmo,fraseInicio])
        index_jogador = self.__esperarResposta()
        return index_jogador

    def selecionaValorGuarda(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaValorGuarda"])
        id_carta = self.__esperarResposta()
        return id_carta

    def resultadoGuarda(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoGuarda",r_json])

    def resultadoPadre(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoPadre",r_json])

    def resultadoBarao(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoBarao",r_json])

    def resultadoAia(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoAia",r_json])

    def resultadoPrincipe(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoPrincipe",r_json])

    def resultadoRei(self, result, jogadorTurno):
        r_json = jsonpickle.encode(result)
        jt_json = jsonpickle.encode(jogadorTurno)
        self.__enviar([self.__cmd,"resultadoRei",r_json,jt_json])

    def resultadoPrincesa(self, result):
        r_json = jsonpickle.encode(result)
        self.__enviar([self.__cmd,"resultadoPrincesa",r_json])

    def anunciarMorto(self, jogador):
        j_json = jsonpickle.encode(jogador)
        self.__enviar([self.__cmd,"anunciarMorto",j_json])

    # enviar para o jogador do turno
    def __jogadorTurnoEnviar(self, jogadorTurno, lista):
        jt_json = jsonpickle.encode(jogadorTurno)
        lista = lista[0]+['jogadorTurno',jt_json]+lista[1:]
        self.__enviar(lista)

    # enviar para todos os jogadores
    def __enviar(self, lista):
        for id in self.__jogadores_ip:
            self.interRede.clienteEnviar(self.__jogadores_ip[id], lista)

    def __esperarResposta(self):
        reply = None
        tentativas = 100
        while not reply and tentativas > 0:
            reply = self.interRede.serverReceber()
            tentativas -= 1
        return reply

    ### CHAT ###

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        mensagem = ['msg', jogador.get_nome(), msg.get_cor(), msg.get_texto()]
        self._enviar(mensagem)
