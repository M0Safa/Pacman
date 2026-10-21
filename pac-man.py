import pygame
from mazegenerator import MazeGenerator
from src.config import load_config
from src.draw import draw_maze

WIDTH = 800
HEIGHT = 800
SEED = 42
conf = load_config("config.json")
lev = conf["levels"]
lev_1 = lev[0]
w = lev_1["width"]
h = lev_1["height"]
mz = MazeGenerator(size=(lev_1["width"], lev_1["height"]), perfect=False, seed=conf["seed"])
mz.generate()
for row in mz.maze:
    print(row)
pygame.init()
clock = pygame.time.Clock()


speed = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
maze_surface = pygame.Surface((WIDTH, HEIGHT))
maze_surface.fill((0, 0, 0))
pacman = pygame.image.load("assets/pacmanPack/PacMan.png").convert_alpha()
pygame.display.set_caption("Pac-Man")

running = True
x = 0
y = 8

space = 30
hud_height = 80

available_height = HEIGHT - (2 * space) - hud_height
available_Width = WIDTH - (2 * space)
cell_size = min(
    available_Width // w,
    available_height // h
)

offset_x = space
offset_y = hud_height + space

draw_maze(maze_surface, mz.maze, cell_size, offset_x, offset_y)
        
while running:
    dt = clock.tick(60) / 1000
    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(maze_surface, (0, 0))

    # 4. Display
    pygame.display.flip()


pygame.quit()