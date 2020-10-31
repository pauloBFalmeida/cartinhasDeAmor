# coding: utf-8
from codigo.interfaceRede import InterfaceRede
from codigo.Mastermind import *
from urllib.request import urlopen

class InterfaceMasterMind(InterfaceRede):

    def getIp(self) -> str:
        external_ip_v4 = urlopen('https://v4.ident.me/').read().decode('utf8')
        return external_ip_v4
    
    def enviar(self, ip: str, texto: str):
        pass
    
    def receber(self) -> str:
        return ""
    
    def conectarHost(self, ip: str) -> bool:
        return True