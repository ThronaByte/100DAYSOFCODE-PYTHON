import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to The Turtle Race!")
user_bet = screen.textinput(title="Place Your Bet",
                            prompt="Which turtle will win? (blue, black, red, green, violet or brown) ")

colors = ["blue", "black", "red", "green", "violet", "brown"]
while user_bet not in colors:
    user_bet = screen.textinput(title="Place Your Bet",
                                prompt="Color does not exist try again!"
                                       "\nWhich turtle will win? (blue, black, red, green, violet or brown) ")

all_turtle = []
y_pos = [-60, -20, 30, 70, 100, 140]

for index in range(6):
    each_turtle = Turtle(shape="turtle")
    each_turtle.penup()
    each_turtle.color(colors[index])
    each_turtle.goto(x=-230, y=y_pos[index])
    all_turtle.append(each_turtle)

finish_line = Turtle()
finish_line.penup()
finish_line.goto(200, 200)
finish_line.setheading(270)
finish_line.pendown()
finish_line.pensize(5)
finish_line.color("black")
finish_line.goto(200, -140)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 190:
            race_on = False
            winner_color = turtle.pencolor()

            announcer = Turtle()
            announcer.penup()
            announcer.hideturtle()
            announcer.goto(x=0, y=0)

            if winner_color == user_bet:
                announcer.write(f"{winner_color.capitalize()} turtle wins!\n\n", align="center",
                                font=("Arial", 18, "bold"))
                # print(f"You've won! The {winner_color} turtle is the winner!".title())
            else:
                announcer.write(f"You've lost! {winner_color.capitalize()} turtle wins!", align="center",
                                font=("Arial", 18, "bold"))
                # print(f"You've lost! The {winner_color} turtle is the winner!".title())
            break

screen.exitonclick()