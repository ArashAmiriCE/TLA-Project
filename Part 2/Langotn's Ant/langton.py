import numpy as np

class LangtonsAnt:
    def __init__(self, N, ant_position=(0,0), rules={0: (1, 'R'), 1: (0, 'L')}):
        self.N = N
        self.grid = np.zeros((N, N), np.uint)
        self.r = ant_position[0]
        self.c = ant_position[1]
        self.direction = "U"
        self.rules = rules

    def get_states(self):
        return self.grid

    def get_current_position(self):
        return (self.r, self.c)

    def step(self):
        current_color = self.grid[self.r, self.c]
        self.grid[self.r, self.c] = self.rules[current_color][0]
        if self.rules[current_color][1] == 'R':
            match self.direction:
                case 'R':
                    self.direction = 'D'
                    self.r = (self.r + 1) % self.N
                case 'L':
                    self.direction = 'U'
                    self.r = (self.r - 1) % self.N
                case 'U':
                    self.direction = 'R'
                    self.c = (self.c + 1) % self.N
                case 'D':
                    self.direction = 'L'
                    self.c = (self.c - 1) % self.N
        elif self.rules[current_color][1] == 'L':
            match self.direction:
                case 'R':
                    self.direction = 'U'
                    self.r = (self.r - 1) % self.N
                case 'L':
                    self.direction = 'D'
                    self.r = (self.r + 1) % self.N
                case 'U':
                    self.direction = 'L'
                    self.c = (self.c - 1) % self.N
                case 'D':
                    self.direction = 'R'
                    self.c = (self.c + 1) % self.N

    def update(self):
        self.step()
