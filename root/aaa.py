#hi

import os
import sys
import random
import pygame
from pygame.locals import *

print(os.getcwd())
print('hi')


pygame.init()

black = pygame.Color(0, 0, 0)         # Black
white = pygame.Color(255, 255, 255)   # White
grey = pygame.Color(128, 128, 128)   # Grey
red = pygame.Color(255, 0, 0)       # Red


FPS = pygame.time.Clock()
FPS.tick(60) # this goes inside the loop and it stalls in real time, it is not a parameter
fps = 60


k = 80

surf1 = pygame.display.set_mode((10*k, 10*k))
surf1.fill(black)
pygame.display.set_caption("Example")


class Chessboard(pygame.Surface):

    def __init__(self, size = (k*8, k*8)):
        super().__init__(size)
        c = [white, grey]
        for i in range(k*8):
            for j in range(k*8):
                    x = ((j // k % 2) + (i // k % 2)) % 2
                    self.set_at( (i, j), c[x] )



while True:

    FPS.tick(10)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5


P1 = Player()


sys.exit()

E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    P1.update()
    E1.move()

    DISPLAYSURF.fill(white)
    P1.draw(DISPLAYSURF)
    #E1.draw(DISPLAYSURF)

    pygame.display.update()
    FPS.tick(fps)




newGame = Game()

newGame.board = newGame.getEmptyBoard()

position = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'



#while True:
#    chessboard.display.start(position)

#display.terminate()


#newGame.showBoard()



