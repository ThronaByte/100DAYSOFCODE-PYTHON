from turtle import Turtle, Screen
derik = Turtle()
derik.shape("circle")
derik.color("red")

# #Challenge 2
for _ in range(15):
    derik.forward(10)
    derik.penup()
    derik.forward(10)
    derik.pendown()



screen = Screen()
screen.exitonclick()