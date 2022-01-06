from turtle import Screen, left
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
from time import sleep


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle_position = (-350, 0)
right_paddle_position = (350, 0)
l_paddle = Paddle(left_paddle_position)
r_paddle = Paddle(right_paddle_position)

ball = Ball()

score_board = ScoreBoard()

def new_func(screen, l_paddle, r_paddle):
    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w" )
    screen.onkey(l_paddle.move_down, "s")

new_func(screen, l_paddle, r_paddle)


is_game_on = True
while is_game_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() >= 330 and r_paddle.distance(ball) < 60 and ball.xdist > 0 or ball.xcor() <= -330 and l_paddle.distance(ball) < 60 and ball.xdist < 0:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score_board.left_score()
    
    if ball.xcor() < -400:
        ball.reset_position()
        score_board.right_score()
    
    if score_board.r_score + score_board.l_score == 10:
        score_board.game_over()
        is_game_on = False


screen.exitonclick()

