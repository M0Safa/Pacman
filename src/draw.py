import pygame

def draw_maze (maze_surface, maze,
               cell_size,
               offset_x,
               offset_y):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            x = offset_x + col * cell_size
            y = offset_y + row * cell_size
            walls = maze[row][col]
            if walls & 1:
                #North
                pygame.draw.line(
                    maze_surface,
                    (0, 80, 255),
                    (x, y),
                    (x + cell_size, y),
                    3
                )
            if walls & 2:
                #East
                pygame.draw.line(
                    maze_surface,
                    (0, 80, 255),
                    (x + cell_size, y),
                    (x + cell_size, y + cell_size),
                    3
                )
            if walls & 4:
                #South
                pygame.draw.line(
                    maze_surface,
                    (0, 80, 255),
                    (x, y + cell_size),
                    (x + cell_size, y + cell_size),
                    3
                )
            if walls & 8:
                #West
                pygame.draw.line(
                    maze_surface,
                    (0, 80, 255),
                    (x, y),
                    (x, y + cell_size),
                    3
                )