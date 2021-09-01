import os
import sys
import random
import pygame
from pygame.locals import *
import c




SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5



class Piece(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("sprites/white_queen.png")
		self.image = pygame.transform.scale(self.image, (c.k, c.k))
		self.image.fill(c.red)
		self.image.set_colorkey(None) 			# can be removed, specify which color turns transparent
		#self.surf = pygame.Surface((k, k))
		#self.rect = self.surf.get_rect()

	def __repr__(self):
		return 'Chess Piece Sprite'








class Ball(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("sprites/car.jpg")
		self.surf = pygame.Surface((50, 50))
		self.rect = self.surf.get_rect()






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



