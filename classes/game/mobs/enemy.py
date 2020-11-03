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
        
        # zwykly rect sie zmienia a ten zapobiega dziwnym przeskokom 
        self.hit_rect = ENEMY_HIT_RECT.copy()   # tych bd duzo
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILE_SIZE
        self.rect.center = self.pos

        self.rot = 0
        #zamiast xv yv i x, y
        self.vel = vec(0, 0)
        self.acc =vec(0, 0)

        self.health = ENEMY_HEALTH

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pygame.transform.rotate(self.game.enemy_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(ENEMY_SPEED, 0).rotate(-self.rot) # jak dasz wieksza wartosc to jest smiesznie XD
        
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt 
        self.pos += self.vel * self.game.dt + .5 * self.acc * self.game.dt **2 
        
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        # umieraja gdy nie maja hp
        if self.health <= 0:
            self.kill()
            self.game.generate_new_enemy()
            self.game.score += 1
    
    # rysuje bar nad glowami
    def draw_health(self):
        if self.health > 40:
            col = GREEN
        else:
            col = RED
        bar_width = int(self.rect.width * self.health / ENEMY_HEALTH)
        self.health_bar = pygame.Rect(0, 0, bar_width, 7)
        if self.health < ENEMY_HEALTH:
            pygame.draw.rect(self.image, col, self.health_bar)
