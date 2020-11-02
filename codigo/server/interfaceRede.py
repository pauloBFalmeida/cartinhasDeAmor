# coding: utf-8
import abc

class InterfaceRede(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getIp(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def serverEnviar(self, ip: str, texto: str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def clienteEnviar(self, ip: str, message: list):
        raise NotImplementedError

    @abc.abstractmethod
    def serverReceber(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def clienteReceber(self) -> str:
        raise NotImplementedError
    