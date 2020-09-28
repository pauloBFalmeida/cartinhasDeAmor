# coding: utf-8
import pygame
pygame.init()

class CartinhaDeAmor:

	def __init__(self, width, height, title):
		self.width = width
		self.height = height
		self.win = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)
		#icon = pygame.image.load("icone.png")
		#pygame.display.set_icon(icon)

		self.clock = pygame.time.Clock()
		self.rodando = True
		self.FPS = 30

		self.background = (0,0,50)


	def start(self):
		pass

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
		game.render(game.win)

if __name__ == "__main__":
	main()
	pygame.quit()
	quit()
