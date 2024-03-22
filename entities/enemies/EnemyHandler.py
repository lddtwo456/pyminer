from entities.enemies.Follower import Follower
from utils.Vector2D import Vector2D

class EnemyHandler:
  def getEnemy(type, args):
    if type == "follower":
      return Follower(args)