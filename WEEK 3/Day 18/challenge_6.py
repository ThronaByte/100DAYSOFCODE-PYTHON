import turtle
from turtle import Turtle, Screen
import random
derik = Turtle()
derik.shape("circle")
derik.color("red")



# #Challenge 6
turtle.colormode(255)
def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r, g, b)
    return tup

derik.speed(17)
def spirograph(gap):
    for _ in range(int(360 / gap)):
        derik.circle(90)
        derik.position()
        derik.color(random_colors())
        derik.setheading(derik.heading() + gap)
spirograph(3)

screen = Screen()
screen.exitonclick()