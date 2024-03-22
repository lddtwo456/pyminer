import pygame

class SpritePainter:
  sprites = []

  def addSprite(sprite):
    SpritePainter.sprites.append(sprite)

  def drawSprites(camera, WIN):
    for sprite in SpritePainter.sprites:
      sprite.camera = camera

      if sprite.img != None:
        print("draw sprite img")
      else:
        pygame.draw.rect(WIN, sprite.color, pygame.Rect(sprite.rect.left-camera.pos[0], sprite.rect.top-camera.pos[1], sprite.rect.width, sprite.rect.height))
