import pygame
import numpy as np

class Globals:
  FULLSCREEN = True
  UNSCALED_WIN_DIMENSIONS = (320, 240)

  if FULLSCREEN:
    WIN = pygame.display.set_mode((0, 0))

    BLIT_OFFSET = np.round((WIN.get_width() - (np.round(WIN.get_height() * (UNSCALED_WIN_DIMENSIONS[0]/UNSCALED_WIN_DIMENSIONS[1])))) / 2)
    SCALE = WIN.get_height()/UNSCALED_WIN_DIMENSIONS[1]
    SCREEN = pygame.Surface(UNSCALED_WIN_DIMENSIONS)
  else:
    SCALE = 2
    WIN = pygame.display.set_mode((UNSCALED_WIN_DIMENSIONS[0]*SCALE, UNSCALED_WIN_DIMENSIONS[1]*SCALE))

    BLIT_OFFSET = 0
    SCREEN = pygame.Surface(UNSCALED_WIN_DIMENSIONS)

  PLAYER = None
  MOUSE = None
  CAMERA = None