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

  def C2C(c1, c2):
    if ((c2.center_pos[0]-c1.center_pos[0])^2 + (c2.center_pos[1]-c1.center_pos[1])^2 <= (c1.r+c2.r)^2):
      return True
    else:
      return False
  
  def P2P(p1, p2, continued=False):
    results = []

    for i in range(len(p1.vertices)):
      vertex = p1.vertices[i]
      if i != len(p1.vertices)-1:
        next_vertex = p1.vertices[i+1]+p1.center_pos
      else:
        next_vertex = p1.vertices[0]+p1.center_pos

      line = vertex.getTo(next_vertex)
      perp_line = line.normalVector()

      projected_t_p1 = []
      projected_t_p2 = []

      for p1vertex in p1.vertices:
        projected_t = (vertex.getTo(p1vertex)**perp_line)
        projected_t_p1.append(projected_t)
      for p2vertex in p2.vertices:
        projected_t = (vertex.getTo(p2vertex)**perp_line)
        projected_t_p2.append(projected_t)
      
      projected_t_p1 = Hitbox.getLims(projected_t_p1)
      projected_t_p2 = Hitbox.getLims(projected_t_p2)

      results.append(Hitbox.getOverlap(projected_t_p1, projected_t_p2))

    for result in results:
      if result == False:
        return False
    
    if continued == True:
      return True
    else:
      return Hitbox.P2P(p2, p1, True)
        

  def getLims(list):
    max = float('-inf')
    min = float('inf')
    for item in list:
      if item > max:
        max = item
      if item < min:
        min = item

    return [min, max]
  
  def getOverlap(l1, l2):
    return max(l1[0], l2[0]) <= min(l1[1], l2[1])