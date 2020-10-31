from Mastermind import *
from chat import *
from controleJogo import *

class Server(MastermindServerTCP):

    def __init__(self):
        self.__chat = chat.Chat()
        self.__jogo = controlejogo.ControleJogo()

        #tem alguns argumentos possíveis de avaliar
        MastermindClientTCP.__init__(self)

    def criar_bot(self):
        pass

    def callback_client_handle(self, connection_obj, data):
        if data.find('msg') != -1:
            ## lidar no chat
            msg = data.split(":")
            new_msg = Mensagem(user_origem=msg[1], cor=msg[2], texto=msg[3])
            self.__chat.adicionar_mensagem(new_msg)
            self.callback_client_send(connection_obj, self.__chat.get_mensagens())
        elif data.find('cmd') != -1:
            # segunda posição da mensagem enviada é a função que deve ser executada
            cmd = data.split(':')[1]
            if cmd == 'compararCartas':
                self.__jogo.iniciarRound()