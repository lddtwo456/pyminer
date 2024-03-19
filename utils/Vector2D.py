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
      raise ValueError("Cannot normalize zero vector")

  # COOL DUNDER FUNCTIONS

  # lets you do v[0] for x or v[1] for y
  def __getitem__(self, i):
    if (i == 0):
      return self.x
    elif (i == 1):
      return self.y
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