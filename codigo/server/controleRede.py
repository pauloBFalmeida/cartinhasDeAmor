# coding: utf-8
from sys import path
path.append('codigo')
from jogador import Jogador
from chat import Mensagem
from server.interfaceRede import InterfaceRede

class ControleRede():

    def __init__(self, interfaceRede, meuIp=None):
        self.interRede = interfaceRede
        self.meuIp = meuIp if meuIp else self.interRede.getIp()

    def getIp(self):
        return self.meuIp

    def setHostIp(self, ip):
        self.host_ip = ip

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        texto = ":msg" +                          \
                "\d" + msg.get_data() +         \
                "\j" + jogador.get_nome() +     \
                "\c" + msg.get_cor() +          \
                "\t" + msg.get_texto()
        self.__enviarChat(texto)

    def conectarHost(self):
        self.interRede.conectarHost(self.host_ip)
        self.interRede.enviar(self.host_ip, ":getId")
        id = self.interRede.receber()
        if not id:
            id = 0
        return id

    def enviarJogador(self, j):
        dado = ["cmd:jogador", j]
        self.interRede.enviar(self.host_ip, dado)
        
    def __enviarChat(self, texto):
        self.interRede.enviar(self.host_ip, texto)
