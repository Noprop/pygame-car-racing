import pygame
import time
import math

GRASS = pygame.image.load('assets/grass.jpg')
TRACK = pygame.image.load('assets/track.png')

TRACK_BORDER = pygame.image.load('assets/track-border.png')
FINISH = pygame.image.load('assets/finish.png')

RED_CAR = pygame.image.load('assets/red-car.png')
GREEN_CAR = pygame.image.load('assets/green-car.png')

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Game!')


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()