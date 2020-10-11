from os import path

""" TU WRZUCASZ WSZYSTKIE ZMIENNE GLOBALNE JAK NP KOLORY CZY PATH DO JAKIEGOS FOLDERU"""

SCR_SIZE = (WIDTH, HEIGHT) = (1024, 768)
TITLE = "THE TILEMAP GAME"
FPS = 60

# game folders paths
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, "maps")

# Colors (pygame)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40 ,40)

BG_COLOR = DARKGREY        # jak cos pozniej bd pewnie po prosty obrazek na calosc

# Game variables
TILE_SIZE = 32
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

PLAYER_SPEED = 250


