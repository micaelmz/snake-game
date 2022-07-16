from turtle import Turtle
import sound_effect

ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        sound_effect.game_over()
        self.goto(0, 40)
        self.update()
        self.goto(0, 0)
        self.write(f'GAME OVER', move=False, align=ALIGNMENT, font=FONT)

