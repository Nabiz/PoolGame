from vpython import box, vec, color

LENGTH = 2000
WIDTH = 1000
POSITION = vec(0, -23.5, 0)


class Table:
    def __init__(self):
        self.board = box(pos=POSITION, size=vec(LENGTH, 0, WIDTH), color=color.green)
