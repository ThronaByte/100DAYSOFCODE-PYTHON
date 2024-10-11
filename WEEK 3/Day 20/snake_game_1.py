from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO: 1 Create a snake body
snake = Snake()


# TODO: 3 Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.d, "9")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# TODO: 2 Move the snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
