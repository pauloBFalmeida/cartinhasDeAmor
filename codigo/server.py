from Mastermind import *
from chat import *
from controleJogo import *

class Server(MastermindServerTCP):

    def __init__(self):
        self.__chat = Chat()
        self.__jogo = ControleJogo()

        #tem alguns argumentos possíveis de avaliar
        MastermindClientTCP.__init__(self)

    def criar_bot(self):
        pass