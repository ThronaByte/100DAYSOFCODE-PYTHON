from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        ball_x = self.xcor() + self.x_move
        ball_y = self.ycor() + self.y_move
        self.goto(ball_x, ball_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.7
    def reset_pos(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
