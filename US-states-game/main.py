import turtle
import pandas

screen = turtle.Screen()
pen = turtle.Turtle()
screen.title("U.S. States Game")
us_image = "blank_states_img.gif"
screen.addshape(us_image)

turtle.shape(us_image)

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()

# game_is_on = True
correct_guesses = 0
correct_guess_list = []

while len(correct_guess_list) < 50:
    guessed_answer = (screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                       prompt="What's a state name?")).title()
    if guessed_answer == "Exit":
        missed_states = []
        for state in state_list:
            if state not in correct_guess_list:
                missed_states.append(state)
        break
    if guessed_answer in state_list:
        correct_guesses += 1
        correct_guess_list.append(guessed_answer)
        coordinates = states_data[states_data["state"] == guessed_answer]
        x_cor = coordinates["x"].item()
        y_cor = coordinates["y"].item()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_cor, y_cor)
        pen.pendown()
        pen.write(guessed_answer)

# states missed by the player stored into a csv file
data = pandas.DataFrame(missed_states)
data.to_csv("States_to_learn.csv")
