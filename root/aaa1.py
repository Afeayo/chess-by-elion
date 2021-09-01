#hi
import os
import sys
import random
import chessboard
from chessboard import display
from game import *
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




c1 = Chessboard()
surf1.blit(c1, (k,k))


p1 = Piece()
surf1.blit( p1.image, (k*4, k*5) )

b1 = Ball()

print(b1.rect)

# surf1.blit(b1.surf, (100,100 ))


while True:

    FPS.tick(10)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()





# pygame.draw.line(DISPLAYSURF, grey, (150, 130), (130, 170))
# pygame.draw.line(DISPLAYSURF, grey, (150, 130), (170, 170))
# pygame.draw.line(DISPLAYSURF, grey, (130, 170), (170, 170))
# pygame.draw.circle(DISPLAYSURF, black, (100, 50), 30)
# pygame.draw.circle(DISPLAYSURF, black, (200, 50), 30)
# pygame.draw.rect(DISPLAYSURF, red, (100, 200, 100, 50), 2)
# pygame.draw.rect(DISPLAYSURF, black, (110, 260, 80, 5))






SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/pawn.jpg")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center=(random.randint(40, 360), 0))

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.jpg")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



P1 = Player()

print(P1.rect)

print('hi')
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



