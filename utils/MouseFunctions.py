import pygame
import numpy as np

from Globals import Globals

class MouseFunctions:
  # scaled mouse positions
  def getMX(self):
    return np.round((pygame.mouse.get_pos()[0] - Globals.BLIT_OFFSET) / Globals.SCALE - .5)
  def getMY(self):
    return np.round(pygame.mouse.get_pos()[1] / Globals.SCALE - .5)
  def getM(self):
    return (self.getMX(), self.getMY())