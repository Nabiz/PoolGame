from vpython import vec, keysdown, rate, mag, dot
from ball import Ball, create_rack
from table import Table
from camera import Camera
from math import pi, sqrt

# Creating objects
table = Table()
cue_ball = Ball(number=0)
rack = create_rack()
camera = Camera(cue_ball.ball.pos)

rack.append(cue_ball)

# Game loop
power = 4
dt = 0.1
while True:
    rate(100)
    k = keysdown()
    if 'left' in k:
        camera.aim(-0.001*pi)
    if 'right' in k:
        camera.aim(0.001*pi)
    if 'x' in k:
        cue_ball.set_velocity(power * vec(camera.camera.axis.x, 0, camera.camera.axis.z))
    for ball in rack:
        ball.table_collision(table)
        for another_ball in rack:
            pos_a = ball.ball.pos
            pos_b = another_ball.ball.pos
            vel_a = ball.velocity
            vel_b = another_ball.velocity
            radius = ball.ball.radius
            if ball != another_ball and mag(pos_a-pos_b)<2*radius:
                a = mag(vel_a-vel_b) ** 2
                b = dot(-2*(pos_a-pos_b), (vel_a-vel_b))
                c = mag(pos_a-pos_b) ** 2-(2*radius)**2
                delta = b ** 2 - 4*a*c
                if a != 0 and delta > 0:
                    dtprim = (-b + sqrt(delta)) / (2*a)
                    pos_a = pos_a - vel_a * dtprim
                    pos_b = pos_b - vel_b * dtprim
                    tmp = (dot(vel_a-vel_b,(pos_a-pos_b)/mag(pos_a-pos_b)))*((pos_a-pos_b)/mag(pos_a-pos_b))
                    vel_a -= tmp
                    vel_b += tmp
                    pos_a += vel_a * dtprim
                    pos_b += vel_b * dtprim
                    ball.ball.pos, ball.velocity = pos_a, vel_a
                    another_ball.pos, another_ball.velocity = pos_b, vel_b
        ball.move(dt)
