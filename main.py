import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
 
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectile = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (projectile, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x, y)



    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color("black"))
        dt = clock.tick(60) / 1000.0
        for obj in drawable:
            obj.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            if player.collision(obj):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    main()
