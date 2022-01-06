from turtle import Turtle


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_screen()

    
    def update_screen(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def left_score(self):
        self.l_score += 1
        self.update_screen()
    

    def right_score(self):
        self.r_score += 1
        self.update_screen()
    

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Courier", 80, "normal"))


    
