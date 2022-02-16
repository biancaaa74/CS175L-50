# Bianca Beltran
# stop_sign.py
# CS-175L

import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

for x in range(8):
    turtle.forward(100)
    turtle.right(45)


turtle.penup()
turtle.goto(30,-135)
turtle.pendown()
style = ('Courier',20)
turtle.write('STOP',font = style)

# stack overflow for help
