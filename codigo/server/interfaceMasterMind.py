# coding: utf-8
#from sys import path
#path.append('codigo')
#from server.interfaceRede import InterfaceRede
#from server.Mastermind import *

from interfaceRede import InterfaceRede
from Mastermind import *
from urllib.request import urlopen

class InterfaceMasterMind(InterfaceRede):

    def __init__(self):
        meuIp = "localhost"
        self.__port = 6317

    def startClient(self, ip):
        class Client(MastermindClientTCP):
            def __init__(self):
                self.respostas = []
                MastermindClientTCP.__init__(self,
                                            1.0,    # timeout_connect
                                            1.0)    # timeout_receive
            def callback_client_handle(self, connection_object,data):
                self.respostas.append(data)

        self.__client = Client()
        self.__ipHost = ip
        self.__client.connect(ip, self.__port)

    
    def startServer(self, ip):
        #class Server(MastermindServerCallbacksEcho,MastermindServerCallbacksDebug,MastermindServerTCP):
        class Server(MastermindServerTCP):
            def __init__(self):
                self.respostas = []
                MastermindServerTCP.__init__(self,
                                            0.5,   # server refresh
                                            0.5,   # connections refresh
                                            5.0)  # connection timeout
            def callback_client_handle(self, connection_object,data):
                self.respostas.append(data)

        self.__server = Server()
        self.__server.connect(ip, self.__port)
        self.__server.accepting_allow()
        
    def serverReceber(self):
        if len(self.__server.respostas) > 0:
            r = self.__server.respostas.pop()
            print('resposta')
            print(r)

    def clienteReceber(self):
        self.__client.receive(True)

    def clienteEnd(self):
        self.__client.disconnect()

    def serverEnd(self):
        self.__server.accepting_disallow()
        self.__server.disconnect_clients()
        self.__server.disconnect()


    def getIp(self) -> str:
        external_ip_v4 = urlopen('https://v4.ident.me/').read().decode('utf8')
        return external_ip_v4
    
    def enviar(self, ip: str, texto: str):
        pass
    
    def enviarLista(self, ip: str, lista: list):
        self.__client.send(lista,None)

    def receber(self) -> str:
        return ""
    
    def conectarHost(self, ip: str) -> bool:
        return True