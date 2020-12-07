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

        self.__client = Client()
        self.__ipHost = ip
        self.__client.connect(ip, self.__port)
    
    def clienteReceber(self) -> list:
        self.__client.receive()
        if len(self.__client.respostas) > 0:
            return self.__client.respostas.pop()

    def clienteEnviar(self, lista: list):
        #print(lista)
        self.__client.send(lista, None)

    def clienteEnd(self):
        self.__client.disconnect()

# ================ Server ======================

    def startServer(self, ip: str):
        #class Server(MastermindServerCallbacksEcho,MastermindServerCallbacksDebug,MastermindServerTCP):
        class Server(MastermindServerTCP):
            def __init__(self):
                self.respostas = []
                self.respostas_id = []
                self.nConectados = -1
                self.jogadores_ip = {}
                self.connection_objects = {}
                self.sem = threading.Semaphore(0)
                MastermindServerTCP.__init__(self,
                                            0.5,   # server refresh
                                            0.5,   # connections refresh
                                            60.0)  # connection timeout
            def callback_client_handle(self, connection_object, data):
                #print('callback_client_handle')
                #print(data)
                self.respostas.append(data)
                self.respostas_id.append( (data, self.__findId(connection_object)) )
                self.sem.release()
                return super(MastermindServerTCP,self).callback_client_handle(connection_object,data)

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

            def __findId(self, connection_object):
                ip_desejado = None
                for ip in self.connection_objects:
                    if self.connection_objects[ip] == connection_object:
                        ip_desejado = ip
                #
                id_desejado = None
                for id in self.jogadores_ip:
                    if self.jogadores_ip[id] == ip_desejado:
                        id_desejado = id
                #
                return id_desejado

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
        self.__server.sem.acquire()
        if len(self.__server.respostas) > 0:
            r = self.__server.respostas.pop()
        return r

    def serverReceberId(self) -> list:
        r = None
        self.__server.sem.acquire()
        if len(self.__server.respostas_id) > 0:
            r = self.__server.respostas_id.pop()
        return r

    def serverEnviar(self, ip: str, lista: list):
        ## formato do dict de conexoes do server: 
        ## {(ip, port) : MastermindConnectionThreadTCP obj}
        connection_object = self.__server.connection_objects[ip]
        self.__server.callback_client_send(connection_object, lista)
    
    def serverEnd(self):
        self.__server.accepting_disallow()
        self.__server.disconnect_clients()
        self.__server.disconnect()
