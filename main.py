import pygame
import numpy as np
import sys

from Camera import Camera
from Globals import Globals
from Player import Player
from utils.MouseFunctions import MouseFunctions
from utils.Vector2D import Vector2D



# SETUP STUFF



pygame.init()

# hide mouse
pygame.mouse.set_visible(False)

# init global classes
Globals.PLAYER = Player()
Globals.MOUSE = MouseFunctions()
Globals.CAMERA = Camera(Globals.PLAYER)



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

  Globals.PLAYER.update()

  # FRAME DRAWING
  Globals.CAMERA.update()

  Globals.SCREEN.fill((0,0,0))
  Globals.WIN.fill((0,0,0))

  pygame.draw.circle(Globals.SCREEN, (255,255,255), (40-Globals.CAMERA.pos[0], 40-Globals.CAMERA.pos[1]), 50)
  pygame.draw.circle(Globals.SCREEN, (255,255,255), (120-Globals.CAMERA.pos[0], 160-Globals.CAMERA.pos[1]), 75)
  pygame.draw.circle(Globals.SCREEN, (255,255,255), (20-Globals.CAMERA.pos[0], 120-Globals.CAMERA.pos[1]), 30)
  pygame.draw.circle(Globals.SCREEN, (255,255,255), (230-Globals.CAMERA.pos[0], -20-Globals.CAMERA.pos[1]), 90)
  Globals.SCREEN.blit(pygame.image.load("./assets/ui/cursor.png"), Globals.MOUSE.getM())
  Globals.PLAYER.draw()

  scaled_screen = pygame.transform.scale(Globals.SCREEN, (Globals.SCALE*Globals.SCREEN.get_width(), Globals.SCALE*Globals.SCREEN.get_height()))
  Globals.WIN.blit(scaled_screen, (Globals.BLIT_OFFSET, 0))

  pygame.display.flip()

  #FPS 
  clock.tick(60)