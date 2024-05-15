import numpy as np
from numbers import Number

# essentially just wrapper class for np.ndarray
class Vector2D:
  def __init__(self, x, y=None):
    if (isinstance(x, Number)):
      self.array = np.array([x, y])
    elif (isinstance(x, np.ndarray)):
      self.array = x
    else:
      raise TypeError("invalid type for vector2d array")

  def magnitude(self):
    return np.linalg.norm(self.array)
  
  def normalize(self):
    m = self.magnitude()
    if m != 0:
      return Vector2D(self.array/m)
    else:
      return Vector2D(0, 0)
  
  def normalVector(self):
    return Vector2D(self[1], self[0])
    
  def getTo(self, other):
    return other-self
    
  def lerpTo(self, other, t):
    self.array = (1 - t) * self.array + t * other.array
  
  def snapTo(self, other):
    # if close enough, set equal to
    if (self.getTo(other).magnitude() < 0.01):
      self.array = other.array

  # COOL DUNDER FUNCTIONS

  # lets you do v[0] for x or v[1] for y
  def __getitem__(self, i):
    if (i == 0):
      return self.array[0]
    elif (i == 1):
      return self.array[1]
    else:
      raise IndexError("Index out of range")
  
  def __setitem__(self, val, i):
    if (i == 0):
      self.array[0] = val
    if (i == 1):
      self.array[1] = val
    else:
      raise IndexError("Index out of range")
    
  # stringify
  def __str__(self):
    return f"{self[0]} {self[1]}"
    
  def __add__(self, other):
    return Vector2D(self.array + other.array)
  
  def __sub__(self, other):
    return Vector2D(self.array - other.array)
  
  def __mul__(self, other):
    if isinstance(other, Number):
      # scalar
      return Vector2D(self.array * other)
    elif isinstance(other, Vector2D):
      # piecewise
      return Vector2D(self.array * other.array)
    else:
      raise TypeError("Unsupported operation")
    
  def __div__(self, other):
    if isinstance(other, (int, float)):
      # scalar
      return Vector2D(self.array / other)
    elif isinstance(other, Vector2D):
      # piecewise
      return Vector2D(self.array / other.array)
    else:
      raise TypeError("Unsupported operation")
  
  # dot product
  def __pow__(self, other):
    return np.dot(self.array, other.array)