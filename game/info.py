PLAYER1 = 'PLAYER 1'
PLAYER2 = 'PLAYER 2'


class Info:
    def __init__(self, scene):
        self.scene = scene
        self.info = "Turn: {}, Ball Type: {}, Power: {}, Scored: {}"
        self.instruction = "Z (hold) - precision mode, 1-5 - set power, X - shot"
        self.turn = PLAYER1
        self.p1_type = 'open'
        self.p2_type = 'open'
        self.scored = {'solid': [], 'striped': []}
        self.is_change = True

    def get_info(self, power):
        ball_type = self.p1_type if self.turn == PLAYER1 else self.p2_type
        self.scene.title = self.info.format(self.turn, ball_type, power, self.scored) + "\n" + self.instruction

    def score(self, ball):
        ball_type = self.p1_type if self.turn == PLAYER1 else self.p2_type
        if 0 < ball.number < 8:
            self.scored['solid'].append(ball.number)
            if self.p1_type == 'open':
                self._change_ball_type('solid', 'striped')
            if ball_type in ('solid', 'open'):
                self.is_change = False
            if len(self.scored['solid']) == 7:
                if self.turn == PLAYER1:
                    self.p1_type = '8'
                else:
                    self.p2_type = '8'
        elif ball.number > 8:
            self.scored['striped'].append(ball.number)
            if self.p1_type == 'open':
                self._change_ball_type('striped', 'solid')
            if ball_type in ('striped', 'open'):
                self.is_change = False
                if len(self.scored['striped']) == 7:
                    if self.turn == PLAYER1:
                        self.p1_type = '8'
                    else:
                        self.p2_type = '8'
        elif ball.number == 8:
            self.turn = 'GAME OVER'
            self.is_change = False

    def _change_ball_type(self, ball_type, enemy_ball_type):
        if self.turn == PLAYER1:
            self.p1_type = ball_type
            self.p2_type = enemy_ball_type
        else:
            self.p1_type = enemy_ball_type
            self.p2_type = ball_type

    def change_turn(self, power):
        if self.is_change:
            self.turn = PLAYER2 if self.turn == PLAYER1 else PLAYER1
        else:
            self.is_change = True
        self.get_info(power)
