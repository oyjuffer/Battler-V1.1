

### SETUP ###

# IMPORT LIBRARIES 
from os import path
import pygame

# IMPORT GAME FILES
from . import constants


# INITIALIZATION
pygame.init()
pygame.display.set_caption(constants.CAPTION)
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE)

# graphics_dir = path.join(path.dirname(__file__), ("resources\graphics"))
# arrow = pygame.image.load(path.join(graphics_dir, "menu_arrow"))
# arrow_rect = arrow.get_rect()


print("setup.py RUN")