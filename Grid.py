import pygame
import Utils

class Grid:
    def __init__(self, minPos, maxPos, startPos=pygame.Vector2(0, 0)):
        self.minPos = minPos
        self.maxPos = maxPos
        self.position = startPos

    def clone(self):
        return Grid(Utils.Utils.cloneVector2(self.minPos), Utils.Utils.cloneVector2(self.maxPos), Utils.Utils.cloneVector2(self.position))