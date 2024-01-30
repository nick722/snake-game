from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        # Todo: convert high_score to use number from data.txt
        # self.high_score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        with open("data.txt", "r+") as file:
            self.high_score = int(file.read())
            if self.score > self.high_score:
                # todo: write to high_score from file
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
