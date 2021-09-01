# hi
import c
import os
import sys
import random
import pygame
from pygame.locals import *
import mySprites
import mySurfaces



# variables
name = "[game.Game]: "
foo = "bar"
fps = 4
k = c.k


self.msg("Initialising")
pygame.init()
self.surf1 = pygame.display.set_mode( (10 * self.k, 10 * self.k) )
self.surf1.fill(c.black)
pygame.display.set_caption("Chess game")
