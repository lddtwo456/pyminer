import pygame
import numpy as np

from entities.EntityPointers import EntityPointers
from utils.Vector2D import Vector2D

import random

class Follower:
  def __init__(self, args):
    self.category = "enemy"
    self.type = "follower"

    # pos vector allows for subpixel movements
    self.pos = Vector2D(0, 0)
    self.velocity = Vector2D(0, 0)

    # screen position and collisions, center used for camera centering
    self.dimensions = (8, 8)
    self.rect = pygame.Rect(self.pos[0]-(self.dimensions[0]/2), self.pos[1]-self.dimensions[1], self.dimensions[0], self.dimensions[1])
    self.center = Vector2D(0, -1*(self.dimensions[1]/2))

    # separate outside and movement velocy so there can be a max movement speed and you can be blown back by stuff
    self.mvmt_velocity = Vector2D(0, 0)
    self.mvmt_vector = Vector2D(0, 0)

    # max speed (magnitude of acceleration vector)
    self.mvmt_speed = .4
    # lerp to target movement velocity speed
    self.mvmt_lerp = .25
    # percent of velocity vector that lo
    self.friction = .2

    # drawing
    self.camera = None
    self.color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
    self.img = None

    if args != None:
      self.pos = args.get("pos")
  
  def update(self):
    self.move()

    self.pos += self.mvmt_velocity + self.velocity
    self.rect.left = np.round(self.pos[0])
    self.rect.top = np.round(self.pos[1])

    if (self.velocity != Vector2D(0, 0)):
      self.velocity.lerpTo(Vector2D(0, 0), self.friction)

  def move(self):
    self.mvmt_vector = (EntityPointers.PLAYER.pos-self.pos).normalize()

    if (self.mvmt_velocity != self.mvmt_vector*self.mvmt_speed):
      self.mvmt_velocity.lerpTo(self.mvmt_vector*self.mvmt_speed, self.mvmt_lerp)
      self.mvmt_velocity.snapTo(self.mvmt_vector*self.mvmt_speed)