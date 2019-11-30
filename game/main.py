from vpython import vec, keysdown, rate, mag, dot
from ball import Ball, create_rack, CUE_BALL_POS
from table import Table
from camera import Camera
from math import pi, sqrt

# Creating objects
table = Table()
cue_ball = Ball(number=0)
rack = create_rack()
camera = Camera(cue_ball.ball.pos)

rack.append(cue_ball)

mode = "aim"
# Game loop
power = 0.2
dt = 0.1
while True:
    rate(100)
    k = keysdown()
    if 'left' in k:
        if 'z' in k:
            camera.aim(-0.001*pi)
        else:
            camera.aim(-0.005*pi)
    if 'right' in k:
        if 'z' in k:
            camera.aim(0.001*pi)
        else:
            camera.aim(0.005*pi)
    if 'x' in k and mode == 'aim':
        cue_ball.set_velocity(power * vec(camera.camera.axis.x, 0, camera.camera.axis.z))
        camera.set_observing_camera()
        mode = 'observe'
    for ball in rack:
        if ball.ball.visible:
            ball.pocket_collision(table.pockets)
            ball.table_collision(table)
            ball.oter_balls_collision(rack)
            ball.move(dt)
    for ball in rack:
        if ball.velocity != vec(0, 0, 0):
            break
    else:
        can_aim = True
        if mode == "observe":
            if cue_ball.ball.visible is False:
                cue_ball.ball.pos = CUE_BALL_POS
                cue_ball.ball.visible = True
            camera.set_aim_camera()
            mode = "aim"
