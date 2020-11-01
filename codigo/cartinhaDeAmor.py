# coding: utf-8
import pygame
from sys import path
path.append('codigo')
from jogador import Jogador
from server.server import Server
from server.controleJogo import ControleJogo
from server.controleServer import ControleServer
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

        self.clock = pygame.time.Clock()
        self.rodando = True
        self.FPS = 30

        #self.background = (0,0,50)
        
        self.__interfaceUsuario = InterfaceTexto()
        self.__interfaceRede = InterfaceMasterMind()
        self.__controleServer = ControleServer(self.__interfaceRede, "localhost")
        self.controleJogo = ControleJogo(self.__controleServer)
        self.cores = [    (200,200,200),
                        (200,100,100),
                        (100,0,0),
                        (100,200,100),
                        (0,100,0),
                        (100,100,200),
                        (0,0,100)    ]

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
        self.__server = Server()
        self.__server.start()
        # esperar todos se conectarem
        self.__server.main()

    def entrarJogo(self):
        if self.__online:
            host_ip = self.__interfaceUsuario.entrarIpHost()
        else:
            host_ip = "localhost"
        self.controleCliente = ControleCliente(self.__interfaceRede, self.__interfaceUsuario)
        self.controleCliente.setHostIp(host_ip)
        # criar jogador
        id = 0
        nome = self.__interfaceUsuario.nomeJogador(id)
        j = Jogador(id, nome, self.cores[id])
        #
        self.controleCliente.conectarHost()
        self.controleCliente.main()

    def preparativos(self):
        self.__online = self.__interfaceUsuario.entrarOnline()
        criarServer   = self.__interfaceUsuario.criarServer()
        if criarServer:
            self.criarServer()
        entrarPartida = self.__interfaceUsuario.entrarPartida()
        if entrarPartida:
            self.entrarJogo()


    def start(self):
        pass
        #self.controleJogo.gerenciarJogo()

    #def input(self, keys):
    #    if keys[pygame.K_ESCAPE]:
    #        self.rodando = False
    #    
    #def logic(self):
    #    pass

    #def render(self, window):
    #    window.fill(self.background)        # background
    #    pygame.display.update()                # update screen

