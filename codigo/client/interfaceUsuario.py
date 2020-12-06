# coding: utf-8
import abc
from sys import path
path.append('codigo')
from jogador import Jogador
from carta import Carta

class InterfaceUsuario(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def numeroJogadores(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def nomeJogador(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def esperarPartida(self) -> list:
        raise NotImplementedError
    
    @abc.abstractmethod
    def entrarIpHost(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def addChat(self, texto: str):
        raise NotImplementedError

    @abc.abstractmethod
    def iniciarRound(self):
        raise NotImplementedError

    @abc.abstractmethod
    def apresentarGanhadorDoJogo(self, jg_nome: str, jg_pontos: int):
        raise NotImplementedError

    @abc.abstractmethod
    def apresentarGanhadorDoRound(self, jg_nome: str, jg_pontos: int):
        raise NotImplementedError

    @abc.abstractmethod
    def anunciarCompararCartas(self):
        raise NotImplementedError

    @abc.abstractmethod
    def compararCartas(self, set_m: tuple,  set_j: tuple, ganhador_j: bool):
        raise NotImplementedError
    
    @abc.abstractmethod
    def anunciarCarta(self, j_nome: str, c_nome: str):
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaJogador(self, j_origem: Jogador, jogadores: list, siMesmo: bool, textoInicio: str) -> Jogador:
        raise NotImplementedError

    @abc.abstractmethod
    def selecionaValorGuarda(self):
        raise NotImplementedError

    @abc.abstractmethod
    def jogadorEscolherCarta(self, cartasMao_tipos: list) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def alertarSobreCondessa(self):
        raise NotImplementedError

    @abc.abstractmethod
    def anunciarMorto(self, j_nome: str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoGuarda(self, resultadoAcusacao: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPadre(self, c_nome: str):
        raise NotImplementedError
    
    @abc.abstractmethod
    def resultadoBarao(self, j_nome: str):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoAia(self, j_nome: str):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincipe(self, j_nome: str):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoRei(self, j1_nome: str, j2_nome: str):
        raise NotImplementedError

    @abc.abstractmethod
    def resultadoPrincesa(self, j_nome: str):
        raise NotImplementedError