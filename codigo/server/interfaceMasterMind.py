# coding: utf-8
import threading
from sys import path
path.append('codigo')
from server.interfaceRede import InterfaceRede
from server.Mastermind import *


class InterfaceMasterMind(InterfaceRede):

    def __init__(self):
        self.__port = 6317

    def getIp(self) -> str:
        external_ip_v4 = urlopen('https://v4.ident.me/').read().decode('utf8')
        return external_ip_v4

# ================ Cliente ======================

    def startClient(self, ip):
        class Client(MastermindClientTCP):
            def __init__(self):
                self.respostas = []
                MastermindClientTCP.__init__(self,
                                            5.0,    # timeout_connect
                                            60.0)    # timeout_receive
            # esse aqui não existe
            #def callback_client_handle(self, connection_object,data):
            #    self.respostas.append(data)
            def receive(self):
                self.respostas.append(super(Client, self).receive(True))


        self._lock = threading.Lock()
        self.__client = Client()
        self.__ipHost = ip
        self.__client.connect(ip, self.__port)
    
    def clienteReceber(self) -> list:
        #if len(self.__client.respostas) > 0:
        #    print(self.__client.respostas)
        #    reply = self.__client.respostas.pop()
        #return reply
        self._lock.acquire()
        self.__client.receive()
        self._lock.release()
        return self.__client.respostas.pop()

    def clienteEnviar(self, lista: list):
        self.__client.send(lista, None)

    def clienteEnd(self):
        self.__client.disconnect()

# ================ Server ======================

    def startServer(self, ip: str):
        #class Server(MastermindServerCallbacksEcho,MastermindServerCallbacksDebug,MastermindServerTCP):
        class Server(MastermindServerTCP):
            def __init__(self):
                self.respostas = []
                self.nConectados = -1
                self.jogadores_ip = {}
                self.connection_objects = {}
                MastermindServerTCP.__init__(self,
                                            0.5,   # server refresh
                                            0.5,   # connections refresh
                                            60.0)  # connection timeout
            def callback_client_handle(self, connection_object,data):
                self.respostas.append(data)

            def callback_connect_client(self, connection_object):
                self.nConectados += 1
                # add ao self.jogadores_ip 
                ip = connection_object.address
                self.jogadores_ip[self.nConectados] = ip
                self.connection_objects[ip] = connection_object
                # retorno padrao
                return super(MastermindServerTCP,self).callback_connect_client(connection_object)

            def callback_disconnect_client(self, connection_object):
                self.nConectados -= 1
                # remove do self.jogadores_ip
                ip = connection_object.address
                id_rem = -1
                for id in self.jogadores_ip:
                    if self.jogadores_ip[id] == ip:
                        id_rem = id
                self.jogadores_ip.pop(id_rem, None)
                # retorno padrao
                return super(MastermindServerTCP,self).callback_disconnect_client(connection_object)

        self.__server = Server()
        # {ip : MastermindClientThreadTCP} --> acabou que nao fiz assim
        # self.__clientes = {}
        self.__server.connect(ip, self.__port)
        self.__server.accepting_allow()

    def getJogadores_ip(self) -> dict:
        return self.__server.jogadores_ip

    def findConnectionObject(self, ip: str):
        # nao queria mexer tanto com o negocio, então tem essa solucao aqui :p
        clientes = self.__server._mm_connections
        for key in clientes:
            if key[0] == ip:
                return clientes[key]

    def getNConectados(self) -> int:
        return self.__server.nConectados

    def serverReceber(self) -> list:
        r = None
        if len(self.__server.respostas) > 0:
            r = self.__server.respostas.pop()
        return r

    def serverEnviar(self, ip: str, lista: list):
        ## formato do dict de conexoes do server: 
        ## {(ip, port) : MastermindConnectionThreadTCP obj}

        #connection_object = self.findConnectionObject(ip)
        connection_object = self.__server.connection_objects[ip]
        self.__server.callback_client_send(connection_object, lista)
    
    def serverEnd(self):
        self.__server.accepting_disallow()
        self.__server.disconnect_clients()
        self.__server.disconnect()
