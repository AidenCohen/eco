import pygame
import keyboard
from block import Block
import time


class character(Block):
    def __init__(self, color, width, height):
        super(self.__class__, self,).__init__(color, width,height)
        size=width, height=1400, 800
        self.screen=pygame.display.set_mode(size)
