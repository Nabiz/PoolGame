from vpython import box, vec, color, cylinder, shapes

LENGTH = 2000
WIDTH = 1000
WALL_WIDTH = 50
HOLE_RADIUS = 37
POSITION = vec(0, -23.5, 0)


class Table:
    def __init__(self):
        self.board = box(pos=POSITION, size=vec(LENGTH, 0, WIDTH), color=color.green)
        self.create_walls()
        self.pockets = self.create_pockets()

    def create_walls(self):
        brown = vec(0.55, 0.27, 0.07)
        wall_right = box(pos=vec(0, 0, (WIDTH + WALL_WIDTH)/2), size=vec(LENGTH, WALL_WIDTH, WALL_WIDTH), color=brown)
        wall_left = box(pos=vec(0, 0, -(WIDTH + WALL_WIDTH)/2), size=vec(LENGTH, WALL_WIDTH, WALL_WIDTH), color=brown)
        wall_up = box(pos=vec((LENGTH + WALL_WIDTH)/2, 0, 0),
                      size=vec(WALL_WIDTH, WALL_WIDTH, WIDTH+2*WALL_WIDTH), color=brown)
        wall_down = box(pos=vec(-(LENGTH + WALL_WIDTH)/2, 0, 0),
                        size=vec(WALL_WIDTH, WALL_WIDTH, WIDTH+2*WALL_WIDTH), color=brown)

    def create_pockets(self):
        pocket1 = cylinder(pos=vec(0, -WALL_WIDTH/2.1, -WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS, color=color.black)
        pocket2 = cylinder(pos=vec(0, -WALL_WIDTH/2.1, WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS, color=color.black)
        pocket3 = cylinder(pos=vec(-LENGTH/2, -WALL_WIDTH/2.1, -WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS,
                           color=color.black)
        pocket4 = cylinder(pos=vec(LENGTH/2, -WALL_WIDTH/2.1, -WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS,
                           color=color.black)
        pocket5 = cylinder(pos=vec(-LENGTH/2, -WALL_WIDTH/2.1, WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS,
                           color=color.black)
        pocket6 = cylinder(pos=vec(LENGTH/2, -WALL_WIDTH/2.1, WIDTH/2), axis=vec(0, WALL_WIDTH, 0), radius=HOLE_RADIUS, color=color.black)
        return [pocket1, pocket2, pocket3, pocket4, pocket5, pocket6]
