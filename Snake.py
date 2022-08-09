import arcade
import random

class Snake(arcade.Sprite):
    def __init__(self,width , height):
        super().__init__()
        self.width = 16
        self.height = 16
        self.speed = 4
        self.color_1 = arcade.color.GREEN
        self.color_2 = arcade.color.DARK_GREEN
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.center_x = width // 2
        self.center_y = height // 2
        self.body = []

    def eat(self, eat):
        if eat == 1:
            self.score += 1
        elif eat == 2:
            self.score -= 1
        elif eat == 3:
            self.score -= 1

    def move(self):
        self.body.append((self.center_x, self.center_y))
        if len(self.body) > self.score:
            self.body.pop(0)
        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed
        elif self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y < 0:
            self.center_y -= self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color_1)
        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_1)
            else:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color_2)
