# coding: utf-8
from threading import Thread
from sys import path
path.append('codigo')
from server.server import Server
from server.interfaceMasterMind import InterfaceMasterMind
from client.controleCliente import ControleCliente
from client.interfaceTexto import InterfaceTexto
#from client.interfaceTexto import InterfaceTexto
from client.interfaceVisual import InterfaceVisual


# classe que comunica o controle com as interfaces
class CartinhaDeAmor:

    def __init__(self):
        #self.__interfaceUsuario = InterfaceTexto()
        self.__interfaceUsuario = InterfaceVisual()
        self.__interfaceRede = InterfaceMasterMind()

    def main(self):
        self.__preparativos()

    # criar server 
    def __criarServer(self, nJogadores):
        self.__server = Server(self.__interfaceRede)
        self.__server.start()
        self.__server.esperarEntrarJogadores(nJogadores)
        # iniciar partida
        self.__server.iniciarJogo()
        # fim
        self.__server.desligar()

    def __entrarJogo(self):
        if self.__online:
            host_ip = self.__interfaceUsuario.entrarIpHost()
        else:
            host_ip = "localhost"
        self.__controleCliente = ControleCliente(self.__interfaceRede, self.__interfaceUsuario)
        self.__controleCliente.setHostIp(host_ip)
        self.__controleCliente.conectarServer()
        # criar jogador
        self.__controleCliente.criarJogador()
        # 
        self.__controleCliente.main()
        # fim
        self.__fim()

    def __preparativos(self):
        self.__online, self.____criarServer = self.__interfaceUsuario.esperarPartida()
        if self.____criarServer:
            nJogadores = self.__interfaceUsuario.numeroJogadores()
            self.__serverThread = Thread(target=self.__criarServer, args=(nJogadores,))
            self.__serverThread.start()
            self.__interfaceUsuario.esperarandoJogadores()
        self.__entrarJogo()

    def __fim(self):
        self.__controleCliente.desligar()
        if self.____criarServer:
            self.__serverThread.join()
