import pygame
import numpy as np
import sys

pygame.init()

fullscreen = True
unscaled = (200,150)

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

# scaled mouse positions
def getMX():
  return np.round((pygame.mouse.get_pos()[0] - blit_offset) / scale - .5)
def getMY():
  return np.round(pygame.mouse.get_pos()[1] / scale - .5)
def getM():
  return (getMX(), getMY())

# game loop
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

  screen.fill((0,0,0))
  WIN.fill((0,0,0))

  pygame.draw.circle(screen, (255,255,255), (screen.get_width()/2, screen.get_height()/2), 100)
  pygame.draw.rect(screen, (255,0,0), pygame.Rect(getMX(),getMY(),1,1))
  pygame.draw.circle(screen, (255,0,0), getM(), 5, 1)

  scaled_screen = pygame.transform.scale(screen, (scale*screen.get_width(), scale*screen.get_height()))
  WIN.blit(scaled_screen, (blit_offset, 0))

  print(f"{getMX()}, {getMY()}")

  pygame.display.flip()