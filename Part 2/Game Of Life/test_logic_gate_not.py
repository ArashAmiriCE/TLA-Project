from logic_gates import GliderLogicGates
from pygame_viewer import run_pygame_life
N = 65
CELL_SCALE = 10
def main():
    input_a = True
    LogicGate = GliderLogicGates()
    life = LogicGate.setup_not_gate(N,input_a)
    run_pygame_life(life, cell_scale=CELL_SCALE, fps=50, max_frames=300, title="Game of Life - Not Gate")
    print(LogicGate.run_not_gate(input_a))

if __name__ == "__main__":
	main()
    