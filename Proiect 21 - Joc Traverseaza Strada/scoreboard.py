from turtle import Turtle

FONT = ("Courier" , 24 , "normal" )

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
    
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-280,250)

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Level: {self.level}" , align="left", font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-100,0)
        self.color("red")
        self.write(f"GAME OVER" , align="left", font=FONT)