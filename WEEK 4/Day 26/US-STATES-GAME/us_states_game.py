from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("US-STATE-GAME")
IMAGE= "blank_state_img.gif"
screen.addshape(IMAGE)


map_turtle = Turtle()
map_turtle.shape(IMAGE)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

state_writer = Turtle()
state_writer.hideturtle()
state_writer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct? ",
                                    prompt="What another state's name")
    # print(answer_state)
    if answer_state is None:
        break

    # Convert the input to title case for consistency
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_data=pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # print(answer_state)

        states_data= data[data.state == answer_state]
        state_writer.goto(int(states_data.x.iloc[0]), int(states_data.y.iloc[0]))
        state_writer.write(answer_state)

screen.exitonclick()
    # break
    # if answer_state in each_data:
    #     print(f"YES")
    #     break
# print(data)
# if answer_state in