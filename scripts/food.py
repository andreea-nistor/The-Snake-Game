import random
from turtle import Turtle

from constants import STEP, WALL_LIMIT


class Food(Turtle):
    def __init__(self, snake_segments):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh(snake_segments)

    def refresh(self, snake_segments):
        occupied = {(round(segment.xcor()), round(segment.ycor())) for segment in snake_segments}
        cells = range(-WALL_LIMIT, WALL_LIMIT + 1, STEP)
        free = [(x, y) for x in cells for y in cells if (x, y) not in occupied]
        if free:
            self.goto(random.choice(free))
