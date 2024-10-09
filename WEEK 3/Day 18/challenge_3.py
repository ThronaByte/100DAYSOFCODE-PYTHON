import turtle
from turtle import Turtle, Screen
import random
derik = Turtle()
derik.shape("circle")
derik.color("red")

# # Challenge 3
colors = [
    "blue", "yellow", "black", "red", "green", "violet", "brown", "darkblue",
    "darkmagenta", "pink", "darkred", "darkslateblue"
]
def shapes(sides):
    angle = 360 / sides
    for _ in range(sides):
        derik.forward(100)
        derik.left(angle)
        derik.width(5)
for shape_side in range(3, 10):
    derik.color(random.choice(colors))
    shapes(shape_side)



screen = Screen()
screen.exitonclick()