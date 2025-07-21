import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color(0,0,0))
        clock.tick(60)
        dt = clock.get_time()
        pygame.display.flip()

if __name__ == "__main__":
    main()
