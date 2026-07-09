from logic_gates import GliderLogicGates
from pygame_viewer import run_pygame_life
N = 65
CELL_SCALE = 10
def main():
    input_a = True
    input_b = True
    LogicGate = GliderLogicGates()
    life = LogicGate.setup_and_gate(N,input_a,input_b)
    run_pygame_life(life, cell_scale=CELL_SCALE, fps=18, max_frames=300, title="Game of Life - And Gate")
    print(LogicGate.run_and_gate(input_a,input_b))

if __name__ == "__main__":
	main()
    