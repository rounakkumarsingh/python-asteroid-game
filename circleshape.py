import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # type: ignore
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):

        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides(self, other: "CircleShape") -> bool:
        dist_to_other = self.position.distance_to(other.position)
        if dist_to_other <= self.radius + other.radius:
            return True
        return False
