from entities.EntityPointers import EntityPointers
from entities.enemies.EnemyHandler import EnemyHandler

class EntityHandler:
  entities = []

  def update():
    for entity in EntityHandler.entities:
      entity.update()

  def addEntity(category, type, args):
    if category == "enemy":
      EntityHandler.entities.append(EnemyHandler.getEnemy(type, args))

  def init(player):
    # get references to objects that entities may need
    EntityPointers.PLAYER = player