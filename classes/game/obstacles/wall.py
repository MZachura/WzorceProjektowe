import pygame
from config import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        #self.image.fill(BLACK)
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

    def update(self):
        pass
