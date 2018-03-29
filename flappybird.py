
import sys, os
import math
import random
from itertools import cycle

import pygame
from pygame.locals import *



SCREEN_DIMENSIONS = screenX, screenY = (288, 512)
BG_COLOR = (0, 0, 0)
FPS = 60
PIPE_GAP = 100

# list of all possible players (tuple of 3 positions of flap)
PLAYERS_LIST = (
    # red bird
    (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png',
    ),
    # blue bird
    (
        # amount by which base can maximum shift to left
        'assets/sprites/bluebird-upflap.png',
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-downflap.png',
    ),
    # yellow bird
    (
        'assets/sprites/yellowbird-upflap.png',
        'assets/sprites/yellowbird-midflap.png',
        'assets/sprites/yellowbird-downflap.png',
    ),
)

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
    'assets/sprites/background-night.png',
)

# list of pipes
PIPES_LIST = (
    'assets/sprites/pipe-green.png',
    'assets/sprites/pipe-red.png',
)





pygame.init()
pygame.display.set_caption(" FLAPPY BIRD ")
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
clock = pygame.time.Clock()







def main():

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keyPressed = pygame.key.get_pressed()

		if keyPressed[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

		# if keyPressed[pygame.K_SPACE]:
			


		screen.fill(BG_COLOR)
		pygame.display.update()
		clock.tick(FPS)




if __name__ == '__main__':
	main()