from vpython import sphere, vec, mag, dot
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
        self.rotation_axis = vec(0, 0, 0)
        if number in range(1, 16):
            self.ball = sphere(radius=RADIUS, pos=pos, texture={'file': 'textures/ball{}.jpg'.format(self.number)})
        else:
            self.ball = sphere(radius=RADIUS, pos=CUE_BALL_POS)

    def set_velocity(self, velocity):
        self.velocity = velocity

    def move(self, dt):
        self.ball.pos = self.ball.pos + dt * self.velocity
        self.set_velocity(self.velocity - self.velocity * 0.005)
        if mag(self.velocity) < 0.2:
            self.set_velocity(vec(0, 0, 0))

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
                self.set_velocity(vec(0, 0, 0))
                self.ball.visible = False

    def oter_balls_collision(self, rack):
        for another_ball in rack:
            if another_ball.ball.visible:
                pos_a = self.ball.pos
                pos_b = another_ball.ball.pos
                vel_a = self.velocity
                vel_b = another_ball.velocity
                radius = self.ball.radius
                if self != another_ball and mag(pos_a - pos_b) < 2 * radius:
                    a = mag(vel_a - vel_b) ** 2
                    b = dot(-2 * (pos_a - pos_b), (vel_a - vel_b))
                    c = mag(pos_a - pos_b) ** 2 - (2 * radius) ** 2
                    delta = b ** 2 - 4 * a * c
                    if a != 0 and delta > 0:
                        dtprim = (-b + sqrt(delta)) / (2 * a)
                        pos_a = pos_a - vel_a * dtprim
                        pos_b = pos_b - vel_b * dtprim
                        tmp = (dot(vel_a - vel_b, (pos_a - pos_b) / mag(pos_a - pos_b))) * (
                                    (pos_a - pos_b) / mag(pos_a - pos_b))
                        vel_a -= tmp
                        vel_b += tmp
                        pos_a += vel_a * dtprim
                        pos_b += vel_b * dtprim
                        self.ball.pos = pos_a
                        self.set_velocity(vel_a)
                        another_ball.pos = pos_b
                        another_ball.set_velocity(vel_b)


def create_rack():
    rack = []
    for row in range(len(BALL_ORDER)):
        x = RACK_POS + 2*row * RADIUS * sqrt(3)/2
        for i in range(len(BALL_ORDER[row])):
            z = -row*RADIUS + 2*i*RADIUS
            rack.append(Ball(BALL_ORDER[row][i], pos=vec(x, 0, z)))
    return rack
