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

    def addJogador(self, j):
        self.__jogadores.append(j)

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
        print('processar comando')
        print(comando)
        if comando == "id":
            id = len(self.__jogadores_ip)
            self.__enviarJogadorEspecifico(id, [self.__ret, 'id', id])
        elif comando == "criarJogador":
            print('======= jhogador criado =========')
            nome = entrada[0]
            id = len(self.__jogadores)
            j = Jogador(id, nome, self.cores[id])
            self.__jogadores.append(j)

# ============= enviar ================

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
        jt_json = jsonpickle.encode(jogadorTurno)
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"jogadorEscolherCarta",jt_json])
        # esperar resposta
        self.esperarResposta("jogadorEscolherCarta")
        index_carta = self.__retJogadorEscolherCarta
        self.__retJogadorEscolherCarta = None
        return index_carta

    def alertarSobreCondessa(self, jogadorTurno):
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"alertarSobreCondessa"])

    def jogarCarta(self, jogadorTurno, carta_jogada):
        jt_json = jsonpickle.encode(jogadorTurno)
        c_json = jsonpickle.encode(carta_jogada)
        self.__enviar([self.__cmd,"jogarCarta",jt_json, c_json])

    def selecionaJogador(self, jogadorTurno, jogadores, siMesmo, fraseInicio):
        jt_json = jsonpickle.encode(jogadorTurno)
        js_json = [jsonpickle.encode(j) for j in jogadores]
        self.__jogadorTurnoEnviar(jogadorTurno, [self.__cmd,"selecionaJogador",jt_json,js_json,siMesmo,fraseInicio])
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

# ============= Rede ================
        
    # enviar para o jogador do turno
    def __jogadorTurnoEnviar(self, jogadorTurno, lista):
        jogador_id = jogadorTurno.getId()
        self.__enviarJogadorEspecifico(jogador_id, lista)

    def __atualizarJogadores_ip(self):
        self.__jogadores_ip = self.__interRede.getJogadores_ip()

    # enviar para todos os jogadores
    def __enviar(self, lista):
        self.__atualizarJogadores_ip()
        for id in self.__jogadores_ip:
            self.__interRede.serverEnviar(self.__jogadores_ip[id], lista)

    def __enviarJogadorEspecifico(self, jogador_id, lista):
        self.__atualizarJogadores_ip()
        print()
        print(self.__jogadores_ip)
        print()
        self.__interRede.serverEnviar(self.__jogadores_ip[jogador_id], lista)

    def esperarResposta(self, comando):
        comandoEsperado = False
        while comando or not comandoEsperado:
            reply = None
            tentativas = 100
            while not reply and tentativas > 0:
                reply = self.__interRede.serverReceber()
                tentativas -= 1
            if comando:
                if reply:
                    comandoEsperado = (comando == reply[1])
            else:
                comandoEsperado = True
            if reply:
                self.__processar(reply)

# ============= CHAT ================

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        mensagem = ['msg', jogador.get_nome(), msg.get_cor(), msg.get_texto()]
        self.__enviar(mensagem)
