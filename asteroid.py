import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_BROKEN_SPEED_SCALING
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, width=LINE_WIDTH
        )

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        e = random.uniform(20, 50)
        v1 = self.velocity.rotate(e)
        v2 = self.velocity.rotate(-e)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1 * ASTEROID_BROKEN_SPEED_SCALING
        a2.velocity = v2 * ASTEROID_BROKEN_SPEED_SCALING
