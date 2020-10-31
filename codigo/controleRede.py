# coding: utf-8
from codigo.interfaceRede import InterfaceRede
from codigo.jogador import Jogador

class ControleRede():

    def __init__(self, interfaceRede, chat, host=False):
        self.interRede = interfaceRede
        self.chat = chat
        self.host = host
        self.jogadores_ips = {}
        self.meuIp = self.interRede.getIp()

    def getIp(self):
        return self.meuIp

    def addJogadorIdIp(self, id, ip):
        self.jogadores_ips[id] = ip

    def setHostIp(self, ip):
        self.host_ip = ip

    def enviarMsgChat(self, msg):
        jogador = msg.get_origem()
        texto = "\m" +                          \
                "\d" + msg.get_data() +         \
                "\j" + jogador.get_nome() +     \
                "\c" + jogador.get_cor() +          \
                "\t" + msg.get_texto()
        self.__enviarChat(texto)

    def __enviarChat(self, texto):
        if self.host:
            for id in self.jogadores_ips:
                ip = self.jogadores_ips[id]
                self.interRede.enviar(ip, texto)
        else:
            self.interRede.enviar(self.host_ip, texto)

        
