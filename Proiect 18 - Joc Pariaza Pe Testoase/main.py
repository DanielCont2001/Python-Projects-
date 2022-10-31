from turtle import Turtle, Screen 
import random 

screen = Screen()
screen.bgcolor('pink')
screen.title('Joc Pariaza Pe Testoase')

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Creeaza un pariu", prompt="Tasteaza culoarea")
colors = ["red" , "orange", "green", "purple" , "blue", "yellow"]
y_position = [-70 , -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet: 
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Ai castigat! Culoarea {winning_color} a testoasei este castigatoare!")
            else: 
                print("Ai pierdut! ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
