from WzorceProjektowe.config import TILE_SIZE
import pygame
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

        self.vx, self.vy = 0, 0

    def update(self):
        self.whre_to_move()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        

    def collide_with_walls(self):
         # Horizontal
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False) # false zeby nie usuwalo
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        
        # Vertical
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False) # false zeby nie usuwalo
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def where_to_move(self):
        """TO DO:
        jakas funkcja zeby sobie chodzili 
        """
        pass