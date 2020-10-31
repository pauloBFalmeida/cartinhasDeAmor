# coding: utf-8
import pygame
from codigo.mesa import Mesa
from codigo.jogador import Jogador
from codigo.controleJogo import ControleJogo
from codigo.interfaceTexto import InterfaceTexto
from codigo.interfaceMasterMind import InterfaceMasterMind

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
		#self.FPS = 30

		#self.background = (0,0,50)
		
		self.__interfaceUsuario = InterfaceTexto()
		self.__interfaceRede = InterfaceMasterMind()
		self.controleJogo = ControleJogo(self.__interfaceUsuario, self.__interfaceRede)
		self.cores = [	(200,200,200),
						(200,100,100),
						(100,0,0),
						(100,200,100),
						(0,100,0),
						(100,100,200),
						(0,0,100)	]

	def main(self):
		self.preparativos()
		self.start()	# start game
		self.clock.tick(self.FPS)
		# loop
		while game.rodando:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game.rodando = False

			self.input(pygame.key.get_pressed())
			self.logic()
			self.render(game.win)

	#def criarJogoHost(self):
	#	self.mesa = Mesa(1)
	#	# criar jogador
	#	id = 0
	#	nome = self.__interfaceUsuario.nomeJogador(id)
	#	j = Jogador(id, nome, self.cores[id])
	#	self.mesa.addJogador(j)
	#	# 
	#	self.controleJogo.setMesa(self.mesa)
	#	self.controleRede = ControleRede(interfaceRede, True)
	#	self.__interfaceUsuario.addChat('ip: '+self.ControleRede.getIp())
		
	#	for id in range(1, self.__interfaceUsuario.numeroJogadores()):
	#		ip = self.__interfaceUsuario.entrarIpJogador()
	#		self.controleRede.addJogadorIdIp(id, ip)

	def entrarJogo(self):
		self.controleRede = ControleRede(interfaceRede, False)
		if self.__online:
			host_ip = self.__interfaceUsuario.entrarIpHost()
		else:
			host_ip = "localhost"
		self.controleRede.setHostIp(host_ip)
		id = self.controleRede.conectarHost()
		# criar jogador
		nome = self.__interfaceUsuario.nomeJogador(id)
		j = Jogador(id, nome, self.cores[id])
		# 
		self.controleRede.enviarJogador(j)

	def preparativos(self):
		self.__online = self.__interfaceUsuario.entrarOnline()
		entrarPartida = self.__interfaceUsuario.entrarPartida()
		if entrarPartida:
			self.entrarJogo()


	def start(self):
		self.controleJogo.gerenciarJogo()

	#def input(self, keys):
	#	if keys[pygame.K_ESCAPE]:
	#		self.rodando = False
	#	
	#def logic(self):
	#	pass

	#def render(self, window):
	#	window.fill(self.background)		# background
	#	pygame.display.update()				# update screen

