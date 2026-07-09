import numpy as np
from conway import GameOfLife


class GliderLogicGates:

    def __init__(self):
        pass

    def setup_and_gate(self, grid_size=65, input_a_present=False, input_b_present=False):
        life = GameOfLife(grid_size, finite=True, fastMode=True)
        if input_a_present:
            life.insertGliderGunSouthWest((2,4))
        if input_b_present:
            life.insertGliderGunNorthhWest((25,9))
        return life

    def setup_not_gate(self, grid_size=65, input_a_present=False):
        life = GameOfLife(grid_size,finite=True, fastMode=True)
        if input_a_present:
            life.insertGliderGunSouthWest((10,16))
        life.insertGliderGunNorthhWest((31,15))
        return life

    def run_and_gate(self, input_a_present, input_b_present):
        life = self.setup_and_gate(input_a_present=input_a_present, input_b_present=input_b_present)
        for _ in range(60):
            life.evolve()
        if life.getGrid()[15:17, 12:14].sum() == 4:
            return True
        else:
            return False

    def run_not_gate(self, input_a_present):
        life = self.setup_not_gate(input_a_present=input_a_present)
        for _ in range(129):
            life.evolve()
        if life.getGrid()[2:4 , 0:2].sum() > 0:
            return True
        else:
            return False
