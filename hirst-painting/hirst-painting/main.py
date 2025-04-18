import colorgram as cg
import turtle as t
from turtle import Screen
import random
t.colormode(255)

# Objective: To create a 10 X 10 hirst painting
# pensize = 20
# spaced apart = 50

rgb_colors = [(30, 106, 145), (229, 153, 80), (15, 169, 207), (148, 79, 30), (6, 57, 97), (31, 134, 77),
              (214, 133, 162), (138, 32, 51), (205, 156, 22), (118, 172, 194), (213, 93, 124),
              (235, 211, 85), (6, 103, 66), (145, 185, 167), (216, 209, 11), (3, 69, 136),
              (15, 49, 43), (76, 83, 23), (243, 168, 151), (134, 59, 83), (53, 60, 15),
              (223, 170, 191), (230, 100, 40), (1, 90, 120), (71, 157, 105), (164, 29, 25)]

# # to extract the colors from the image
# colors = cg.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)

pen = t.Turtle()
pen.speed("fastest")

# # first attempt
# for rows in range(10):
#     for cols in range(9):
#         pen.dot(20, random.choice(rgb_colors))
#         pen.penup()
#         pen.forward(50)
#         pen.pendown()
#     if pen.heading() == 0:
#         pen.setheading(90)
#         pen.dot(20, random.choice(rgb_colors))
#         pen.penup()
#         pen.forward(50)
#         pen.pendown()
#         pen.setheading(180)
#     elif pen.heading() == 180:
#         pen.setheading(90)
#         pen.dot(20, random.choice(rgb_colors))
#         pen.penup()
#         pen.forward(50)
#         pen.pendown()
#         pen.setheading(0)

# optimized solution
pen.penup()
pen.setheading(225)
pen.forward(300)
pen.setheading(0)
pen.hideturtle()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    pen.dot(20, random.choice(rgb_colors))
    pen.forward(50)

    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


screen = Screen()
screen.exitonclick()
