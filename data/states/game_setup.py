

### GAME SETUP STATE ###

# IMPORT LIBRARIES
import os 
import pygame

# IMPORT GAME FILES
from .. import constants
from .. import control
from .. import setup


class Game_Setup():
	def __init__(self):
		self.running 		= False
		self.state 			= None
		self.menu_location	= 1

	def setup(self):
		self.menu_location = 1

	def events(self, keystate):
		pass

	def update(self):
		pass

	def draw(self):
		control.draw_text("CHARACTER SETUP", 32, constants.BLACK, setup.SCREEN, "center", 250, 40)
		control.draw_text("LEVEL 1", 24, constants.BLACK, setup.SCREEN, "center", 70, 75)
		
		# DRAWS SKILL POINTS
		control.draw_text("SKILL",  24, constants.BLACK, setup.SCREEN, "center", 70, 125)
		control.draw_text("POINTS",  24, constants.BLACK, setup.SCREEN, "center", 70, 145)
		control.draw_text("3",  32, constants.BLACK, setup.SCREEN, "center", 125, 130)

		# DRAWS STRENGTH 
		control.draw_text("STR", 22, constants.BLACK, setup.SCREEN, "center", 185, 100)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [160, 115, 50, 50], 5)

		# DRAWS INTELLIGENCE
		control.draw_text("INT", 22, constants.BLACK, setup.SCREEN, "center", 270, 100)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [245, 115, 50, 50], 5)

		# DRAW AGILITY
		control.draw_text("AGI", 22, constants.BLACK, setup.SCREEN, "center", 355, 100)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [330, 115, 50, 50], 5)


		# DRAW CONSTITUTION
		control.draw_text("CON", 22, constants.BLACK, setup.SCREEN, "center", 440, 100)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [415, 115, 50, 50], 5)


		# DRAW INVENTORY SLOTS
		control.draw_text("Weapon", 26, constants.BLACK, setup.SCREEN, "center", 100, 205)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [62.5, 222.5, 75, 75], 5)

		control.draw_text("Armour", 26, constants.BLACK, setup.SCREEN, "center", 250, 205)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [212.5, 222.5, 75, 75], 5)

		control.draw_text("Token", 26, constants.BLACK, setup.SCREEN, "center", 400, 205)
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [362.5, 222.5, 75, 75], 5)


		pygame.draw.rect(setup.SCREEN, constants.BLACK, [0, 175, 500, 10])
		pygame.draw.rect(setup.SCREEN, constants.BLACK, [0, 350, 500, 10])