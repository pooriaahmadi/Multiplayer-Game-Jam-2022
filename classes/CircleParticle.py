from turtle import width
from .Object import Object
from .Vector2D import Vector2D
import pygame


class CircleParticle(Object):
    def __init__(self, position: Vector2D, color: pygame.Color, radius=0, friction=0, momentum=Vector2D(0, 0)) -> None:
        super().__init__(position, radius, radius)
        self.color = color
        self.friction = friction
        self.momentum = momentum
        self.initial_momentum = Vector2D(momentum.x, momentum.y)

    def update(self):
        if self.momentum.y < 0:
            self.momentum.y += self.friction
        else:
            self.momentum.y -= self.friction
        if self.momentum.x < 0:
            self.momentum.x += self.friction
        else:
            self.momentum.x -= self.friction
        self.position = self.position + self.momentum

        self.width -= self.friction
        if self.width <= 0:
            return False

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, radius=self.width, color=self.color, center=[
                           self.position.x, self.position.y])
