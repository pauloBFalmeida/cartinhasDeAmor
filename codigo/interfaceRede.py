# coding: utf-8
import abc

class InterfaceRede(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getIp(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def enviar(self, ip: str, texto: str):
        raise NotImplementedError