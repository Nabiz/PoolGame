from vpython import vec, curve, color
from math import pi, sin, cos


class Camera:
    def __init__(self, cue_ball_pos, scene):
        self.scene = scene
        self.camera = scene.camera
        self.cue_ball_pos = cue_ball_pos
        self.fi = pi
        self.c = curve(color=color.red, radius=5)
        self.set_aim_camera()

    def aim_camera_position(self, fi, r=200):
        x = r * cos(fi)
        z = r * sin(fi)
        return vec(x, 50, z)

    def set_aim_camera(self):
        new_pos = self.aim_camera_position(self.fi)
        self.camera.pos = self.cue_ball_pos + new_pos
        self.camera.axis = -new_pos
        self.c.clear()
        self.c.append(self.cue_ball_pos, self.cue_ball_pos - 10*vec(new_pos.x, 0, new_pos.z))

    def aim(self, angle):
        self.fi += angle
        self.camera.rotate(angle, axis=self.scene.up)
        self.set_aim_camera()

    def set_observing_camera(self):
        self.c.clear()
        self.scene.center = vec(0, 0, 0)
        self.camera.pos = vec(0, 1250, -1000)
        self.camera.axis = -self.camera.pos
