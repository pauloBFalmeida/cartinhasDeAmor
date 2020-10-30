# Feito por Paulo Almeida e Pedro Aquino

import pygame
from codigo.cartinhaDeAmor import CartinhaDeAmor


if __name__ == "__main__":
    pygame.init()
    game = CartinhaDeAmor()
    game.main()
    pygame.quit()
    quit()
