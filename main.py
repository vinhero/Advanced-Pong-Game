import pygame
from MVC.model import Model
from MVC.view import View
from MVC.controller import Controller


def gameloop():
    pygame.init()
    print('game has started!')
    pygame.display.set_caption('Advanced Pong')

    clock = pygame.time.Clock()
    screen_width = 1000
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    background_colour = pygame.Color(0, 0, 0)
    screen.fill(background_colour)

    model = Model()
    view = View()
    controller = Controller()

    left = 20
    top = 20
    width = 50
    height = 100
    player1 = pygame.Rect(left, top, width, height)

    keys = set()
    running = True
    while running:
        clock.tick(60)
        screen.fill(background_colour)
        pygame.draw.rect(surface=screen, rect=player1,
                         color=pygame.Color(255, 255, 255))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    keys.add(event.key)
            elif event.type == pygame.KEYUP:
                keys.discard(event.key)

        speed = 20
        if pygame.K_UP in keys:
            print("Move UP!")
            if (player1.y - speed > 0):
                player1 = player1.move(0, -20)
            else:
                print("would be out of area!")

        if pygame.K_DOWN in keys:
            print("Move Down!")
            if (player1.y + speed + height < screen_height):
                player1 = player1.move(0, 20)
            else:
                print("would be out of area!")

        if pygame.K_s in keys:
            model.saveMatchResult()


if __name__ == "__main__":
    gameloop()
