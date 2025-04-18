import turtle as turtle_module
from turtle import Screen

pen = turtle_module.Turtle()

# W - forwards
# S - Backwards
# A - counter-clockwise (left)
# D - clockwise (right)
# C - Clear and bring pen to center
screen = Screen()


def move_forward():
    pen.forward(10)


def move_back():
    pen.back(10)


def turn_right():
    # pen.right(10)
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)


def turn_left():
    # pen.left(10)
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)


def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()