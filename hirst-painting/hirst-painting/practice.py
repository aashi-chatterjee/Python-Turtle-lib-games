import random
import turtle as t
from turtle import Screen
t.colormode(255)
pen = t.Turtle()

# # to draw a dashed line
# for steps in range(15):
#     pen.forward(10)
#     pen.penup()
#     pen.forward(10)
#     pen.pendown()

# # drawing different shapes with different colours
# sides = 3
# colours = ["dark slate blue", "medium purple", "orchid", "magenta", "medium violet red", "orange red", "medium blue",
#            "lime green", "medium turquoise", "dark red", "black"]
# while sides != 11:
#     angle = 360 / sides
#     pen.color(random.choice(colours))
#     for side in range(sides):
#         pen.forward(100)
#         pen.right(angle)
#     sides += 1

# # drawing a random walk
# pen.pensize(10)
# pen.speed(10)
# directions = ["forward", "right", "left", "back"]
#
# def movement(paces):
#     while paces > 0:
#         pen.color(random.choice(colours))
#         random_dir = random.choice(directions)
#         if random_dir == "forward":
#             pen.forward(20)
#         elif random_dir == "back":
#             pen.back(20)
#         elif random_dir == "right":
#             pen.right(90)
#             pen.forward(20)
#         elif random_dir == "left":
#             pen.left(90)
#             pen.forward(20)
#         paces -= 1
#
# movement(50)

# # drawing a walk (better)
# direction = [0, 90, 180, 270]

# randomizing colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
#
# pen.pensize(8)
# pen.speed("fastest")
# for steps in range(200):
#     pen.color(random_color())
#     pen.forward(30)
#     pen.setheading(random.choice(direction))

# drawing a spirograph
def draw_spirograph(number_of_circles):
    angle = 360/number_of_circles
    while number_of_circles > 0:
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + angle)
        number_of_circles -= 1

pen.speed("fastest")
draw_spirograph(100)


screen = Screen()
screen.exitonclick()
