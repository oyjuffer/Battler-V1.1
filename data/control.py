

### Control ###

# IMPORT LIBRARIES
import os 
import pygame

# IMPORT GAME FILES
from . import constants
from . import control
from . import setup

# CLASSES
class Control():
	def __init__(self):
		self.running 	= True
		self.clock 		= pygame.time.Clock()
		self.fps		= 60

		self.keystate 	= pygame.key.get_pressed()

		self.state_dict = {}
		self.state_name = None
		self.state		= None


	def setup_states(self, state_dict, start_state):
		self.state_dict 	= state_dict
		self.state_name 	= start_state
		self.state = self.state_dict[self.state_name]

	def change_states(self):
		pass

	def eventloop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			if event.type == pygame.KEYDOWN:
				self.keystate = pygame.key.get_pressed()
				self.state.events(self.keystate)

	def updateloop(self):
		pass

	def drawloop(self):
		draw_backdrop()
		self.state.draw()



	def mainloop(self):
		while self.running:
			
			self.eventloop() 
			self.updateloop()
			self.drawloop()

			pygame.display.update()
			self.clock.tick(self.fps)



# FUNCTIONS
def draw_backdrop():
	setup.SCREEN.fill(constants.BLACK)
	edge = pygame.Surface((480, 480))
	edge.fill(constants.SNOW)
	setup.SCREEN.blit(edge, (10, 10))

def draw_text(text, size, colour, surface, attribute, x, y):
	font = pygame.font.Font(constants.FONT, size)
	text_surface = font.render(text, True, colour)
	text_rect = text_surface.get_rect()
	if attribute == "center":
		text_rect.center = (x, y)
	surface.blit(text_surface, text_rect)



print("control.py RUN")