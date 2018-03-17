
import sys, os, pygame
from pygame.locals import *


SCREEN_DIMENSIONS = screenX, screenY = (720, 480)
BG_COLOR = (0,0,0)


pygame.init()
pygame.display.set_caption(" Name of the Game ")
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
		clock.tick(60)




if __name__ == '__main__':
	main()