# coding: utf-8
from codigo.interfaceRede import InterfaceRede

class ControleRede():

    def __init__(self, interfaceRede):
        self.__interRede = interfaceRede
        self.__meuIp = self.__interRede.getIp()

    def enviarMsgChat(self, msg):
        pass
