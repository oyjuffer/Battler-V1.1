

### MAIN MENU STATE ###

# IMPORT LIBRARIES
import os 
import pygame

# IMPORT GAME FILES
from .. import constants
from .. import control
from .. import setup




class Main_Menu():
	def __init__(self):
		self.running = False

	def setup(self):
		self.menu_location = [1, 1]
	
	def events(self):
		pass
	
	def update(self):
		pass
	
	def draw(self):
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [0, 350, 250, 250])

	def running(self):
		pass

