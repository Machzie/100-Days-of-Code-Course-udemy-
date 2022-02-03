from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"
FONTSIZE = 12
FONTTYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setposition(-240, -260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(-70, 0)
        self.write(arg="GAME OVER", font=("Arial", 20, "normal"))
