from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard
# pong = Turtle()
# TODO: 1 Create the screen
screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
# TODO: 2 Create and move a paddle
r_paddle = Paddle((350,0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "space")

# TODO: 3 Create another paddle
l_paddle = Paddle((-350,0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
score_board = ScoreBoard()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

# TODO: 4 Create the ball and make it move
    ball.move()

# TODO: 5 Detect collision with ball and bounce
    if ball.ycor() > 280  or ball.xcor() < -280:
        ball.bounce_y()
# TODO: 6 Detect collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

# TODO: 7 Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        # TODO: 8 Keep Score
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        # TODO: 8 Keep Score
        score_board.r_point()



screen.exitonclick()