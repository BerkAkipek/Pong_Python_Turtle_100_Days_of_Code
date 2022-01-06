from turtle import Turtle


class Paddle(Turtle):


    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)
        self.score = 0


    def move_up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    
    def move_down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)


