

### MAIN ###

# IMPORT LIBRARIES
import os 
import pygame

# IMPORT GAME FILES
from . import constants
from . import control
from . import setup
from .states import main_menu

# CLASSES

# FUNCTIONs 
def main():
	"""
	This is the main function for the game; it sets up a game object and state dictionaries.
	It then sets up the initital active state and runs the mainloop. 
	This can be found in control.py. 
	"""
	game = control.Control()
	state_dict = {constants.MAIN_MENU: main_menu.Main_Menu()}
	
	game.setup_states(state_dict, constants.MAIN_MENU)
	game.mainloop()
