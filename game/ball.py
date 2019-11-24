from vpython import sphere, vec, mag
from math import sqrt

RADIUS = 23.5
CUE_BALL_POS = vec(-600, 0, 0)
BALL_ORDER = [[1], [10, 3], [6, 8, 13], [9, 4, 15, 2], [14, 11, 5, 12, 7]]
RACK_POS = 400
HOLE_RADIUS = 37

class Ball:
    def __init__(self, number, pos=vec(0, 0, 0)):
        self.number = number
        self.velocity = vec(0, 0, 0)
        if number in range(1, 16):
            self.ball = sphere(radius=RADIUS, pos=pos, texture={'file': 'textures/ball{}.jpg'.format(self.number)})
        else:
            self.ball = sphere(radius=RADIUS, pos=CUE_BALL_POS)

    def set_velocity(self, velocity):
        self.velocity = velocity

    def move(self, dt):
        self.ball.pos = self.ball.pos + dt * self.velocity
        self.velocity -= self.velocity * 0.005
        if mag(self.velocity) < 0.2:
            self.velocity = vec(0, 0, 0)

    def table_collision(self, table):
        if self.ball.pos.x - self.ball.radius < -table.board.length/2 \
                or table.board.length/2 < self.ball.pos.x + self.ball.radius:
            self.set_velocity(vec(-self.velocity.x, 0, self.velocity.z))
        if self.ball.pos.z - self.ball.radius < -table.board.width/2 \
                or table.board.width/2 < self.ball.pos.z + self.ball.radius:
            self.set_velocity(vec(self.velocity.x, 0, -self.velocity.z))

    def pocket_collision(self, pockets):
        for pocket in pockets:
            if mag(self.ball.pos - pocket.pos) < HOLE_RADIUS+RADIUS:
                self.velocity = vec(0, 0, 0)
                self.ball.visible = False


def create_rack():
    rack = []
    for row in range(len(BALL_ORDER)):
        x = RACK_POS + 2*row * RADIUS * sqrt(3)/2
        for i in range(len(BALL_ORDER[row])):
            z = -row*RADIUS + 2*i*RADIUS
            rack.append(Ball(BALL_ORDER[row][i], pos=vec(x, 0, z)))
    return rack
