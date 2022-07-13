from classes import Game, Text, Vector2D, CircleParticle
import pygame
import typing
import random

from math import pi, cos, sin


def point(h, k, r):
    theta = random.random() * 2 * pi
    return h + cos(theta) * r, k + sin(theta) * r


class NewGame(Game):
    particles: typing.List[CircleParticle] = []

    def left_click(self):
        self.particles = []
        for i in range(200):
            # momentum = point(0, -4, 5)
            momentum = [
                random.randrange(-3000, 3000) / 1000, random.randrange(-3000, 3000) / 1000]  # EXPLODE
            self.particles.append(CircleParticle(Vector2D(self.mouse_position.x, self.mouse_position.y), pygame.Color(
                0, 0, 0), random.randrange(300, 500) / 100, 0.1, Vector2D(momentum[0], momentum[1])))

    def game_loop_initiate(self):
        font = pygame.font.Font("fonts/font.ttf", 25)
        self.text = Text(font, "Test text", pygame.Color(
            0, 0, 0), Vector2D(self.size[0] / 2, self.size[1] / 2))

    def game_loop(self):
        # Background color: white
        self.frame.fill((255, 255, 255))
        self.text.draw(self.frame)


if __name__ == "__main__":
    game = NewGame([640, 360], fullscreen=True)
    game.init_game()
    game.run()
