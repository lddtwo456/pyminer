import pygame
import numpy as np
from utils.Vector2D import Vector2D

class Inputs:
  # keys
  keys = None

  # player things
  l = 0
  r = 0
  u = 0
  d = 0
  dashed = False

  # mouse
  blit_offset = None
  scale = None

  def mouseInit(blit_offset, scale):
    Inputs.blit_offset = blit_offset
    Inputs.scale = scale

  def update(keys):
    # update get_pressed
    Inputs.keys = keys

  def getMvmtVector():
    if Inputs.keys == None: return Vector2D(0, 0)

    if Inputs.keys[pygame.K_a]:
      Inputs.l = -1
    else:
      Inputs.l = 0
    if Inputs.keys[pygame.K_d]:
      Inputs.r = 1
    else:
      Inputs.r = 0
    if Inputs.keys[pygame.K_w]:
      Inputs.u = -1
    else:
      Inputs.u = 0
    if Inputs.keys[pygame.K_s]:
      Inputs.d = 1
    else:
      Inputs.d = 0

    return Vector2D(Inputs.l+Inputs.r, Inputs.u+Inputs.d).normalize()
  
  def getDash():
    if Inputs.keys == None: return False

    if Inputs.keys[pygame.K_SPACE]:
      if (Inputs.dashed != True):
        Inputs.dashed = True
        return True
    else:
      Inputs.dashed = False

    return False
  
  def getMX():
    if Inputs.scale == None: return 0
    return np.round((pygame.mouse.get_pos()[0] - Inputs.blit_offset) / Inputs.scale - .5)
  def getMY():
    if Inputs.scale == None: return 0
    return np.round(pygame.mouse.get_pos()[1] / Inputs.scale - .5)
  def getM():
    if Inputs.scale == None: return (0, 0)
    return (Inputs.getMX(), Inputs.getMY())