from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold2")
        self.penup()
        # self.x = random.randint(1,6)
        self.x = 5
        self.angle = 0
        self.start = True
        self.keep_moving = True



    def move(self):
        self.forward(1)
        
    def first_move(self):
        if self.start :
            if self.x == 1 :
                    self.setheading(150)
                    self.move()
                    self.start = False

            elif self.x == 2:
                    self.setheading(330)
                    self.move()
                    self.start = False

            elif self.x == 3:
                    self.setheading(210)
                    self.move()
                    self.start = False

            elif self.x == 4:
                    self.setheading(120)
                    self.move()
                    self.start = False

            elif self.x == 5 :
                    self.setheading(30)
                    self.move()
                    self.start = False

            elif self.x == 6:
                    self.setheading(60)
                    self.move()
                    self.start = False


    def border_touch(self):
        if self.ycor() >= 290  :
            self.angle = 360 - self.heading() 
            self.setheading(self.angle)
            self.move()
        elif self.ycor() <=  -290 :
            self.angle = 360 - self.heading()
            self.setheading(self.angle)
            self.move()
    def bat_touch(self):
        self.angle = 180 - self.heading()
        self.setheading(self.angle)
        self.move()
    def edge_touch(self):
            self.angle = 360 - self.heading() 
            self.setheading(self.angle)
            self.move()

    

    


            



