import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Python Python")
screen.tracer(0)


def draw_border():
    border = Turtle()
    border.penup()
    border.color("white")
    border.goto(-290, -290)  # Adjust so the border is just inside the screen
    border.pendown()
    border.speed("fastest")
    for _ in range(4):
        border.forward(580)  # Adjust the length to fit inside the window
        border.left(90)
    border.hideturtle()


draw_border()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()


def setup_key_bindings():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "W")
    screen.onkey(snake.down, "S")
    screen.onkey(snake.left, "A")
    screen.onkey(snake.right, "D")
    screen.onkey(game_restart, "r")  # Add event listener for "R" key press


def exit_game():
    turtle.bye()


screen.onkeypress(exit_game, "Escape")  # Bind the Escape key to exit_game function

def game_restart():
    global game_state, move_speed
    snake.reset()  # Reset the snake to the starting position
    scoreboard.reset()  # Reset the scoreboard
    food.refresh()  # Move the food to a new position
    move_speed = 0.1  # Reset the move speed
    screen.update()
    setup_key_bindings()
    game_state = "PLAYING"  # Ensure the game loop knows to continue running


def game_over():
    global game_state
    game_state = "GAME_OVER"
    scoreboard.game_overs()


setup_key_bindings()
game_state = "PLAYING"
move_speed = 0.1
speed_increase = 0.01

while True:
    if game_state == "PLAYING":
        screen.update()
        time.sleep(move_speed)
        snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        move_speed = max(0.05, move_speed - speed_increase)
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over()
        scoreboard.game_overs()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_over()
            scoreboard.game_overs()

    screen.update()


