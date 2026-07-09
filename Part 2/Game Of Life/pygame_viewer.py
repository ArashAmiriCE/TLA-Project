# -*- coding: utf-8 -*-

import numpy as np
import pygame


def grid_to_surface(grid, cell_scale=1, alive_color=(255, 255, 255), dead_color=(0, 0, 0), viewport=None):
    cells = np.swapaxes(grid, 0, 1)

    if viewport is not None:
        row_start, row_end, col_start, col_end = viewport
        cells = cells[row_start:row_end, col_start:col_end]

    rgb = np.empty((cells.shape[0], cells.shape[1], 3), dtype=np.uint8)
    rgb[cells > 0] = alive_color
    rgb[cells == 0] = dead_color
    # for x in (12, 13):
    #     for y in (15,16):
    #         if cells[x, y] == 0:
    #             rgb[x, y] = (0,0,255)
    #         else:
    #             rgb[x,y] = (255,0,0)

    surface = pygame.surfarray.make_surface(rgb)
    if cell_scale != 1:
        surface = pygame.transform.scale(
            surface,
            (surface.get_width() * cell_scale, surface.get_height() * cell_scale),
        )
    return surface


def run_pygame_life(life, cell_scale=1, fps=20, viewport=None, max_frames=None, title="Game of Life"):
    """Render a Game of Life simulation in a pygame window."""
    pygame.init()
    cells = life.getStates()
    surface = grid_to_surface(cells, cell_scale=cell_scale, viewport=viewport)
    screen = pygame.display.set_mode(surface.get_size())
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    finished = False
    frame = 0
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        screen.blit(surface, (0, 0))
        pygame.display.flip()

        life.evolve()
        cells = life.getStates()
        # if cells[15:17, 12:14].sum() == 4:
        #     finished = True
        # if cells[2:4 , 0:2].sum() > 0:
        #     finished = True
        surface = grid_to_surface(cells, cell_scale=cell_scale, viewport=viewport)

        frame += 1
        if max_frames is not None and frame >= max_frames:
            finished = True

        clock.tick(fps)
    # print(frame)
    pygame.quit()