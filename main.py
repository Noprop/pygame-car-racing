import pygame
import time
import math
from utils import scale_image

GRASS = scale_image(pygame.image.load('assets/grass.jpg'), 2.5)
TRACK = scale_image(pygame.image.load('assets/track.png'), 0.9)

TRACK_BORDER = scale_image(pygame.image.load('assets/track-border.png'), 0.9)
FINISH = pygame.image.load('assets/finish.png')

RED_CAR = scale_image(pygame.image.load('assets/red-car.png'), 0.55)
GREEN_CAR = scale_image(pygame.image.load('assets/green-car.png'), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racing Game!')

FPS = 60


def draw(win, images_to_draw):
    for img, pos in images_to_draw:
        win.blit(img, pos)


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, (0, 0)), (RED_CAR, (0, 0)), (GREEN_CAR, (0, 0))]

while run:
    clock.tick(FPS)

    draw(WIN, images)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                run = False
                break
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
