from Globals import Globals
from utils.Vector2D import Vector2D

class Camera():
  def __init__(self, target):
    self.pos = Vector2D(0, 0)
    self.target = target
    self.lerp_speed = 0.1

    self.screen_center = Vector2D(Globals.UNSCALED_WIN_DIMENSIONS[0]/2, Globals.UNSCALED_WIN_DIMENSIONS[1]/2)
    self.target_pos = self.target.pos + self.target.center - self.screen_center

  def setTarget(self, target):
    self.target = target    
    self.target_pos = target.pos + target.center - self.screen_center
  
  def setSpeed(self, speed):
    self.lerp_speed = speed

  def update(self):
    self.target_pos = self.target.pos + self.target.center - self.screen_center

    if (self.pos != self.target_pos):
      self.pos.lerpTo(self.target_pos, self.lerp_speed)
      self.pos.snapTo(self.target_pos)