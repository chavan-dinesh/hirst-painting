# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('sample_image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle
from turtle import Screen


turtle.colormode(255)
tim = turtle.Turtle()

# def random_color():
color_list = [(234, 220, 200), (214, 159, 97), (208, 230, 215), (45, 107, 146), (125, 165, 192), (237, 212, 222), (202, 137, 159), (208, 220, 233), (125, 181, 155), (147, 65, 92), (39, 130, 95), (182, 161, 35), (159, 82, 51), (226, 201, 119), (197, 84, 110), (213, 88, 66), (60, 165, 133), (139, 28, 46), (234, 163, 180), (47, 160, 183), (159, 210, 191), (10, 104, 81), (112, 116, 167), (237, 169, 158), (22, 52, 80), (135, 33, 23), (33, 58, 113), (74, 34, 22), (150, 208, 218), (18, 63, 47)]

tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(220)
tim.forward(280)
tim.setheading(0)

def draw(x, y, space):
    for i in range(x):
        for j in range(y):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(space)
        tim.left(90)
        tim.left(90)
        tim.penup()
        tim.forward(space * x)
        tim.right(90)
        tim.forward(space)
        tim.right(90)


tim.penup()
draw(10, 10, 50)

screen = Screen()
screen.exitonclick()
