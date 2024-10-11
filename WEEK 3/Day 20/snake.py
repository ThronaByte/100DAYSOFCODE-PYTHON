from turtle import Turtle
SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.movement = []
        self.snake_move()
        self.head = self.movement[0]

    def snake_move(self):
        for position in SNAKE_POSITION:
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)
            self.movement.append(snake_body)

    def move(self):
        snake_movement = self.movement
        for moves in range(len(snake_movement)-1, 0, -1):
            new_x =  snake_movement[moves -1].xcor()
            new_y =  snake_movement[moves -1].ycor()
            snake_movement[moves].goto(new_x, new_y)
        self.head.forward(SNAKE_DISTANCE) #forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def d(self): #to go down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
