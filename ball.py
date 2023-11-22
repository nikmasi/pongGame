import ball
import pygame

class Ball:
    speed_ball = 5
    color = (0, 0, 0)
    min_speed=3
    max_speed=20

    def __init__(self, x, y, radius):
        self.x = self.org_x = x
        self.y = self.org_y = y
        self.radius = radius
        self.x_vel = self.speed_ball
        self.y_vel = 0

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        if(self.x_vel>0 and self.speed_ball!=self.x_vel):
            self.x_vel=self.speed_ball
        elif(self.x_vel < 0 and self.speed_ball != -self.x_vel):
            self.x_vel=-self.speed_ball
        print(str(self.x) + " " + str(self.x_vel))
        self.x += self.x_vel
        print(str(self.x) + " " + str(self.x_vel))
        self.y += self.y_vel

    def reset(self):
        self.x = self.org_x
        self.y = self.org_y
        self.y_vel = 0
        self.x_vel *= -1

    def speed_increment(self):
        if (self.speed_ball < self.max_speed):
            self.speed_ball=self.speed_ball+1

    def speed_decrement(self):
        if(self.speed_ball>self.min_speed):
            self.speed_ball=self.speed_ball-1

    def get_speed(self):
        return self.speed_ball