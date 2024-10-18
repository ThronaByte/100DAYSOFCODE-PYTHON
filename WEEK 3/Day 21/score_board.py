from turtle import Turtle
ALIGN = "center"
FONT = ("Verdana", 23, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",  align=ALIGN, font=FONT)

    def update_score(self):
        self.write(f"Score: {self.score}",  align=ALIGN, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()