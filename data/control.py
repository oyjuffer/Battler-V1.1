

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

		self.state		= None


	def setup_states(self, state_dict, start_state):
		self.state_dict 	= state_dict
		self.start_state 	= start_state
		self.state = self.state_dict[self.start_state]

	def eventloop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

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
	edge.fill(constants.WHITE)
	setup.SCREEN.blit(edge, (10, 10))

print("control.py RUN")