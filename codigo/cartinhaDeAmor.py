# coding: utf-8
import pygame
#from threading import Thread
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
        self.preparativos()

    # criar server 
    def criarServer(self):
        self.__server = Server(self.__interfaceRede)
        nJogadores = self.__interfaceUsuario.numeroJogadores()
        self.__server.start()
        self.__server.esperarEntrarJogadores(nJogadores)
        self.__server.iniciarJogo()

    def entrarJogo(self):
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
        #
        self.fim()

    def preparativos(self):
        self.__online, self.__criarServer = self.__interfaceUsuario.esperarPartida()
        if self.__criarServer:
            self.criarServer()
        else:
            self.entrarJogo()

    def fim(self):
        if self.__criarServer:
            self.__serverThread.join()
            self.__server.desligar()
        self.__controleCliente.desligar()
