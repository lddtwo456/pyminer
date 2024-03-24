import pygame
import numpy as np

class EntityPainter:
  def drawEntities(camera, WIN, entities):
    sorted_entities = sorted(entities, key=lambda sprite: sprite.pos[1])

    for entity in sorted_entities:
      entity.camera = camera

      if (camera.pos+camera.screen_center).getTo(entity.pos+entity.center).magnitude() > (np.sqrt((WIN.get_width()/2)**2 + (WIN.get_height()/2)**2)):
        pass
      else:
        if entity.img != None:
          print("draw entity img")
        else:
          pygame.draw.rect(WIN, entity.color, pygame.Rect(entity.rect.left-camera.pos[0], entity.rect.top-camera.pos[1], entity.rect.width, entity.rect.height))
