from turtle import Turtle, Screen
from pickle import dump, load
import sound_effect

ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.high_score_players = []
        super().__init__()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.update()
        self.update_score()

    def update(self):
        self.hideturtle()
        self.clear()
        self.write(f'Your score: {self.score}              High score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        pos = 170
        sound_effect.game_over()
        self.update_score()
        self.goto(0, -280)
        self.update()
        self.goto(0, 250)
        self.write(f'GAME OVER', move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, 200)
        self.write(f'TOP PLAYERS', move=False, align=ALIGNMENT, font=FONT)
        for player in self.high_score_players:
            if not pos < -280:
                self.goto(0, pos)
                self.write(f'Player: {player[0]} | Score: {player[1]}', move=False, align=ALIGNMENT, font=('Times New Roman', 16, 'normal'))
                pos -= 30

    def update_score(self):
        try:
            with open("data.dat", "rb") as cache:
                data_load = load(cache)
                self.high_score = data_load[0]
                self.high_score_players = data_load[1]
        except:
            with open("data.dat", "wb") as cache:
                pass

        if self.score > self.high_score:
            player_name = Screen().textinput(title='NEW RECORD', prompt='Type your name')
            self.high_score = self.score
            self.high_score_players.append((player_name, self.score))
            self.high_score_players = sorted(self.high_score_players, key=lambda score: score[1], reverse=True)
            with open("data.dat", "wb") as cache:
                dump((self.score, self.high_score_players), cache)
