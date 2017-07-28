import pygame
from player import Player
class enemy(pygame.sprite.Sprite):
    def __init__(self, color,width,height,health):
            # Define some colors
            self.width= width
            self.height=height
            self.speed= 8 #speed is relative to players size
            self.gravity=False
            self.health = health
            super(enemy,self).__init__()


            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(color)


            # Fetch the rectangle object that has the dimensions of the image
            # image.
            # Update the position of this object by setting the values
            # of rect.x and rect.y
            self.rect = self.image.get_rect()
    def attack(self,player):

        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        elif self.rect.x < player.rect.x:
            self.rect.x += self.speed
        # Movement along y direction
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed
