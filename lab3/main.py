import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill("#D9D9D9")

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 2)

# eye 1
line(screen, (0, 0, 0), (50, 100), (180, 160), 15)
circle(screen, (255, 0, 0), (130, 170), 30)
circle(screen, (0, 0, 0), (130, 170), 30, 2)
circle(screen, (0, 0, 0), (130, 170), 10)

# eye 2
line(screen, (0, 0, 0), (350, 100), (220, 160), 15)
circle(screen, (255, 0, 0), (260, 170), 22)
circle(screen, (0, 0, 0), (260, 170), 22, 2)
circle(screen, (0, 0, 0), (260, 170), 10)

line(screen, (0, 0, 0), (130, 280), (260, 280), 30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
