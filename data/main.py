

### MAIN ###

# IMPORT LIBRARIES
import os 
import pygame

# IMPORT GAME FILES
from . import constants
from . import setup

# CLASSES
class Control():
	def __init__(self):
		self.running 	= True
		self.clock 		= pygame.time.Clock()
		self.fps		= 60

	def eventloop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def mainloop(self):
		while self.running:
			self.eventloop() 
			pygame.display.update()
			self.clock.tick(self.fps)


# FUNCTIONs 


def main():
	game = Control()

	game.mainloop()
