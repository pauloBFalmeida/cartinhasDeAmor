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
from server.interfaceMasterMind import *   #InterfaceMasterMind

class Server():

    def __init__(self):
        self.__interRede = InterfaceMasterMind()
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

    def __processar(self):
        self.__nJogadores = self.__interRede.getNConectados()

    def iniciarJogo(self):
        self.__mesa = Mesa(0)
        for j in self.__jogadores:
            self.__mesa.addJogador(j)
        self.__controleJogo.setMesa(self.__mesa)
        self.__controleJogo.gerenciarJogo()

    def main(self):
        pass

    def desligar(self):
        self.__interRede.serverEnd()


#class Server():
#
#    def __init__(self):
#        self.__ip = 'localhost'
#        self.__interRede = InterfaceMasterMind()
#        self.__interRede.startServer('localhost')

#    def testeServer1(self):
#        time.sleep(1)
#        reply = None
#        while not reply:
#            reply = self.__interRede.serverReceber()
#        print(reply)
    
#    def teste2(self):
#        self.__interRede.serverEnviar('127.0.0.1', "mensagezeinhaa")

#    def testeEnd(self):
#        self.__interRede.serverEnd()

#class Cliente():
#    def __init__(self):
#        self.interC = InterfaceMasterMind()
#        self.interC.startClient('localhost')

#    def testeCliente1(self):
#        self.interC.clienteEnviar([1,2,3])

#    def teste2(self):
#        time.sleep(1)
#        reply = None
#        while not reply:
#            reply = self.interC.clienteReceber()
#        print(reply)

#    def testeEnd(self):
#        self.interC.clienteEnd()
        

#s = Server()
#c = Cliente()
#print("Cliente envia pro server")
#c.testeCliente1()
#s.testeServer1()

#print("Server envia pro cliente")
#s.teste2()
#c.teste2()

#c.testeEnd()
#s.testeEnd()
#print('fim')
    