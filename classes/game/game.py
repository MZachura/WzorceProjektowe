import pygame
import random
from config import *
from classes.game.map.tilemap import Map
from classes.game.map.camera import Camera
from classes.game.mobs.player import Player
from classes.game.obstacles.wall import Wall
from classes.game.mobs.enemy import Enemy
from classes.db.database import Database


vec = pygame.math.Vector2

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.level = 1
        self.score = 0
        self.how_many_to_spawn = 0
        
        # db
        self.player_name = "Pan Janusz"
        self.db = Database()

    """FUNKCJE GLOWNE"""
    # tworzy obiekt Map ktory zczytuje tilemape
    def load_data(self):
        self.map = Map(path.join(MAP_FOLDER, "map.txt"))
        self.player_img = pygame.image.load(path.join(PLAYER_IMG_FOLDER, PLAYER_IMG)).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (TILE_SIZE, TILE_SIZE))

        self.wall_img = pygame.image.load(path.join(IMG_FOLDER, WALL_IMG)).convert_alpha()
        self.wall_img = pygame.transform.scale(self.wall_img, (TILE_SIZE, TILE_SIZE))

        self.enemy_img = pygame.image.load(path.join(IMG_FOLDER, ENEMY_IMG)).convert_alpha()
        self.enemy_img = pygame.transform.scale(self.enemy_img, (TILE_SIZE, TILE_SIZE))

        self.bullet_img = pygame.image.load(path.join(IMG_FOLDER, BULLET_IMG)).convert_alpha()

    # tu tworzysz wszystkie obiekty np kamere 
    def set_up(self):
        self.all_sprites = pygame.sprite.Group()    # tu dodajesz wszytkie sprity
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)

        self.camera = Camera(self.map.width, self.map.height)

    # do wywalania w main albo w menu jak sie klikanie przycisk
    def mainloop(self):
        self.run = True # jak false wylaczasz gre
        while self.run:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # wszystkie jakies przyciski 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    # update pozycji spritow itp
    def update(self):
        self.all_sprites.update()       # to wywoluje metode update u kazdego kto jest dodany do tej grupy
        self.camera.update(self.player)
        
        # czy zombie dotknely gracza O.O
        hits = pygame.sprite.spritecollide(self.player, self.enemies, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= ENEMY_DMG
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.add_score_to_db()
                self.run = False
        if hits:
            self.player.pos += vec(KNOCK_BACK, 0).rotate(-hits[0].rot)

        # czy pociski trafily Enemy
        hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DMG  
            hit.vel = vec(0, 0)

        

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Enemy):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        score_lbl = f"SCORE: {self.score}"
        draw_score(self.screen, score_lbl)
        pygame.display.update()

    def gen_coords(self):
        find_coords = True
        while (find_coords):
            cordx = random.randint(1, GRID_WIDTH - 1) #* TILE_SIZE
            cordy = random.randint(1, GRID_HEIGHT - 1) #* TILE_SIZE

            if self.player.pos.x != cordx and self.player.pos.y != cordy:
                find_coords = False # znalazlo i nie koliduje z playerm
        return cordx, cordy
    '''
    def generate_new_enemy(self):
        while (len(self.enemies) < ENEMY_SPAWN_NO * self.level):
            x, y = self.gen_coords()
            Enemy(self, x, y)
    '''

    def generate_new_enemy(self):
        x, y = self.gen_coords()
        Enemy(self, x, y)            

    def add_score_to_db(self):
        self.db.add_score(self.player_name, self.score)


    """FUNKCJE POMOCNICZE"""
    # bedzie mozna  pozniej usunac
    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):            
                pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    # tu dajesz wszystkie symbole co oanczaja na tilemapie
    def what_to_create(self, tile, row, col):
        if tile == 'P':
            self.player = Player(self, col, row)

        elif tile == '1':
            Wall(self, col, row)

        elif tile == "M":
            Enemy(self, col, row)
            

    def quit(self):
        self.run = False
        pygame.quit()

    
