#from interfaceMasterMindServer import InterfaceMasterMindServer
#from chat_server import ServerChat
from interfaceMasterMind import InterfaceMasterMind
import time

class Server():

    def __init__(self):
        self.__ip = 'localhost'
        self.__interRede = InterfaceMasterMind()
        self.__interRede.startServer('localhost')

    def main(self):
        time.sleep(1)
        reply = None
        while reply == None:
            #self.__interRede.enviarLista("localhost", [1,2,3])
            reply = self.__interRede.serverReceber()
            
        
    def testeCliente(self):
        self.interC = InterfaceMasterMind()
        self.interC.startClient('localhost')
        self.interC.enviarLista('localhost', [1,2,3])

    def testeEnd(self):
        self.interC.clienteEnd()
        self.__interRede.serverEnd()
        

s = Server()
s.testeCliente()
s.main()

s.testeEnd()
print('fim')
    