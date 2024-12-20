# Day 25
# Learning to work with csv files
# Also learning about the pandas library
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
screen.setup(width=700, height=500)


data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

user_score = 0
guessed_states = []

states_missing = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{user_score}/50 States Correct",
    prompt="What's another state name?").title()

    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                states_missing.append(state)
        df = pandas.DataFrame(states_missing)
        df.to_csv("states_to_learn")
        break
    if answer_state in states:
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            guessed_states.append(answer_state)
            user_score += 1
            state_data = data[data.state == answer_state]
            coord = (state_data.x.item(), state_data.y.item())
            t.goto(coord)
            t.write(answer_state)


turtle.mainloop()
