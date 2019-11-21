import vpython
from math import pi, cos, sin

def biegunowe_na_kartezjanskie(fi, r=10):
    x = r * cos(fi)
    z = r * sin(fi)
    return vpython.vector(x, 10, z)

radius = 1
white_ball = vpython.sphere(pos=vpython.vector(0, 0, 0), radius=radius, texture={'file': 'ball.jpg'})
plane = vpython.box(pos=vpython.vector(0, -1.5, 0), length=100, height=1, width=100, texture={'file': 'ground.jpg'})
fi = 0
c = vpython.curve(radius=0.1)

while True:
    vpython.rate(100)
    k = vpython.keysdown()
    if 'left' in k:
        white_ball.pos = white_ball.pos + vpython.vector(-0.1, 0, 0)
        white_ball.rotate(-0.1*pi, vpython.vector(1, 0, 0))
    if 'right' in k:
        white_ball.pos = white_ball.pos + vpython.vector(0.1, 0, 0)
        white_ball.rotate(0.1*pi, vpython.vector(1, 0, 0))
    if 'up' in k:
        white_ball.pos = white_ball.pos + vpython.vector(0, 0.1, 0)
        white_ball.rotate(0.1 * pi, vpython.vector(0, 1, 0))
    if 'down' in k:
        white_ball.pos = white_ball.pos + vpython.vector(0, -0.1, 0)
        white_ball.rotate(-0.1 * pi, vpython.vector(0, 1, 0))
    if 'x' in k:
        fi = fi + 0.005*pi
        vpython.scene.camera.pos = biegunowe_na_kartezjanskie(fi)
        vpython.scene.camera.axis = -biegunowe_na_kartezjanskie(fi)
        vpython.scene.camera.rotate(0.005*pi, axis=vpython.scene.up)
        c.clear()
        c.append(white_ball.pos, 2*(white_ball.pos + vpython.vector(vpython.scene.camera.axis.x, 0, vpython.scene.camera.axis.z)))

    if 'z' in k:
        fi = fi - 0.005*pi
        vpython.scene.camera.pos = biegunowe_na_kartezjanskie(fi)
        vpython.scene.camera.axis = -biegunowe_na_kartezjanskie(fi)
        vpython.scene.camera.rotate(-0.005*pi, axis=vpython.scene.up)
        c.clear()
        c.append(white_ball.pos, 2*(white_ball.pos + vpython.vector(vpython.scene.camera.axis.x, 0, vpython.scene.camera.axis.z)))
