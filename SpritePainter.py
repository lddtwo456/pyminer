import pygame
import numpy as np

class SpritePainter:
  sprites = []

  def addSprite(sprite):
    SpritePainter.sprites.append(sprite)

  def drawSprites(camera, WIN):
    sorted_sprites = sorted(SpritePainter.sprites, key=lambda sprite: sprite.pos.y)

    for sprite in sorted_sprites:
      sprite.camera = camera

      if ((sprite.pos+sprite.center)-(camera.pos+camera.screen_center)).magnitude() > (np.sqrt((WIN.get_width()/2)**2 + (WIN.get_height()/2)**2)):
        pass
      else:
        if sprite.img != None:
          print("draw sprite img")
        else:
          pygame.draw.rect(WIN, sprite.color, pygame.Rect(sprite.rect.left-camera.pos[0], sprite.rect.top-camera.pos[1], sprite.rect.width, sprite.rect.height))
