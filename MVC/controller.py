import pygame
import sys
from MVC.model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.keys = set()

    def listenForInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    self.keys.add(event.key)
            elif event.type == pygame.KEYUP:
                self.keys.discard(event.key)

        if (len(self.keys) > 0):
            self.execInput()

    def execInput(self):
        for key in self.keys:
            if pygame.K_UP in self.keys:
                self.model.GameObjects["player1"].moveUp()

            if pygame.K_DOWN in self.keys:
                self.model.GameObjects["player1"].moveDown()

            if pygame.K_w in self.keys:
                self.model.GameObjects["player2"].moveUp()

            if pygame.K_s in self.keys:
                self.model.GameObjects["player2"].moveDown()

            if pygame.K_0 in self.keys:
                print("saving Match")
                self.model.saveMatchResult()
