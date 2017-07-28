"""
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
from block import Block
import keyboard

class Player(Block):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height, health,exp):
        #Block.__init__(self, color, width, height)
         super(self.__class__, self,).__init__(color, width,height)
         self.move_ticker = 0
         self.gravity=True
         self.exp = 0
         self.change_x = 0
         self.change_y = 0
         self.health = health

    def moveleft(self,screen_width):
        self.rect.x = self.rect.x - 1

    def jump(self,screen_height):
        self.rect.y = self.rect.y - 30
    def collision(self,spritegroup):
        pygame.sprite.spritecollide(self,spritegroup, False)

    def moveright(self,screen_width):
        self.rect.x= self.rect.x + 1



    def flush(self):
        self.change_x=0
