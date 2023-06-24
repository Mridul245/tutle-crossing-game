import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

car = CarManager()

score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    for car1 in car.all_cars:
        if car1.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish_line():
        player.goto_start()
        car.increase_speed()
        score_board.increase_level()

screen.exitonclick()
