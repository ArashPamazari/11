import arcade
import random

class PU (arcade.Sprite):
    def __init__(self, width , height):
        super().__init__()
        self.image = "pu.jpeg"
        self.PU = arcade.Sprite(self.image, 0.05)
        self.PU.center_x = random.randint(10, width - 10)
        self.PU.center_y = random.randint(10, height - 10)

    def draw(self):
        self.PU.draw()

