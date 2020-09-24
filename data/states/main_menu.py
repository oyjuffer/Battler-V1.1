

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
		self.running 		= False
		self.state 			= None
		self.menu_location	= 1
		


		self.state_dict 	= {1:constants.START_GAME,
		                       2:constants.COMPENDIUM,
		                       3:constants.SETTINGS,
		                       4:constants.EXIT} 

		self.state = self.state_dict[1]
		self.state_change 	= False
		self.next_state 	= None
		
	def setup(self):
		self.menu_location = 1
	
	def events(self, keystate):
		self.keystate = keystate
		if self.keystate[pygame.K_UP]:
			print("KEYSTATE: UP")
			if self.menu_location == 1:
				print("PASSING")
				pass
			else:
				self.menu_location -= 1
			print("MENU LOCATION: " + str(self.menu_location))

		if self.keystate[pygame.K_DOWN]:
			print("KEYSTATE: DOWN")
			if self.menu_location == 4:
				print("PASSING")
				pass
			else:
				self.menu_location += 1			
			print("MENU LOCATION: " + str(self.menu_location))


		if self.keystate[pygame.K_RETURN]:
			print("KEYSTATE: RETURN")
			self.state_change = True

	
	def update(self):
		if self.state_change == True:
			return self.state

	def draw(self):
		control.draw_text("BATTLER V1.1", 64, constants.BLACK, setup.SCREEN, "center", 250, 50)

		control.draw_text("START GAME", 32, constants.BLACK, setup.SCREEN, "center", 250, 200)
		control.draw_text("COMPENDIUM", 32, constants.BLACK, setup.SCREEN, "center", 250, 250)
		control.draw_text("SETTINGS", 32, constants.BLACK, setup.SCREEN, "center", 250, 300)
		control.draw_text("EXIT", 32, constants.BLACK, setup.SCREEN, "center", 250, 350)

		self.draw_menu_location()

	def draw_menu_location(self):
		if self.menu_location == 1:
			pygame.draw.rect(setup.SCREEN, constants.BLACK, (125, 195, 10, 10))
			self.state = self.state_dict[1]
			
		if self.menu_location == 2:
			pygame.draw.rect(setup.SCREEN, constants.BLACK, (125, 245, 10, 10))
			self.state = self.state_dict[2]
			
		if self.menu_location == 3:
			pygame.draw.rect(setup.SCREEN, constants.BLACK, (150, 295, 10, 10))
			self.state = self.state_dict[3]
			
		if self.menu_location == 4:
			pygame.draw.rect(setup.SCREEN, constants.BLACK, (150, 345, 10, 10))
			self.state = self.state_dict[4]
			