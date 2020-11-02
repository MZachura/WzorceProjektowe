import pygame
from config import *
vec = pygame.math.Vector2

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self.groups = game.all_sprites, game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos) # jakby tego cev() nie bylo to by gracz  niezle przyspieszal XD
        self.game = game
        self.rect.center = pos
        self.vel = dir * BULLET_SPEED
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        # jelsi walnie w sciane to znika
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        # albo zasieg przekroczy
        if pygame.time.get_ticks() - self.spawn_time > BULLET_LIFE_TIME:
            self.kill()

