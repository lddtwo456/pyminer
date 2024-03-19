import pygame
import numpy as np

from utils.Vector2D import Vector2D

class Player:
  def __init__(self):
    self.rect = pygame.Rect(0,0,20,40)

    # I think it would be fun to treat movement as a vector :)
    self.vel = Vector2D(0, 0)