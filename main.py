import numpy
import pygame
import sys
import GameObject
import GameObjectManager
import Grid
import Utils

#user variables
size = pygame.Vector2(852, 480)
maxSpeed = pygame.Vector2(100, 100)
circleColor = pygame.Color(0, 0, 255)
backgroundColor = pygame.Color(0, 0, 0)

#other variables
minPosVal = pygame.Vector2(0,0)
maxPosVal = size
minVelVal = pygame.Vector2(-maxSpeed.x, -maxSpeed.y)
maxVelVal = maxSpeed

#main code
print("system check:")
print(f"{numpy} : numpy ok")
print(f"{pygame} : pygame ok")
print(f"{sys} : system ok")

print("initializing pygame...")
pygame.init
screen = pygame.display.set_mode([int(size.x), int(size.y)])
print("pygame initialized")

print("creating gameObjects...")

GOM = GameObjectManager.test()

for i in range(10):
    grid = Grid.Grid(minPosVal, maxPosVal, Utils.Utils.makeRandVector2(minPosVal, maxPosVal))
    speed = Utils.Utils.makeRandVector2(minVelVal, maxVelVal)
    GOM.addObject(GameObject.GameObject(grid, speed, 10, circleColor, screen))
    GOM.initAll()
print("objects created")

print("starting animation...")
while 1:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.exit()
          sys.exit()
    screen.fill((0, 0, 0))
    GOM.runAll()
    pygame.display.update()
    #print(f"X : {gameObject.grid.position.x}, Y : {gameObject.grid.position.y}")