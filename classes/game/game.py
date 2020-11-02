from classes.game.map.tilemap import Map
import pygame
from config import *
from  classes.game.map.tilemap import Map
from  classes.game.map.camera import Camera
from classes.game.mobs.player import Player
from classes.game.obstacles.wall import Wall
from classes.game.mobs.enemy import Enemy
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

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

    # tu tworzysz wszystkie obiekty np kamere 
    def set_up(self):
        self.all_sprites = pygame.sprite.Group()    # tu dodajesz wszytkie sprity
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

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

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.update()


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

    
