import pygame
from MVC.controller import Controller


def gameloop():
    pygame.init()
    print('game has started!')
    pygame.display.set_caption('Advanced Pong')

    clock = pygame.time.Clock()

    controller = Controller()

    running = True
    while running:
        clock.tick(60)

        if (controller.model.match == False):
            controller.model.initMatch()

        controller.listenForInput()

        controller.model.view.update_screen(controller.model.GameObjects)


if __name__ == "__main__":
    gameloop()
