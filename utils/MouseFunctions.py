import pygame
import numpy as np

class MouseFunctions:
  def __init__(self, blit_offset, scale):
    self.blit_offset = blit_offset
    self.scale = scale

  # scaled mouse positions
  def getMX(self):
    return np.round((pygame.mouse.get_pos()[0] - self.blit_offset) / self.scale - .5)
  def getMY(self):
    return np.round(pygame.mouse.get_pos()[1] / self.scale - .5)
  def getM(self):
    return (self.getMX(), self.getMY())