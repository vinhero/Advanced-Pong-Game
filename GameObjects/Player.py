import pygame
import IGameObject


class Player(IGameObject):
    def __init__(self):
        self.ActualPosX = 0
        self.ActualPosY = 0
        self.PosX = 0
        self.PosY = 0
        self.body_width = 20
        self.body_height = 100
        self.body_color = pygame.Color(255, 255, 255)
        self.body = pygame.Rect(
            x=self.PosX,
            y=self.PosY,
            width=self.body_width,
            height=self.body_height,
            color=self.body_color
        )
        self.speed = 20

    def moveUp(self):
        self.ActualPosY - self.speed
        self.update_actualPos(self.ActualPosX, self.ActualPosY)

    def moveDown(self):
        self.ActualPosY + self.speed
        self.update_actualPos(self.ActualPosX, self.ActualPosY)

    def update_actualPos(self, actualX, actualY):
        self.ActualPosX = actualX
        self.ActualPosY = actualY

    def update(self):
        moveX = round(self.ActualPosX) - self.PosX
        moveY = round(self.ActualPosY) - self.PosY
        self.body.move(moveX, moveY)
