import arcade
import random

class Golabi (arcade.Sprite):
    def __init__(self, width , height):
        super().__init__()
        self.image = "Golabi.jpeg"
        self.Golabi = arcade.Sprite(self.image, 0.11)
        self.Golabi.center_x = random.randint(10, width - 10)
        self.Golabi.center_y = random.randint(10, height - 10)

    def draw(self):
        self.Golabi.draw()
       
