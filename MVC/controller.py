import pygame
from model import Model
#from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.keys = set()

    def listenForInput(self):
        if (len(self.keys) > 0):
            self.execInput()

    def execInput(self):
        for key in self.keys:
            if pygame.K_UP in self.keys:
                self.model.GameObjects.player1.moveUp()

            if pygame.K_DOWN in self.keys:
                self.model.GameObjects.player1.moveDown()
            
            if pygame.K_w in self.keys:
                self.model.GameObjects.player2.moveUp()
            
            if pygame.K_s in self.keys:
                self.model.GameObjects.player2.moveDown()
