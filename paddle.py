import pygame

class Paddle:
    color = (0,0,0)
    vel = 4

    def __init__(self, x, y, width, height):
        self.x = self.org_x = x
        self.y = self.org_y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

    def reset(self):
        self.x = self.org_x
        self.y = self.org_y