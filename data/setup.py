

### SETUP ###

# IMPORT LIBRARIES 
import os
import pygame

# IMPORT GAME FILES
from . import constants


# INITIALIZATION
pygame.init()
pygame.display.set_caption(constants.CAPTION)
SCREEN = pygame.display.set_mode(constants.SCREEN_SIZE)

graphics_dir = os.path.join("resources","graphics")
arrow = pygame.image.load(os.path.join(graphics_dir, "menu_arrow.png"))
arrow_rect = arrow.get_rect()



print("setup.py RUN")