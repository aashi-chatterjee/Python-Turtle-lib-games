import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

#     detect collision of car w/turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            # player.color("red")
            scoreboard.game_over()
            game_is_on = False


#     detect turtle finishing the race
    if player.has_succeeded():
        car_manager.level_up()
        player.reset_position()
        scoreboard.increase_level()

screen.exitonclick()
