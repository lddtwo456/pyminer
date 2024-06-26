import pygame
import numpy as np
from utils.Inputs import Inputs
from utils.Vector2D import Vector2D

class Player:
  def __init__(self):
    self.category = "special"
    self.type = "player"
    
    # pos vector allows for subpixel movements
    self.pos = Vector2D(0, 0)
    self.velocity = Vector2D(0, 0)

    # separate outside and movement velocy so there can be a max movement speed and you can be blown back by stuff
    self.mvmt_velocity = Vector2D(0, 0)
    self.mvmt_vector = Vector2D(0, 0)

    # max speed (magnitude of acceleration vector)
    self.mvmt_speed = 1.5
    # lerp to target movement velocity speed
    self.mvmt_lerp = .25
    # percent of velocity vector that lo
    self.friction = .05

    # fun
    self.dashed = 0

    # for drawing
    self.img = None
    self.camera = None
    self.color = (0,255,0)
    self.dimensions = (16, 24)
    self.rect = pygame.Rect(self.pos[0]-(self.dimensions[0]/2), self.pos[1]-self.dimensions[1], self.dimensions[0], self.dimensions[1])
    self.center = Vector2D(-1*(self.dimensions[0]/2), -1*(self.dimensions[1]/2))

  def update(self):
    self.move()
    
    self.pos += self.mvmt_velocity + self.velocity
    self.rect.left = np.round(self.pos[0]-(self.dimensions[0]/2))
    self.rect.top = np.round(self.pos[1]-self.dimensions[1])

    if (self.velocity != Vector2D(0, 0)):
      self.velocity.lerpTo(Vector2D(0, 0), .2)

  def move(self):
    self.mvmt_vector = Inputs.getMvmtVector()

    if (Inputs.getDash()):
      self.dash()

    if (self.mvmt_velocity != self.mvmt_vector*self.mvmt_speed):
      self.mvmt_velocity.lerpTo(self.mvmt_vector*self.mvmt_speed, self.mvmt_lerp)
      self.mvmt_velocity.snapTo(self.mvmt_vector*self.mvmt_speed)

  def getPlayerOnScreenVector(self, center=False):
    if not center: return Vector2D(self.rect.left-self.camera.pos[0], self.rect.top-self.camera.pos[1])
    return Vector2D(self.rect.left-self.camera.pos[0], self.rect.top-self.camera.pos[1]) - self.center
  
  def getMouseVector(self):
    return Vector2D(Inputs.getMX(), Inputs.getMY())
  
  def getPointingVector(self):
    mouse_vector = Vector2D(Inputs.getMX(), Inputs.getMY())
    return (mouse_vector-self.getPlayerOnScreenVector(True)).normalize()
  
  def drawVectors(self, WIN):
    onwin = self.getPlayerOnScreenVector(True)
    mouse = self.getMouseVector()
    point = self.getPointingVector()*15+onwin

    pygame.draw.circle(WIN, (255,255,255), (onwin[0], onwin[1]), 4)
    pygame.draw.circle(WIN, (0,255,0), (mouse[0], mouse[1]), 4)
    pygame.draw.circle(WIN, (255,0,0), (point[0], point[1]), 2)

  def dash(self):
    self.velocity = self.getPointingVector()*15

  # gets with dunder
  def __getitem__(self, i):
    match i:
      case 0:
        return self.rect.left
      case 1:
        return self.rect.top
      case 2:
        return self.rect.width
      case 3:
        return self.rect.height
