

### SETUP ###

# IMPORT LIBRARIES 
import pygame

# IMPORT GAME FILES
from . import constants


# INITIALIZATION
pygame.init()
pygame.display.set_caption(constants.CAPTION)
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE)


print("setup.py RUN")