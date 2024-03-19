class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # lets you do v[0] for x or v[1] for y
  def __getitem__(self, i):
    if (i == 0):
      return self.x
    elif (i == 1):
      return self.y
    else:
      raise IndexError("Index out of range")