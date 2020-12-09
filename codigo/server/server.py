#from interfaceMasterMindServer import InterfaceMasterMindServer
#from chat_server import ServerChat

#from interfaceMasterMind import InterfaceMasterMind
#import time
#import socket

#from sys import path
#path.append('codigo')
#from jogador import Jogador

import time
from sys import path
path.append('codigo')
from mesa import Mesa
from server.controleJogo import ControleJogo
from server.controleServer import *        #ControleServer
from server.interfaceRede import *

class Server():

    def __init__(self, interRede):
        self.__interRede = interRede
        self.__controleServer = ControleServer(self.__interRede, "localhost")
        self.__controleJogo = ControleJogo(self.__controleServer)
        self.__jogadores = []

    def start(self):
        self.__interRede.startServer('localhost')

    def esperarEntrarJogadores(self, nJogadores):
        while len(self.__jogadores) != nJogadores:
            time.sleep(0.5)
            self.__controleServer.esperarResposta(None)
            self.__jogadores = self.__controleServer.getJogadores()

    def iniciarJogo(self):
        self.__mesa = Mesa(0)
        for j in self.__jogadores:
            self.__mesa.addJogador(j)
        self.__controleJogo.setMesa(self.__mesa)
        self.__controleServer.setMesa(self.__mesa)
        self.__controleJogo.gerenciarJogo()

    def desligar(self):
        self.__interRede.serverEnd()

