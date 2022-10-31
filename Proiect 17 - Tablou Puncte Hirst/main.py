color_list = [ (35, 108,167) , (245, 77, 36) , (112, 163 , 211) , (153 , 57 ,85) , 
(219,156,94) ,(201,60,27) , (24,133,55) , (246 ,204 ,55) , (225,119,152) , (46, 53, 121) ]

import random 
import turtle as turtle_module 
turtle_module.colormode(255)
timy = turtle_module.Turtle()

timy.penup()
timy.speed('fastest')
timy.hideturtle()

timy.setheading(255)
timy.forward(300)
timy.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    timy.dot(20, random.choice(color_list))
    timy.forward(50)

    if dot_count % 10 == 0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)







timy.dot(20, random.choice(color_list))

screen = turtle_module.Screen()
screen.exitonclick()