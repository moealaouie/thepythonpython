from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear any text from the scoreboard
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_overs(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)  # Adjust the y-coordinate as needed based on your font size
        self.write('Press "r" to reset or Esc to exit', align="center", font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0  # Reset the score to 0
        self.update_scoreboard()  # Redraw the scoreboard with the reset score

    def draw_border(self):
        border = Turtle()
        border.penup()
        border.color("white")
        border.goto(-300, -300)  # Go to the starting corner
        border.pendown()
        border.speed("fastest")  # Draw the border as fast as possible
        for _ in range(4):
            border.forward(600)  # Draw each side of the square
            border.left(90)
        border.hideturtle()  # Hide the turtle after drawing