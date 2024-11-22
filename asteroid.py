from circleshape import *
from constants import *
import pygame
import random as r

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        random_angle = r.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        medium_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        medium_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        medium_asteroid1.velocity = new_velocity1 * 1.2
        medium_asteroid2.velocity = new_velocity2 * 1.2


    
        
         

        

