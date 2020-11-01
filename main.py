# Feito por Paulo Almeida e Pedro Aquino

import pygame
from codigo.cartinhaDeAmor import CartinhaDeAmor
from codigo.server.server import Server


if __name__ == "__main__":
    pygame.init()
    if input('s para rodar o server: ') == 's':
        server = Server()
        input('digite para iniciar o server')
        server.start()
    else:
        game = CartinhaDeAmor()
        game.main()
    pygame.quit()
    quit()
