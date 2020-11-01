#from interfaceMasterMindServer import InterfaceMasterMindServer
#from chat_server import ServerChat
from interfaceMasterMind import InterfaceMasterMind
import time, socket

class Server():

    def __init__(self):
        self.__ip = 'localhost'
        self.__interRede = InterfaceMasterMind()
        self.__interRede.startServer('localhost')

    def main(self):
        self.testeCliente()
        time.sleep(1)
        reply = None
        while reply == None:
            #self.__interRede.enviarLista("localhost", [1,2,3])
            reply = self.__interRede.serverReceber()
        print(reply)
        self.testeServerEnvia()
        time.sleep(1)
        reply = None
        while reply == None:
            #self.__interRede.enviarLista("localhost", [1,2,3])
            reply = self.__interRede.clienteReceber()
        print(reply)
    
    def testeCliente(self):
        self.interC = InterfaceMasterMind()
        self.interC.startClient('localhost')

    def testeEnd(self):
        self.interC.clienteEnd()
        self.__interRede.serverEnd()

    def testeServerEnvia(self):
        self.__interRede.serverEnviar("mensagem")

s = Server()
s.main()
s.testeEnd()
print('fim')
    