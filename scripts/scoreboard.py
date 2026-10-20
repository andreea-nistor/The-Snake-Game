from pathlib import Path
from turtle import Turtle

POSITION = (0, 280)
DATA_FILE = Path(__file__).with_name("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self._read_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"SCORE = {self.score}   High score = {self.high_score}",
            align="center",
            font=("Courier", 12, "bold"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def _read_high_score(self):
        try:
            return int(DATA_FILE.read_text().strip())
        except (OSError, ValueError):
            return 0

    def _save_high_score(self):
        try:
            DATA_FILE.write_text(str(self.high_score))
        except OSError:
            return
