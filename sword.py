import pygame

class sword(pygame.sprite.Sprite) :
    def __init__(self, color,damage):
        super(sword,self).__init__()
        self.damage = damage
        self.image = pygame.Surface([20, 5])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def attack(self, player):
        self.rect.y = player.rect.y + 5
        self.rect.x = player.rect.x
