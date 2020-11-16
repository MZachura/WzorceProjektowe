from classes.game.obstacles.wall import Wall
from classes.game.mobs.enemy import Enemy
from classes.game.mobs.player import Player
from config import *
from abc import ABCMeta, abstractclassmethod

# w sumie zbedny no ale coz
class ISprite(metaclass=ABCMeta):
    @abstractclassmethod
    def get_sprite():
        """ Interfejs do spritow"""


class SpriteFactory():
    @staticmethod
    def get_sprite(spriteType, game, x=99, y=99):
        try:
            if x == 99 and y == 99:
                x, y = game.gen_coords() 

            if spriteType == 'M':
                return Enemy(game, x, y)
            if spriteType == 'P':
                Player(game, x, y)
            raise AssertionError("Sprite type not found")

        except AssertionError as _e:
            print(_e) 

