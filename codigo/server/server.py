#from interfaceMasterMindServer import InterfaceMasterMindServer
#from chat_server import ServerChat

#from interfaceMasterMind import InterfaceMasterMind
#import time
#import socket

#from sys import path
#path.append('codigo')
#from jogador import Jogador

from sys import path
path.append('codigo')
from mesa import Mesa
from server.controleJogo import ControleJogo
from server.controleServer import *        #ControleServer
from server.interfaceMasterMind import *   #InterfaceMasterMind

class Server():

    def __init__(self):
        self.__interfaceRede = InterfaceMasterMind()
        self.__controleServer = ControleServer(self.__interfaceRede, "localhost")
        self.__controleJogo = ControleJogo(self.__controleServer)

    def start(self):
        self.__mesa = Mesa(0)
        self.__controleJogo.setMesa(self.__mesa)
        self.__controleJogo.gerenciarJogo()




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
    