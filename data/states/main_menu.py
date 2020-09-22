

### MAIN MENU STATE ###

# IMPORT LIBRARIES
import os 
from os import path
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
	
	def update(self, key):
		pass
	
	def draw(self):
		control.draw_text("BATTLER V1.1", 64, constants.BLACK, setup.SCREEN, "center", 250, 50)

		control.draw_text("START GAME", 32, constants.BLACK, setup.SCREEN, "center", 250, 200)
		control.draw_text("COMPENDIUM", 32, constants.BLACK, setup.SCREEN, "center", 250, 250)
		control.draw_text("SETTINGS", 32, constants.BLACK, setup.SCREEN, "center", 250, 300)
		control.draw_text("EXIT", 32, constants.BLACK, setup.SCREEN, "center", 250, 350)

		pygame.draw.polygon(setup.SCREEN, constants.BLACK, [[50, 50], [60, 50], [50, 55]])



	def running(self):
		pass

