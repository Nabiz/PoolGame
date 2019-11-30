from vpython import vec, keysdown, rate, canvas, color
from ball import Ball, create_rack, CUE_BALL_POS
from table import Table
from camera import Camera
from math import pi, sqrt
from info import Info

# Creating objects
scene = canvas(width=1000, height=600, background=color.cyan)
info = Info(scene)
table = Table()
cue_ball = Ball(number=0)
rack = create_rack()
camera = Camera(cue_ball.ball.pos, scene)

rack.append(cue_ball)

mode = "aim"
# Game loop
power = 1
info.get_info(power)
turn = 1
dt = 0.1
while True:
    rate(60)
    k = keysdown()
    if '1' in k:
        power = 0.2
        info.get_info(power)
    if '2' in k:
        power = 0.4
        info.get_info(power)
    if '3' in k:
        power = 0.6
        info.get_info(power)
    if '4' in k:
        power = 0.8
        info.get_info(power)
    if '5' in k:
        power = 1
        info.get_info(power)
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
            ball.pocket_collision(table.pockets, info)
            ball.table_collision(table)
            ball.other_balls_collision(rack)
            ball.move(dt)
    if mode == 'observe':
        for ball in rack:
            if ball.velocity != vec(0, 0, 0):
                break
        else:
            info.change_turn(power)
            can_aim = True
            if mode == "observe":
                if cue_ball.ball.visible is False:
                    cue_ball.ball.pos = CUE_BALL_POS
                    cue_ball.ball.visible = True
                camera.set_aim_camera()
                mode = "aim"
