from turtle import Turtle

from constants import DOWN, LEFT, OPPOSITE, RIGHT, STARTING_POSITIONS, STEP, UP

RAINBOW_COLORS = ("red", "orange", "yellow", "green", "blue", "indigo", "violet")


class Snake:
    def __init__(self):
        self.segments = []
        self.direction = RIGHT
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color(RAINBOW_COLORS[len(self.segments) % len(RAINBOW_COLORS)])
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.head.setheading(self.direction)
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].position())
        self.head.forward(STEP)

    def up(self):
        self._turn(UP)

    def down(self):
        self._turn(DOWN)

    def left(self):
        self._turn(LEFT)

    def right(self):
        self._turn(RIGHT)

    def _turn(self, new_direction):
        # One queued turn per tick. A second key in the same frame cannot reverse the snake.
        if new_direction != OPPOSITE[self.direction]:
            self.direction = new_direction

    def hit_wall(self, limit):
        x, y = self.head.xcor(), self.head.ycor()
        return abs(x) > limit or abs(y) > limit

    def hit_tail(self):
        return any(self.head.distance(segment) < STEP / 2 for segment in self.segments[1:])

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.direction = RIGHT
        self.create_snake()
        self.head = self.segments[0]
