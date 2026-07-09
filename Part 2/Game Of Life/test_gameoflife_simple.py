import conway
from pygame_viewer import run_pygame_life

N = 64
CELL_SCALE = 10


def main():
	life = conway.GameOfLife(N, fastMode=True, finite=True)
	# life.insertBlinker((0,0))
	#life.insertGlider((0,0))       
	#life.insertGliderGun((0,0))    
	#life.insertFromFile("./Test Files/dragon spaceship.cells", (0,30))
	#life.insertFromFile("./Test Files/ak94 gun.cells", (0,0))
	#life.insertFromFile("./Test Files/vacuumgun gun.cells", (0,0))
	#life.insertFromFile("./Test Files/stargate oscillator.cells", (0,0))
	#life.insertFromFile("./Test Files/7enginecordership spaceship.cells", (0,0))
	life.insertFromFile("./Test Files/3enginecordership gun 279x258.cells", (0,0))
	#life.insertFromFile("./Test Files/glider in rle.rle", (0,0))

	run_pygame_life(life, cell_scale=CELL_SCALE, fps=200, max_frames=300, title="Game of Life - Glider Check")


if __name__ == "__main__":
	main()
