# coding: utf-8
import abc
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta

class InterfaceUsuario(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def entrarOnline(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def numeroJogadores(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def nomeJogador(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def iniciarRound(self):
        raise NotImplementedError

    @abc.abstractmethod
    def apresentarGanhadorDoJogo(self, j_ganhador: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def apresentarGanhadorDoRound(self, j_ganhador: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def compararCartas(self, j_ganhador: Jogador, jogadores: list):
        raise NotImplementedError
    
    @abc.abstractmethod
    def jogarCarta(self, j: Jogador, c: Carta):
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaJogador(self, j_origem: Jogador, jogadores: list, siMesmo: bool, textoInicio: str) -> Jogador:
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaValorGuarda(self):
        raise NotImplementedError

    @abc.abstractmethod
    def jogadorEscolherCarta(self, j_origem: Jogador) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def alertarSobreCondessa(self):
        raise NotImplementedError

    @abc.abstractmethod
    def anunciarMorto(self, j_origem: Jogador):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoGuarda(self, resultadoAcusacao: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPadre(self, cartaMao: Carta):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoBarao(self, jogadorMorto: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoAia(self, j: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincipe(self, j: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoRei(self, j1: Jogador, j2: Jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincesa(self, j: Jogador):
        raise NotImplementedError
        
    @abc.abstractmethod
    def entrarPartida(self) -> bool:
        raise NotImplementedError
    
    def entrarIpHost(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def addChat(self, texto: str):
        raise NotImplementedError