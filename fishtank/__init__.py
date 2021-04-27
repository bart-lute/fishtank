import sys

import click
import pygame
from pygame.locals import *
import random
import os

WIDTH = 500
HEIGHT = 500
FPS = 120

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# assets
app_folder = os.path.dirname(__file__)
img_folder = os.path.join(app_folder, "img")


class Fish(pygame.sprite.Sprite):
    # Sprite for the fish
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'fish.png')).convert()
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 1
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Init game and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Tank")
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
fish = Fish()
sprites.add(fish)


@click.command()
def fish_tank():
    """Fish Tank"""
    while True:

        # Keep loop running at correct speed
        clock.tick(FPS)

        # Process events
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update
        sprites.update()

        # Draw
        screen.fill(BLACK)
        sprites.draw(screen)

        # after drawing, flip
        pygame.display.flip()
        # pygame.display.update()


