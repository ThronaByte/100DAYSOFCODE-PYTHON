import turtle
from turtle import Turtle, Screen
from random import random, choice

colors = [(243, 242, 239), (171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (242, 237, 240), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244), (235, 241, 235), (207, 168, 79), (120, 21, 54), (137, 63, 91), (3, 29, 122), (169, 183, 228), (132, 175, 140), (220, 174, 190), (95, 148, 106), (230, 178, 160), (169, 206, 175), (12, 81, 26)]

derik = Turtle()
derik.speed(35)
derik.shape('turtle')
turtle.colormode(255)

derik.penup()
derik.hideturtle()
derik.setheading(225)
derik.forward(300)
derik.setheading(0)
# derik.forward(50)
num_of_dot = 101

for dots in range(1, num_of_dot):
    derik.dot(17, choice(colors))
    derik.forward(50)
#
    if dots % 10 == 0:
        derik.setheading(90)
        derik.forward(50)
        derik.setheading(180)
        derik.forward(500)
        derik.setheading(0)














screen = Screen()
screen.exitonclick()