import turtle
from turtle import Turtle, Screen
import random
derik = Turtle()
derik.shape("circle")
derik.color("red")

# #Challenge 4
colors = [
    "blue", "yellow", "black", "red", "green", "violet", "brown", "darkblue",
    "darkmagenta", "pink", "darkred", "darkslateblue"
]
direction = [0, 90, 180, 270]
for _ in range(1,50):
    derik.width(5)
    derik.forward(50)
    derik.speed(3)
    derik.color(random.choice(colors))
    derik.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()