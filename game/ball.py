from vpython import sphere, vec
from math import sqrt

RADIUS = 23.5
CUE_BALL_POS = vec(-600, 0, 0)
BALL_ORDER = [[1], [10, 3], [6, 8, 13], [9, 4, 15, 2], [14, 11, 5, 12, 7]]
RACK_POS = 400

class Ball:
    def __init__(self, number, pos=vec(0, 0, 0)):
        self.number = number
        if number in range(1, 16):
            self.ball = sphere(radius=RADIUS, pos=pos, texture={'file': 'textures/ball{}.jpg'.format(self.number)})
        else:
            self.ball = sphere(radius=RADIUS, pos=CUE_BALL_POS)


def create_rack():
    rack = []
    for row in range(len(BALL_ORDER)):
        x = RACK_POS + 2*row * RADIUS * sqrt(3)/2
        for i in range(len(BALL_ORDER[row])):
            z = -row*RADIUS + 2*i*RADIUS
            rack.append(Ball(BALL_ORDER[row][i], pos=vec(x, 0, z)))
    return rack
