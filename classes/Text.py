import pygame
from .Vector2D import Vector2D


class Text():
    def __init__(self, font: pygame.font.Font, text: str, color: pygame.Color, center: Vector2D) -> None:
        self.text = font.render(text, False, color)
        self.text_rect = self.text.get_rect(center=(center.x, center.y))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.text, self.text_rect)
