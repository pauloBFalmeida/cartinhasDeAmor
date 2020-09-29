# coding: utf-8
import pygame
from mesa import *
from jogador import *

pygame.init()

class CartinhaDeAmor:

	def __init__(self, width, height, title):
		self.width = width
		self.height = height
		#self.win = pygame.display.set_mode((width, height))
		#pygame.display.set_caption(title)
		#icon = pygame.image.load("icone.png")
		#pygame.display.set_icon(icon)

		self.clock = pygame.time.Clock()
		self.rodando = True
		self.FPS = 30

		self.background = (0,0,50)


	def start(self):
		self.mesa = Mesa(1)
		for i in range(int(input('numero de jogadores\n'))):
			self.mesa.addJogador(Jogador(i, input('nome do jogador '+str(i)+'\n'), 0))
		self.mesa.iniciarPartida()

	def input(self, keys):
		if keys[pygame.K_ESCAPE]:
			self.rodando = False
		
	def logic(self):
		pass

	def render(self, window):
		window.fill(self.background)		# background
		pygame.display.update()				# update screen


def main():
	game = CartinhaDeAmor(800, 600, "CartinhaDeAmor")
	game.start()	# start game
	# loop
	while game.rodando:
		game.clock.tick(game.FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game.rodando = False
				
		game.input(pygame.key.get_pressed())
		game.logic()
		#game.render(game.win)

if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
