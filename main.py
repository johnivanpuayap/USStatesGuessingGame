import turtle
import pandas as pd

# Create the Screen
screen = turtle.Screen()
screen.title("U.S. States Game")

background_image = 'blank_states_img.gif'
screen.addshape(background_image)
turtle.shape(background_image)

# Create the game data
correct_states = 0

# Load States
states_data = pd.read_csv("50_states.csv")
print(states_data)

answer_state = screen.textinput(f"{correct_states}/50 States Correct", "What is the state name?: ")


turtle.mainloop()
