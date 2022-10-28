from snake import Snake
from screen_settings import *
import time
import sound_effect
from score_board import ScoreBoard
from food import Food

GAME_DIMENSION_LIMIT = 290
game_speed = 0.1


sound_effect.background_music('off')
score_board = ScoreBoard()
snake = Snake()
food = Food()
screen.update()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')

game_running = True
while game_running:
    score_board.update()
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        sound_effect.eating()
        snake.extend()
        food.refresh()
        score_board.score += 1

    # Detect collision with the wall
    if snake.head.xcor() > GAME_DIMENSION_LIMIT or snake.head.xcor() < -GAME_DIMENSION_LIMIT or snake.head.ycor() > GAME_DIMENSION_LIMIT or snake.head.ycor() < -GAME_DIMENSION_LIMIT:
        food.hideturtle()
        score_board.game_over()
        game_running = False

    # Detect collision with the body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            food.hideturtle()
            score_board.game_over()

    if 50 <= score_board.score < 30:
        game_speed = 0.030
    elif 20 <= score_board.score < 10:
        game_speed = 0.050
    elif score_board.score >= 10:
        game_speed = 0.075

screen.exitonclick()
