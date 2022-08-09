import arcade
import random

class Apple(arcade.Sprite):
    def __init__(self, width , height ):
        super().__init__()
        self.image = "apple.jpeg"
        self.apple = arcade.Sprite(self.image, 0.025)
        self.apple.center_x = random.randint(10, width - 10)
        self.apple.center_y = random.randint(10, height - 10)

    def draw(self):
        self.apple.draw()
