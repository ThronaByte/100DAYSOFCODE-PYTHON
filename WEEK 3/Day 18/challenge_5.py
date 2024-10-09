import turtle
from turtle import Turtle, Screen
import random
derik = Turtle()
derik.shape("circle")
derik.color("red")


# #Challenge 5
direction = [0, 90, 180, 270]
turtle.colormode(255)
def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r, g, b)
    return tup

derik.width(5)
derik.speed(17)
for _ in range(1,50):
    derik.forward(50)
    derik.color(random_colors())
    derik.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()