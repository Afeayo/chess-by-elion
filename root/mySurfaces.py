import os
import sys
import random
import pygame
from pygame.locals import *
import c




class Chessboard(pygame.Surface):



    def __init__(self, size = (c.k*8, c.k*8)):
        super().__init__(size)
        g = [c.white, c.grey]
        for i in range(c.k*8):
            for j in range(c.k*8):
                    x = ((j // c.k % 2) + (i // c.k % 2)) % 2
                    self.set_at( (i, j), g[x] )


