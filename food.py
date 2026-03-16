from turtle import Turtle
import random as r
SHAPES=["circle", "arrow", "triangle", "turtle"]
COLORS=["pale green", "yellow", "brown"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.choose_food()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        random_x=r.randint(-280, 280)
        random_y=r.randint(-280, 280)
        self.goto(random_x, random_y)

    def choose_food(self):
        self.shape(r.choice(SHAPES))
        self.color(r.choice(COLORS))

    def refresh(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 260)
        self.choose_food()
        self.goto(random_x, random_y)


