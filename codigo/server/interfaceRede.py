# coding: utf-8
import abc

class InterfaceRede(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getIp(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def startClient(self, ip):
        raise NotImplementedError
    
    @abc.abstractmethod
    def clienteReceber(self) -> list:
        raise NotImplementedError
        
    @abc.abstractmethod
    def clienteEnviar(self, lista: list):
        raise NotImplementedError
        
    @abc.abstractmethod
    def clienteEnd(self):
        raise NotImplementedError
        
    @abc.abstractmethod
    def startServer(self, ip: str):
        raise NotImplementedError
        
    @abc.abstractmethod
    def getJogadores_ip(self) -> dict:
        raise NotImplementedError
        
    @abc.abstractmethod
    def findConnectionObject(self, ip: str):
        raise NotImplementedError
        
    @abc.abstractmethod
    def getNConectados(self) -> int:
        raise NotImplementedError
        
    @abc.abstractmethod
    def serverReceber(self) -> list:
        raise NotImplementedError
        
    @abc.abstractmethod
    def serverEnviar(self, ip: str, lista: list):
        raise NotImplementedError
        
    @abc.abstractmethod
    def serverEnd(self):
        raise NotImplementedError
