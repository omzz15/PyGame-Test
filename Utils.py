import pygame
import random

class Utils:
    def makeRandVector2(min = pygame.Vector2(0,0), max = pygame.Vector2(1,1)):
        return pygame.Vector2(random.uniform(min.x, max.x), random.uniform(min.y, max.y))
    def cloneVector2(v2):
        return pygame.Vector2(v2.x, v2.y)
    def cloneColor(c):
        return pygame.Color(c.r, c.g, c.b)