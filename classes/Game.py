import pygame

from classes.Vector2D import Vector2D
pygame.init()
pygame.font.init()
pygame.mixer.init()


class Game:
    FPS = 60
    running = False
    frame = None
    clock = None
    mouse_position = Vector2D(0, 0)
    scale = None

    def __init__(self, size=[400, 300], fullscreen=False) -> None:
        self.size = size
        self.__fullscreen = fullscreen

    @property
    def fullscreen(self) -> bool:
        return self.__fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        self.__fullscreen = value

    def init_game(self):
        if self.fullscreen:
            resolution = list(filter(
                lambda x: x[0]/x[1] == self.size[0]/self.size[1], pygame.display.list_modes()))
            self.screen = pygame.display.set_mode(
                resolution[0], pygame.FULLSCREEN | pygame.SCALED)
            self.scale = [resolution[0][0] /
                          self.size[0], resolution[0][1]/self.size[1]]
        else:
            self.screen = pygame.display.set_mode(
                (self.size[0], self.size[1]))
        self.clock = pygame.time.Clock()
        self.game_loop_initiate()

    def left_click(self):
        pass

    def key_down(self, event):
        pass

    def key_up(self, event):
        pass

    def run(self):
        self.running = True
        running = True
        while running:
            self.mouse_position.x, self.mouse_position.y = pygame.mouse.get_pos()
            self.mouse_position.x = self.mouse_position.x / self.scale[0]
            self.mouse_position.y = self.mouse_position.y / self.scale[1]

            self.frame = pygame.Surface(self.size)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.left_click()
                elif event.type == pygame.KEYDOWN:
                    self.key_down(event)
                elif event.type == pygame.KEYUP:
                    self.key_up(event)

            self.game_loop()
            remove_list = []
            for particle in self.particles:
                result = particle.update()
                if result == False:
                    remove_list.append(particle)
                particle.draw(self.frame)
            for particle in remove_list:
                self.particles.remove(particle)

            if self.fullscreen:
                self.frame = pygame.transform.scale(
                    self.frame, [self.size[0] * self.scale[0], self.size[1] * self.scale[1]])
            self.screen.blit(self.frame, (0, 0))
            pygame.display.update()
            self.clock.tick(60)

        # Done! Time to quit.
        pygame.quit()

    def game_loop_initiate(self):
        pass

    def game_loop(self):
        pass
