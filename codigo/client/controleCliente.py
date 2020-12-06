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
        nome = self.__interUsuario.nomeJogador()
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
        elif comando == "anunciarCompararCartas":
            self.__anunciarCompararCartas()
        elif comando == "compararCartas":
            set_m = entrada[0]
            set_j = entrada[1]
            ganhador_j = entrada[2]
            self.__compararCartas(set_m, set_j, ganhador_j)
        elif comando == "apresentarGanhadorDoRound":
            jg_nome = entrada[0]
            jg_pontos = entrada[1]
            self.__apresentarGanhadorDoRound(jg_nome, jg_pontos)
        elif comando == "apresentarGanhadorDoJogo":
            jg_nome = entrada[0]
            jg_pontos = entrada[1]
            self.__apresentarGanhadorDoJogo(jg_nome, jg_pontos)
        elif comando == "jogadorEscolherCarta":
            cartasMao_tipos = entrada[0]
            self.__jogadorEscolherCarta(cartasMao_tipos)
        elif comando == "alertarSobreCondessa":
            self.__alertarSobreCondessa()
        elif comando == "anunciarCarta":
            j_nome = entrada[0]
            c_nome = entrada[1]
            self.__anunciarCarta(j_nome, c_nome)
        elif comando == "selecionaJogador":
            jogadores_texto = entrada[0]
            possiveis = entrada[1]
            fraseInicio = entrada[2]
            self.__selecionaJogador(jogadores_texto, possiveis, fraseInicio)
        elif comando == "selecionaValorGuarda":
            self.__selecionaValorGuarda()
        elif comando == "resultadoGuarda":
            resultAcusacao = entrada[0]
            self.__resultadoGuarda(resultAcusacao)
        elif comando == "resultadoPadre":
            c_nome = entrada[0]
            self.__resultadoPadre(c_nome)
        elif comando == "resultadoBarao":
            j_nome = entrada[0]
            self.__resultadoBarao(j_nome)
        elif comando == "resultadoAia":
            j_nome = entrada[0]
            self.__resultadoAia(j_nome)
        elif comando == "resultadoPrincipe":
            j_nome = entrada[0]
            self.__resultadoPrincipe(j_nome)
        elif comando == "resultadoRei":
            j1_nome = entrada[0]
            j2_nome = entrada[1]
            self.__resultadoRei(j1_nome, j2_nome)
        elif comando == "resultadoPrincesa":
            j_nome = entrada[0]
            self.__resultadoPrincesa(j_nome)
        elif comando == "anunciarMorto":
            j_nome = entrada[0]
            self.__anunciarMorto(j_nome)
            
# ======== Funcoes com a interface usuario ==============

    def __iniciarRound(self):
        self.__interUsuario.iniciarRound()

    def __anunciarCompararCartas(self):
        self.__interUsuario.anunciarCompararCartas()

    def __compararCartas(self, set_m, set_j, ganhador_j):
        self.__interUsuario.compararCartas(set_m, set_j, ganhador_j)
    
    def __apresentarGanhadorDoRound(self, jg_nome, jg_pontos):
        self.__interUsuario.apresentarGanhadorDoRound(jg_nome, jg_pontos)

    def __apresentarGanhadorDoJogo(self, jg_nome, jg_pontos):
        self.__interUsuario.apresentarGanhadorDoJogo(jg_nome, jg_pontos)

    def __jogadorEscolherCarta(self, cartasMao_tipos):
        ret = self.__interUsuario.jogadorEscolherCarta(cartasMao_tipos)
        self.__enviar([self.__ret, 'jogadorEscolherCarta', ret])
        
    def __alertarSobreCondessa(self):
        self.__interUsuario.alertarSobreCondessa()

    def __anunciarCarta(self, j_nome, c_nome):
        self.__interUsuario.anunciarCarta(j_nome, c_nome)

    def __selecionaJogador(self, jogadores_texto, possiveis, fraseInicio):
        ret = self.__interUsuario.selecionaJogador(jogadores_texto, possiveis, fraseInicio)
        self.__enviar([self.__ret, 'selecionaJogador', ret])

    def __selecionaValorGuarda(self):
        ret = self.__interUsuario.selecionaValorGuarda()
        self.__enviar([self.__ret, 'selecionaValorGuarda', ret])

    def __resultadoGuarda(self, resultAcusacao):
        self.__interUsuario.resultadoGuarda(resultAcusacao)

    def __resultadoPadre(self, c_nome):
        self.__interUsuario.resultadoPadre(c_nome)

    def __resultadoBarao(self, j_nome):
        self.__interUsuario.resultadoBarao(j_nome)

    def __resultadoAia(self, j_nome):
        self.__interUsuario.resultadoAia(j_nome)

    def __resultadoPrincipe(self, j_nome):
        self.__interUsuario.resultadoPrincipe(j_nome)

    def __resultadoRei(self, j1_nome, j2_nome):
        self.__interUsuario.resultadoRei(j1_nome, j2_nome)

    def __resultadoPrincesa(self, j_nome):
        self.__interUsuario.resultadoPrincesa(j_nome)

    def __anunciarMorto(self, j_nome):
        self.__interUsuario.anunciarMorto(j_nome)
    
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
