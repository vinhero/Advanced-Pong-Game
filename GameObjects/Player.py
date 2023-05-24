import pygame
from GameObjects.IGameObject import IGameObject


class Player(IGameObject):
    def __init__(self, actualx, actualy):
        self.ActualPosX = actualx
        self.ActualPosY = actualy
        self.body_width = 20
        self.body_height = 100
        self.body_color = pygame.Color(255, 255, 255)
        self.body = pygame.Rect(
            self.ActualPosX,
            self.ActualPosY,
            self.body_width,
            self.body_height
            # height=self.body_height,
            # color=self.body_color
        )
        self.speed = 20

    def moveUp(self):
        self.ActualPosY = self.ActualPosY - self.speed
        self.update_actualPos(self.ActualPosX, self.ActualPosY)

    def moveDown(self):
        self.ActualPosY = self.ActualPosY + self.speed
        self.update_actualPos(self.ActualPosX, self.ActualPosY)

    def update_actualPos(self, actualX, actualY):
        self.ActualPosX = actualX
        self.ActualPosY = actualY

    def update(self):
        moveX = round(self.ActualPosX) - self.body.x
        moveY = round(self.ActualPosY) - self.body.y
        # self.body.move(moveX, moveY)
        #     if (player1.y + speed + height < screen_height):
        #     if (player1.y - speed > 0):
        self.body.x = self.body.x + moveX
        self.body.y = self.body.y + moveY

        print("")
        print("MoveX: " + str(moveX) + " MoveY: " + str(moveY))
        print("X: " + str(self.body.x) + " Y: " + str(self.body.y))

    # def draw(self, surface):
    #     pygame.draw()
