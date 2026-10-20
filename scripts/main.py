import time
from turtle import Screen

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, STEP, TICK_SECONDS, WALL_LIMIT
from food import Food
from scoreboard import Scoreboard
from snake import Snake


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()

    snake = Snake()
    food = Food(snake.segments)
    score = Scoreboard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True

    def stop_game():
        nonlocal game_is_on
        game_is_on = False

    screen.onkey(stop_game, "Escape")

    while game_is_on:
        screen.update()
        time.sleep(TICK_SECONDS)
        snake.move()

        if snake.head.distance(food) < STEP / 2:
            snake.extend()
            score.increase_score()
            food.refresh(snake.segments)

        if snake.hit_wall(WALL_LIMIT) or snake.hit_tail():
            score.reset()
            snake.reset()
            food.refresh(snake.segments)

    screen.exitonclick()


if __name__ == "__main__":
    main()
