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
		self.controle = ControleJogo(self.__interfaceUsuario, self.__interfaceRede)

	def main(self):
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


	def start(self):
		self.mesa = Mesa(1)
		for i in range(self.controle.getNumeroJogadores()):
		#	self.mesa.addJogador(Jogador(i, self.controle.getNomeJogador(i), 0))
			self.mesa.addJogador(Jogador(i, 'j'+str(i), 0))
		self.controle.setMesa(self.mesa)
		self.controle.gerenciarJogo()

	#def input(self, keys):
	#	if keys[pygame.K_ESCAPE]:
	#		self.rodando = False
	#	
	#def logic(self):
	#	pass

	#def render(self, window):
	#	window.fill(self.background)		# background
	#	pygame.display.update()				# update screen

