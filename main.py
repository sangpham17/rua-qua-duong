from pickle import TRUE
from turtle import Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.up, 'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # phat hien va cham voi xe
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # phat hien toi dich
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
