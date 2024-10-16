from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_pos()
        self.setheading(90)
        self.is_moving = False


    def go_up(self):
        if self.is_moving:
            self.forward(MOVE_DISTANCE)

    def start_moving(self):
        self.is_moving = True
        self.go_up()  # Start moving the player

    def stop_moving(self):
        self.is_moving = False

    def start_pos(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return  False