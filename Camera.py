import pygame
import numpy as np

from utils.Vector2D import Vector2D

class Camera:
  def __init__(self, target, lerp_speed, screen_dimensions):
    self.pos = Vector2D(0, 0)
    self.target = target
    self.lerp_speed = lerp_speed

    self.screen_center = Vector2D(screen_dimensions[0]/2, screen_dimensions[1]/2)
    self.target_pos = self.target.pos + self.target.center - self.screen_center

  def setTarget(self, target):
    self.target = target    
    self.target_pos = target.pos + target.center - self.screen_center
  
  def setSpeed(self, speed):
    self.lerp_speed = speed

  def update(self):
    self.target_pos = self.target.pos - self.target.center - self.screen_center

    if (self.pos != self.target_pos):
      self.pos.lerpTo(self.target_pos, self.lerp_speed)
      self.pos.snapTo(self.target_pos)