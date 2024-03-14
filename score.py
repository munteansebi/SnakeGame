from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=250)
        self.update()

    def update(self):
        self.write(f"Score : {self.score}", font=("Verdana", 24, "bold"), align="center")

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Verdana", 24, "bold"), align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()