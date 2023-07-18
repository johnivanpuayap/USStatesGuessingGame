import turtle
import pandas as pd

# Create the Screen and Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.color("Black")

background_image = 'blank_states_img.gif'
screen.addshape(background_image)
turtle.shape(background_image)

# Create the game data
correct_states = 0

# Load States
states_data = pd.read_csv("50_states.csv")
states = states_data.state.to_list()


# Functions

def print_state(state):
    state_data = states_data[states_data.state == state]
    print(state_data)
    xcor = state_data.iloc[0, 1]
    ycor = state_data.iloc[0, 2]
    tim.goto(xcor, ycor)
    tim.write(f"{state}", align="center", font=("Arial", 10, "bold"))


# Main Game Loop

while True:
    answer_state = screen.textinput(f"{correct_states}/50 States Correct", "What is the state name?: ")

    if answer_state is None:
        print("Exiting..")
        break

    if answer_state in states:
        print("You are correct")
        correct_states += 1
        states.remove(answer_state)
        print_state(answer_state)
    else:
        print("You are incorrect")

    if correct_states == 50:
        print("You Win")


turtle.mainloop()
