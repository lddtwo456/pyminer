import pygame
import numpy as np
from utils.Inputs import Inputs
from utils.Vector2D import Vector2D

class Player:
  def __init__(self):
    # pos vector allows for subpixel movements
    self.pos = Vector2D(0, 0)
    self.velocity = Vector2D(0, 0)

    # screen position and collisions, center used for camera centering
    self.rect = pygame.Rect(self.pos[0], self.pos[1], 8, 12)
    self.center = Vector2D(self.rect.width/2, self.rect.height/2)

    # separate outside and movement velocy so there can be a max movement speed and you can be blown back by stuff
    self.mvmt_velocity = Vector2D(0, 0)
    self.mvmt_vector = Vector2D(0, 0)

    # max speed (magnitude of acceleration vector)
    self.mvmt_speed = 1
    # lerp to target movement velocity speed
    self.mvmt_lerp = .25
    # percent of velocity vector that lo
    self.friction = .1

    # fun
    self.dashed = 0

  def update(self):
    self.move()
    
    self.pos += self.mvmt_velocity + self.velocity
    self.rect.left = np.round(self.pos[0])
    self.rect.top = np.round(self.pos[1])

    if (self.velocity != Vector2D(0, 0)):
      self.velocity.lerpTo(Vector2D(0, 0), .2)

  def move(self):
    self.mvmt_vector = Inputs.getMvmtVector()

    if (Inputs.getDash()):
      self.dash()

    if (self.mvmt_velocity != self.mvmt_vector*self.mvmt_speed):
      self.mvmt_velocity.lerpTo(self.mvmt_vector*self.mvmt_speed, self.mvmt_lerp)
      self.mvmt_velocity.snapTo(self.mvmt_vector*self.mvmt_speed)
  
  def dash(self):
    self.velocity = self.mvmt_vector*10

  def draw(self, camera, WIN):
    pygame.draw.rect(WIN, (255,0,0), pygame.Rect(self.rect.left-camera.pos[0], self.rect.top-camera.pos[1], self.rect.width, self.rect.height))

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
