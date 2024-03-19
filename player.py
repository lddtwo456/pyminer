import pygame
import numpy as np
from utils.Vector2D import Vector2D

class player:
  def __init__(self):
    self.rect = pygame.Rect(0, 0, 20, 40)

  # gets with dunder
  def __getitem__(self, i):
    match i:
      case 0:
        return self.rect.left
      case 1:
        return self.rect.top