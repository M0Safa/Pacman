import pygame
from mazegenerator import MazeGenerator

WIDTH = 20
HEIGHT = 20
SEED = 42
mz = MazeGenerator(size=(WIDTH, HEIGHT), perfect=False, seed=SEED)
mz.generate()
for row in mz.maze:
    print(row)
pygame.init()
clock = pygame.time.Clock()


speed = 200

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pacman = pygame.image.load("assets/pacmanPack/PacMan.png").convert_alpha()
# pygame.display.set_caption("Pac-Man")

# running = True
# x = 0
# y = 8

# while running:
#     dt = clock.tick(60) / 1000
#     # 1. Events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN and speed > 0:
#                 speed -= 20
#             if event.key == pygame.K_UP:
#                 speed += 20
            

#     # 2. Update game
#     # player.move()
#     # ghosts.update()
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         x -= speed * dt

#     if keys[pygame.K_RIGHT]:
#         x += speed * dt
#     # 3. Draw
#     screen.fill((0, 0, 0))
#     #x += speed * dt
#     if x > WIDTH:
#         x -= WIDTH
#     if x < 0:
#         x += WIDTH
#     screen.blit(pacman, (x, y))

#     # 4. Display
#     pygame.display.flip()


# pygame.quit()