import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, width=LINE_WIDTH
        )

    def update(self, delta_time):
        forward = pygame.Vector2(0, 1)
        self.position += forward * 10 * delta_time
