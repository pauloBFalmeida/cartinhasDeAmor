# coding: utf-8
import pygame
#from threading import Thread
from sys import path
path.append('codigo')
from jogador import Jogador
from server.server import Server
from server.interfaceMasterMind import InterfaceMasterMind
from client.controleCliente import ControleCliente
from client.interfaceTexto import InterfaceTexto

# classe que comunica o controle com as interfaces
class CartinhaDeAmor:

    def __init__(self): #, width, height, title):
        #self.width = width
        #self.height = height
        #self.win = pygame.display.set_mode((width, height))
        #pygame.display.set_caption(title)
        #icon = pygame.image.load("icone.png")
        #pygame.display.set_icon(icon)

        #self.clock = pygame.time.Clock()
        #self.rodando = True
        #self.FPS = 30

        #self.background = (0,0,50)
        
        self.__interfaceUsuario = InterfaceTexto()
        self.__interfaceRede = InterfaceMasterMind()
        self.cores = [(200,200,200),
                      (200,100,100),
                      (100,0,0),
                      (100,200,100),
                      (0,100,0),
                      (100,100,200),
                      (0,0,100)]

    def main(self):
        self.preparativos()
        self.start()    # start game

        #self.clock.tick(self.FPS)
        ## loop
        #while game.rodando:
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            game.rodando = False

        #    self.input(pygame.key.get_pressed())
        #    self.logic()
        #    self.render(game.win)

    # criar server 
    def criarServer(self):
        #class ServerThread(Thread):
        #    def __init__ (self, server):
        #        Thread.__init__(self)
        #        self.__server = server

        #    def run(self, nJogadores):
        #        self.__server.start()
        #        self.__server.esperarEntrarJogadores(nJogadores)
        #        # esperar todos se conectarem

        ##
        #self.__server = Server()
        #nJogadores = self.__interfaceUsuario.numeroJogadores()
        #self.__serverThread = ServerThread(self.__server)
        #self.__serverThread.run(nJogadores) 

        
        self.__server = Server()
        nJogadores = self.__interfaceUsuario.numeroJogadores()
        self.__server.start()
        self.__server.esperarEntrarJogadores(nJogadores)
        self.__server.iniciarJogo()

    def entrarJogo(self):
        if self.__online:
            host_ip = self.__interfaceUsuario.entrarIpHost()
        else:
            host_ip = "localhost"
        self.__controleCliente = ControleCliente(self.__interfaceRede, self.__interfaceUsuario)
        self.__controleCliente.setHostIp(host_ip)
        self.__controleCliente.conectarServer()
        # criar jogador
        #id = self.__controleCliente.getId()
        id = 0
        nome = self.__interfaceUsuario.nomeJogador(id)
        j = Jogador(id, nome, self.cores[id])
        self.__controleCliente.sendJogador(j)
        #
        self.__controleCliente.main()
        #
        self.fim()

    def preparativos(self):
        self.__online = self.__interfaceUsuario.entrarOnline()
        self.__criarServer   = self.__interfaceUsuario.criarServer()
        if self.__criarServer:
            self.criarServer()
        else:
            entrarPartida = self.__interfaceUsuario.entrarPartida()
            if entrarPartida:
                self.entrarJogo()


    def start(self):
        #self.__controleJogo.gerenciarJogo()
        pass

    def fim(self):
        if self.__criarServer:
            self.__serverThread.join()
            self.__server.desligar()
        self.__controleCliente.desligar()



    #def input(self, keys):
    #    if keys[pygame.K_ESCAPE]:
    #        self.rodando = False
    #    
    #def logic(self):
    #    pass

    #def render(self, window):
    #    window.fill(self.background)        # background
    #    pygame.display.update()                # update screen

