import click
import pygame
from pygame.locals import *
from pygame.examples import chimp


@click.command()
def fish_tank():
    """Fish Tank"""
    pygame.examples.chimp.main()
