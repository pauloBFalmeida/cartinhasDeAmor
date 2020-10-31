# coding: utf-8
from codigo.interfaceRede import InterfaceRede
from codigo.jogador import Jogador

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

    def __enviarChat(self, texto):
        self.interRede.enviar(self.host_ip, texto)

    def conectarHost(self):
        self.interRede.conectarHost(self.host_ip)
        self.interRede.enviar(self.host_ip, ":getId")
        id = self.interRede.receber()
        if not id:
            id = 0
        return id

    def enviarJogador(self, j):
        texto = ":jogador" +                    \
                "\id" + msg.getId() +         \
                "\n" + jogador.getNome() +     \
                "\c" + j.getCor() +          \
        self.interRede.enviar(self.host_ip, texto)
        
