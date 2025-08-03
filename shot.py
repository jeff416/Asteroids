import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white") ,(int(self.position.x), int(self.position.y)) , self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt