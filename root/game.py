# hi
import c
import os
import sys
import random
import pygame
from pygame.locals import *
import mySprites
import mySurfaces



class Game(object):
	# variables
	name = "[game.Game]: "
	foo = "bar"
	fps = 4
	k = c.k

	def msg(self, arg):

		print(self.__repr__() , arg)


	def __init__(self):
		self.msg("Initialising")


	def run(self):
		
		
		pygame.init()
		self.surf1 = pygame.display.set_mode( (10 * self.k, 10 * self.k) )
		self.surf1.fill(c.black)
		pygame.display.set_caption("Chess game")

		
		self.msg( "Running...")

		global c1					# chessboard surface
		#   initialize chessboard
		c1 = mySurfaces.Chessboard()
		self.surf1.blit(c1, (self.k, self.k)) 		# draw board on position (k,k)


		#   initialise pieces
		global p1
		global r1
		p1 = mySprites.Piece()
		r1 = p1.image.get_rect(x=self.k * 7, y=self.k * 1)


		#self.surf1.blit(p1.image, (self.k * 4, self.k * 5))
		self.surf1.blit(p1.image, r1)
		
		global v
		v = self.k
		
		self.loop(99)
		
		
		




	def loop(self, n ):
		
		v = self.k
		for i in range(n):

			self.surf1.fill(c.black)
			c1 = mySurfaces.Chessboard()
			self.surf1.blit(c1, (self.k, self.k))

			# v = -v
			
			# r1.x += v



			self.surf1.blit(p1.image, r1)

			pygame.time.Clock().tick(self.fps)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == QUIT:
					self.msg("Terminated")
					pygame.quit()
					sys.exit()


y = "asdf"
x = Game()
x.run()

