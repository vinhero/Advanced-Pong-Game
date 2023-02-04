import pygame
from view import View
from ..GameObjects.Player import Player


class Model:
    def __init__(self) -> None:
        self.view = View()
        self.match = False
        self.GameObjects = dict()

    def initMatch(self):
        self.GameObjects = dict(player1=Player())
        self.runMatch()

    def runMatch(self):
        self.match = True
        # while self.match:
        #     pass
