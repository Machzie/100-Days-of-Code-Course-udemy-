from turtle import Turtle

ALIGNMENT = "left"
FONT = "Courier"
FONTSIZE = 25
FONTTYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-100, 250)
        self.write(self.left_score, align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))
        self.setposition(100, 250)
        self.write(self.right_score, align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_wins(self):
        self.setposition(-85, 0)
        self.write("LEFT WINS!", align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))

    def right_wins(self):
        self.setposition(-90, 0)
        self.write("RIGHT WINS!", align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))
