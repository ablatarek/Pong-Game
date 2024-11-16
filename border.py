from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.pencolor("white")
        self.speed(0)

    def draw_border(self):
        self.teleport(400,300)
        self.pendown()
        self.goto(400,-300)
        self.goto(-400,-300)
        self.goto(-400,300)
        self.goto(400,300)

    def Game_Over(self):
        self.penup()
        self.goto(0,200)
        self.pendown()
        self.write("Game Over",align="Center",font=("Arial",30,"bold"))