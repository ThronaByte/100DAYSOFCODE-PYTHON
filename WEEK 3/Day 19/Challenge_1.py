from turtle import Turtle, Screen

# from colorama.ansi import clear_screen

byte = Turtle()
screen = Screen()

def move_forward():
    byte.forward(10)

def move_backward():
    byte.backward(10)

def turn_left():
    byte.left(10)

def turn_right():
    byte.right(10)

def clear():
    byte.clear()
    byte.penup()
    byte.home()
    byte.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear, "c")
screen.listen()

screen.exitonclick()
