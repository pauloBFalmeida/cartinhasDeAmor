from time import gmtime, strftime
# from Mastermind import *
import threading

class Mensagem:
    
    def __init__(self, user_origem, texto):
        # acho que a data deve ser criada quando a mensagem entrar no chat
        # self.__data = strftime("%H:%M:%S",gmtime())
        self.__origem = user_origem
        self.__texto = texto
    
    def set_data(self):
        self.__data = strftime("%H:%M:%S",gmtime())

    def get_data(self):
        return self.__data
    
    def get_origem(self):
        return self.__origem

    def get_texto(self):
        return self.__texto

class Chat:

    def __init__(self):
        self.mensagens = []
        self.mtx = threading.Lock()

    def adicionar_mensagem(self, msg):
        msg.set_data()

        self.mtx.acquire()
        self.mensagens.append(msg)
        self.mtx.release()

    def get_mensagens(self):
        return self.mensagens