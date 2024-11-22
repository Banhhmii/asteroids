import sys
from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import * 

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    asteroidField = AsteroidField()
    
    x = SCREEN_HEIGHT / 2
    y = SCREEN_WIDTH / 2
    player = Player(x,y)
    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over")
                sys.exit()
            for bullet in shots:
                if bullet.collision(asteroid) == True:
                    asteroid.kill()
                    bullet.kill()
                

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
