import pygame
import numpy as np
import sys

from Player import Player
from utils.Vector2D import Vector2D



# SETUP STUFF



pygame.init()

fullscreen = True
unscaled = (320,240)

# make scaled screen
if fullscreen:
  WIN = pygame.display.set_mode((0, 0))

  blit_offset = np.round((WIN.get_width() - (np.round(WIN.get_height() * (unscaled[0]/unscaled[1])))) / 2)
  scale = WIN.get_height()/unscaled[1]
  screen = pygame.Surface(unscaled)
else:
  scale = 2
  WIN = pygame.display.set_mode((unscaled[0]*scale, unscaled[1]*scale))

  blit_offset = 0
  screen = pygame.Surface(unscaled)

# hide mouse
pygame.mouse.set_visible(False)

# player init
player = Player()



# FUNCITONS



# scaled mouse positions
def getMX():
  return np.round((pygame.mouse.get_pos()[0] - blit_offset) / scale - .5)
def getMY():
  return np.round(pygame.mouse.get_pos()[1] / scale - .5)
def getM():
  return (getMX(), getMY())



# GAME LOOP



clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    # closing window
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  player.move(pygame.key.get_pressed())
  player.update()
  print(player.mvmt_velocity)

  # FRAME DRAWING

  screen.fill((0,0,0))
  WIN.fill((0,0,0))

  pygame.draw.circle(screen, (255,255,255), (screen.get_width()/2, screen.get_height()/2), 100)
  screen.blit(pygame.image.load("./assets/ui/cursor.png"), (getMX(),getMY()))
  pygame.draw.rect(screen, (255,0,0), player)

  scaled_screen = pygame.transform.scale(screen, (scale*screen.get_width(), scale*screen.get_height()))
  WIN.blit(scaled_screen, (blit_offset, 0))

  pygame.display.flip()

  #FPS 
  clock.tick(60)