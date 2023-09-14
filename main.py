from turtle import Turtle, Screen
import random

screen1 = Screen()
screen1.setup(width=500, height=400)
user_input = screen1.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a colour:").lower()
colour_list = ["red", "orange", "yellow", "green", "blue", "purple"]
y_val = -125
is_on = False
turtle_list =[]
for n in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colour_list[n])
    new_turtle.goto(x=-230, y=y_val)
    y_val += 50
if user_input:
    is_on = True

while is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_on = False
            if user_input == turtle.pencolor():
                print(f"You won, Your {user_input} turtle won")
            else:
                print(f"You lose, {turtle.pencolor()} turtle won")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen1.exitonclick()
