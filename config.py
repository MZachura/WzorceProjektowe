from os import path
import pygame
pygame.font.init()
score_font = pygame.font.SysFont('comicsans', 20)

""" TU WRZUCASZ WSZYSTKIE ZMIENNE GLOBALNE JAK NP KOLORY CZY PATH DO JAKIEGOS FOLDERU"""

SCR_SIZE = (WIDTH, HEIGHT) = (1024, 768)
TITLE = "Zombie Rush"
FPS = 60

ENEMY_SPAWN_NO = 5

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
TILE_SIZE = 32
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

# Obstacles
WALL_IMG = "Platform.png"

# Player
PLAYER_HEALTH =100
PLAYER_SPEED = 250
PLAYER_IMG_FOLDER = path.join(IMG_FOLDER, "Player")
PLAYER_IMG = "move (1).png"
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
PLAYER_ROT_SPEED = 250

# Enemies
ENEMY_IMG = "walker.png"
ENEMY_SPEED = 100
ENEMY_HIT_RECT = pygame.Rect(0, 0, 50 ,50)
ENEMY_HEALTH = 100
ENEMY_DMG = 10
KNOCK_BACK = 20
ENEMY_SPAWN_NO = 4
# Pif Paf Stuff
BULLET_IMG = "bullet.png"
BULLET_SPEED = 500
BULLET_LIFE_TIME = 1000 # mozna tez tym sposobem zrobic mele attack
SHOOT_RATE = 100 
BULLET_DMG = 20



# Funkcje wspolne dla wszystkich spritow pewnie bd mozna je jakos we wzorcach powstawiac
def collide_hit_rect(sp1, sp2):
    return sp1.hit_rect.colliderect(sp2.rect)

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

# health bar w lewym gornym rogu
def draw_player_health(screen, x, y, percent_to_fill):
    if percent_to_fill < 0:
        percent_to_fill = 0

    bar_lenght = 100
    bar_height = 20
    fill = percent_to_fill * bar_lenght
    outline = pygame.Rect(x, y, bar_lenght, bar_height )
    fill_rect = pygame.Rect(x, y, fill , bar_height)
    if percent_to_fill > .5:
        col = GREEN
    else:
        col = RED
    pygame.draw.rect(screen, col, fill_rect)
    pygame.draw.rect(screen, BLACK, outline, 2)

def draw_score(screen, text):
    label = score_font.render(text, 1, WHITE, RED)
    screen.blit(label, (int(WIDTH - label.get_width()), 20))

    
