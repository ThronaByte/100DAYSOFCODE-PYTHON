from turtle import Turtle, Screen
from snake import Snake
import time
from snake_food import Food
from score_board import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO: 1 Create a snake body
snake = Snake()

# TODO: 4 Detect collision with food
food = Food()

# TODO: 5 Create a scoreboard
score = Score()


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

# TODO: 4 Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

# TODO: 6 Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280  or snake.head.ycor() < -280:
        score.reset()

# TODO: 7 Detect collision with tail
    for movement in snake.movement:
        if movement == snake.head:
            pass
        elif snake.head.distance(movement) < 18:
            score.reset()
            snake.reset()

screen.exitonclick()
