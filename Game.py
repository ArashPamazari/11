import arcade
import random
from Apple import Apple
from Snake import Snake
from Golabi import Golabi
from PU import PU

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Game(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height, "snake game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(width ,height )
        self.apple = Apple(width,height)
        self.Golabi = Golabi(width,height)
        self.PU = PU(width,height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Score : ' + str(self.snake.score), 2, 480, arcade.color.BLACK, 14, 1000, 'left')
        self.snake.draw()
        self.apple.draw()
        self.Golabi.draw()
        self.PU.draw()

        if self.snake.score < 0 or self.snake.center_x <= 0 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREEN_WIDTH:
            arcade.draw_text('GAME OVER', 150, 250, arcade.color.RED, font_size=12)
            arcade.exit()

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple.apple):
            apple = 1
            self.apple = Apple()
            self.snake.eat(apple)

        if arcade.check_for_collision(self.snake, self.PU.PU):
            pu = 2
            self.PU = PU()
            self.snake.eat(pu)

        if arcade.check_for_collision(self.Golabi.Golabi, self.snake):
            golabi = 3
            self.Golabi = Golabi()
            self.snake.eat(golabi)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1