from turtle import Screen
from bat1 import Bat1
from bat2 import Bat2
from ball import Ball
from border import Border
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("blue")
screen.tracer(0)

bat1 = Bat1()
bat2 = Bat2()
ball = Ball()
border = Border()
border.draw_border()



screen.listen()
screen.onkeypress(bat1.up,"w" )
screen.onkeypress(bat1.up,"W" )
screen.onkeypress(bat1.down,"s")
screen.onkeypress(bat1.down,"S")
screen.onkeypress(bat2.up,"Up" )
screen.onkeypress(bat2.down,"Down" )


is_game_on = True
while is_game_on :
    screen.update()
    time.sleep(0.007)
    ball.first_move()
    ball.move()
    ball.border_touch()
    if   (ball.xcor() >= 320 and ball.xcor() < 323 ) and (bat2.ycor() - 50 < ball.ycor() < bat2.ycor() + 50)  :
        ball.bat_touch()
    if   (ball.xcor() <= -320 and ball.xcor() > -323 ) and (bat1.ycor() - 50 < ball.ycor() < bat1.ycor() + 50)  :
        ball.bat_touch()
        
    if abs(ball.xcor())  >= 390 :
        border.Game_Over()
        is_game_on = False




































screen.exitonclick()