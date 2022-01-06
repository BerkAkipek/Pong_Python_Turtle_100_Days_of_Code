from turtle import Turtle


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xdist = 10
        self.ydist = 10
        self.move_speed = 0.1
    

    def move(self):
        new_x = self.xcor() + self.xdist
        new_y = self.ycor() + self.ydist
        self.goto(new_x, new_y)

    
    def bounce_y(self):
        self.ydist *= -1
        

    def bounce_x(self):
        self.xdist *= -1
        self.move_speed *= 0.8
    

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1