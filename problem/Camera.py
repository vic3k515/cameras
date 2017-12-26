import random

class Camera:
    def __init__(self, problem, pos):
        self.problem = problem
        self.x = float(pos[0])
        self.y = float(pos[1])

    def __eq__(self, other):
        if self.problem == other.problem \
                and self.x == other.x and self.y == other.y:
            return True
        return False

    def move(self, newPos = None):
        if newPos:
            self.x = float(newPos[0])
            self.y = float(newPos[1])
        else:
            self.x += random.choice([-1, 0, 1])
            self.y += random.choice([-1, 0, 1])