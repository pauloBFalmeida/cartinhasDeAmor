# coding: utf-8
import pygame
from mesa import Mesa
from jogador import Jogador
from controleJogo import ControleJogo

pygame.init()

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
		
		self.controle = ControleJogo()


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


def main():
	game = CartinhaDeAmor()
	game.start()	# start game
	# loop
	#while game.rodando:
	#	game.clock.tick(game.FPS)

	#	for event in pygame.event.get():
	#		if event.type == pygame.QUIT:
	#			game.rodando = False
				
	#	game.input(pygame.key.get_pressed())
	#	game.logic()
	#	#game.render(game.win)

if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
