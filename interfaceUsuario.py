# coding: utf-8
import abc
import jogador
import carta

class InterfaceUsuario(metaclass=abc.ABCMeta):

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
    def apresentarGanhadorDoJogo(self, j_ganhador: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def apresentarGanhadorDoRound(self, j_ganhador: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def compararCartas(self, j_ganhador: jogador, jogadores: list):
        raise NotImplementedError
    
    @abc.abstractmethod
    def jogarCarta(self, j: jogador, c: carta):
        raise NotImplementedError

    @abc.abstractmethod
    def jogadorEscolherCarta(self, j_origem: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaJogador(self, j_origem: jogador, jogadores: list, siMesmo: bool, textoInicio: str) -> jogador:
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaValorGuarda(self):
        raise NotImplementedError

    @abc.abstractmethod
    def jogadorEscolheCarta(self, j_origem: jogador) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def alertarSobreCondessa(self):
        raise NotImplementedError

    @abc.abstractmethod
    def anunciarMorto(self, j_origem: jogador):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoGuarda(self, resultadoAcusacao: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPadre(self, cartaMao: carta):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoBarao(self, jogadorMorto: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoAia(self, j: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincipe(self, j: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoRei(self, j1: jogador, j2: jogador):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincesa(self, j: jogador):
        raise NotImplementedError
