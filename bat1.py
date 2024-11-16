from turtle import Turtle

class Bat1(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("square")
        self.color("lavender")
        self.shapesize(1,5)
        self.penup()
        self.goto(-340,-120)
        self.st()
        self.setheading(90)


    def up (self):
        self.forward(20)

    def down (self):
        self.backward(20)