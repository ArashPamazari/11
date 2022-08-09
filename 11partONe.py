import arcade
arcade.open_window(500, 500, 'Loop')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
width = 20
height = 20

center_x = 200
center_y = 200

for row in range(10):
    for column in range(10):
        if (row + column) % 2 == 0:
            arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.RED, 45)
        else:
            arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.BLUE, 45)
        center_x += 20

    center_x = 200
    center_y += 20

arcade.finish_render()
arcade.run()