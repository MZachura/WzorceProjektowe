from os import path
import pygame

""" TU WRZUCASZ WSZYSTKIE ZMIENNE GLOBALNE JAK NP KOLORY CZY PATH DO JAKIEGOS FOLDERU"""

SCR_SIZE = (WIDTH, HEIGHT) = (1024, 768)
TITLE = "THE TILEMAP GAME"
FPS = 60

# game folders paths
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, "maps")
IMG_FOLDER = path.join(GAME_FOLDER, "imgs")

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
TILE_SIZE = 64
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

# Obstacles
WALL_IMG = "Platform.png"

# Player
PLAYER_SPEED = 250
PLAYER_IMG_FOLDER = path.join(IMG_FOLDER, "Player")
PLAYER_IMG = "move (1).png"
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
PLAYER_ROT_SPEED = 250
# Enemies
ENEMY_IMG = "walker.png"

def collide_hit_rect(sp1, sp2):
    return sp1.hit_rect.colliderect(sp2.rect)