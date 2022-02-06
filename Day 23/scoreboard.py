from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-240, 270)
        self.write(f"Level: {self.score + 1}", align='center', font=(FONT))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER.", align='center', font=("Courier", 20, "normal"))
