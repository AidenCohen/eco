import pygame
import time
class menu:
    def __init__(self):
        size=width, height=1400, 800
        self.screen=pygame.display.set_mode(size)
    def button(self):
        pygame.draw.rect(self.screen,(255,0,0), (10,180,430,100), 0)
    def drawtext(self,text,x,y):
        myfont = pygame.font.SysFont("monospace", 60)
        label = myfont.render(text, 1, (255,255,255))
        return self.screen.blit(label,(x,y))

    def run(self):
        pygame.init()
        speed=[1,1]
        color=244,244,244
        pygame.mixer.init()
        sound = pygame.mixer.music.load("promise.mp3")
        rectangle = pygame.Rect(10,180,430,100)
        while True:
                pygame.mixer.music.play(-1)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            break
                        if event.key == pygame.K_RETURN:
                                return True
                self.button()
                pygame.draw.rect(self.screen,(255,255,255), (5,175,435,105),5)
                self.drawtext("Block Knight",10,50)
                self.drawtext("NEW GAME",10,180)
                pygame.display.update()
    def close(self):
        pygame.quit()
