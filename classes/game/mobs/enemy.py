import pygame
from config import *
vec = pygame.math.Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.enemy_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILE_SIZE
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pygame.transform.rotate(self.game.enemy_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
