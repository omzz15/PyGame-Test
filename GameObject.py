import pygame
import time
import Utils


class GameObject:
    def __init__(self, grid, startVel, radius, color, screen):
        self.grid = grid.clone()
        self.grid.minPos.x += radius
        self.grid.minPos.y += radius
        self.grid.maxPos.x -= radius
        self.grid.maxPos.y -= radius

        self.velocity = Utils.Utils.cloneVector2(startVel)
        self.radius = radius
        self.color = Utils.Utils.cloneColor(color)
        self.objectManager = None
        self.lastUpdateTime = time.time()
        self.screen = screen
        self.wasBallHit = {}

    def initWithManager(self):
      for gameObject in self.objectManager.gameObjects:
        if(gameObject != self):
          self.wasBallHit[gameObject] = False

    def run(self):
        timeDif = time.time() - self.lastUpdateTime
        self.move(timeDif)
        self.draw()
        self.physics()
        self.lastUpdateTime = time.time()

    def move(self, timeDif):
        self.grid.position.x += timeDif * self.velocity.x
        self.grid.position.y += timeDif * self.velocity.y

        for i in range(2):
            if (self.grid.position[i] > self.grid.maxPos[i]):
                self.grid.position[i] = self.grid.maxPos[i] - (
                    self.grid.position[i] - self.grid.maxPos[i])
                self.velocity[i] *= -1

            if (self.grid.position[i] < self.grid.minPos[i]):
                self.grid.position[i] = self.grid.minPos[i] + (
                    self.grid.minPos[i] - self.grid.position[i])
                self.velocity[i] *= -1 

    def physics(self):
        if self.objectManager != None:
            for obj in self.objectManager.gameObjects:
                if obj != self:
                    if self.grid.position.distance_to(obj.grid.position) <= self.radius + obj.radius:
                      if(not self.wasBallHit[obj]):
                        self.onCollisionEnter(obj)
                        self.wasBallHit[obj] = True
                      else:
                        self.onCollisionStay(obj)
                    elif(self.wasBallHit[obj]):
                      self.onCollisionExit(obj)
                      self.wasBallHit[obj] = False

                        

    def onCollisionEnter(self, other):
      self.flipVel()
      other.flipVel()
    
    def onCollisionStay(self, other):
      return
    
    def onCollisionExit(self, other):
      return

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.grid.position, self.radius)

    def flipVel(self):
        self.velocity.x *= -1
        self.velocity.y *= -1