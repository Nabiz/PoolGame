from vpython import vec, keysdown, rate, canvas
from ball import Ball, create_rack
from table import Table
from camera import Camera
from math import pi

canvas.width, canvas.height = (800, 600)

table = Table()
cue_ball = Ball(number=0)
camera = Camera(cue_ball.ball.pos)
rack = create_rack()

move = False
while True:
    rate(100)
    k = keysdown()
    if 'left' in k:
        camera.aim(-0.001*pi)
    if 'right' in k:
        camera.aim(0.001*pi)
    if 'x' in k:
        move = True
    if move:
        cue_ball.ball.pos += 0.002*vec(camera.camera.axis.x, 0, camera.camera.axis.z)
