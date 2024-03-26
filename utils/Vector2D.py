import numpy as np

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def magnitude(self):
    return np.sqrt(self[0]**2 + self[1]**2)
  
  def normalize(self):
    m = self.magnitude()
    if m != 0:
      return Vector2D(self[0]/m, self[1]/m)
    else:
      return Vector2D(0, 0)
  
  def normalVector(self):
    return Vector2D(self[1], self[0])
    
  def getTo(self, other):
    return other-self
    
  def lerpTo(self, other, t):
    self.x = self.x + (other.x-self.x) * t
    self.y = self.y + (other.y-self.y) * t

  def snapTo(self, other):
    # if close enough, set equal to
    if (np.abs(self.x - other.x) < 0.01):
      self.x = other.x
    if (np.abs(self.y - other.y) < 0.01):
      self.y = other.y

  # COOL DUNDER FUNCTIONS

  # lets you do v[0] for x or v[1] for y
  def __getitem__(self, i):
    if (i == 0):
      return self.x
    elif (i == 1):
      return self.y
    else:
      raise IndexError("Index out of range")
  
  def __setitem__(self, val, i):
    if (i == 0):
      self.x = val
    if (i == 1):
      self.y = val
    else:
      raise IndexError("Index out of range")
    
  # stringify
  def __str__(self):
    return f"{self[0]} {self[1]}"
    
  def __add__(self, other):
    return Vector2D(self[0]+other[0], self[1]+other[1])
  
  def __sub__(self, other):
    return Vector2D(self[0]-other[0], self[1]-other[1])
  
  def __mul__(self, other):
    if isinstance(other, (int, float)):
      # scalar
      return Vector2D(self[0]*other, self[1]*other)
    elif isinstance(other, Vector2D):
      # piecewise
      return Vector2D(self[0]*other[0], self[1]*other[1])
    else:
      raise TypeError("Unsupported operation")
    
  def __div__(self, other):
    if isinstance(other, (int, float)):
      # scalar
      return Vector2D(self[0]/other, self[1]/other)
    elif isinstance(other, Vector2D):
      # piecewise
      return Vector2D(self[0]/other[0], self[1]/other[1])
    else:
      raise TypeError("Unsupported operation")
  
  # dot product
  def __pow__(self, other):
    return self[0]*other[0] + self[1]*other[1]