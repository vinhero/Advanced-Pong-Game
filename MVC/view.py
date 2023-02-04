import pygame


class View:
    def __init__(self):
        self.width = 1000
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_colour = pygame.Color(0, 0, 0)
        self.screen.fill(self.background_colour)

    def update_screen(self, game_objects):
        self.screen.fill(self.background_colour)

        for game_object in game_objects:
            game_object.update()

        self.screen.flip()
