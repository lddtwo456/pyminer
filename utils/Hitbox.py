from utils.Vector2D import Vector2D


class Hitbox:
  def __init__(self, type, args, center_pos=Vector2D(0,0)):
    self.type = type
    self.center_pos = center_pos

    if type == 'circle':
      self.r = args
    elif type == 'polygon':
      self.buildConvexPolygon(args)

  def buildConvexPolygon(self, args):
    self.vertices = []    
    
    for vector in args:
      self.vertices.append(vector)