from turtle import Screen 
from snake import Snake  
import time
from food import Food 
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

screen.bgcolor('black')
screen.title('Joc sarpe')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')




game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #detecteaza coliziune mancare
    if snake.head.distance(food)<13:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detecteaza coliziunea cu pereti
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or  snake.head.ycor() > 290 or  snake.head.ycor() < -290:
       game_is_on = False
       scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False 
            scoreboard.game_over()

screen.exitonclick()