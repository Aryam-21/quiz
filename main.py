from turtle import Turtle, Screen
import turtle
import pandas
screen = Screen()
screen.title("U.S. STATES GUESSING GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
data = pandas.read_csv("50-states.txt")
all_states = data.state.to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"You {len(guessed_state)}/50 Guess state in U.S",
                                    prompt="what is another state?").title()

    if answer_state == "Exit":
        missed_state = [state for state in all_states if state not in guessed_state]
        file = pandas.DataFrame(missed_state)
        file.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.color("black")
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))