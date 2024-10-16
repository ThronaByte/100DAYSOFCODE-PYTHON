import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


# TODO: 1 Move the Turtle with Keypress
screen.listen()
screen.ontimer(player.go_up, 100)
screen.onkeypress(player.start_moving, "Up")
screen.onkeyrelease(player.stop_moving, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # TODO: 2 Create and mover cars
    car_manager.create_car()
    car_manager.move()

    # TODO: 3 Detect Collision with wall
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False
    # TODO: 4 Detect When the Turtle reaches the other side

    if player.finish_line():
        player.start_pos()
        car_manager.level_up()

    # TODO: 5 Create Scoreboard
        score_board.increase_level()

screen.exitonclick()