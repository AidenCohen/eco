import sys
import pygame
import time
import keyboard
import textwrap
class intro_loading:
    def __init__(self):

            size=width, height=450, 280


            self.screen=pygame.display.set_mode(size)

    def textbox(self):
        pygame.draw.rect(self.screen,pygame.Color("black"), (10,180,430,100), 5)
    def print_slow(self,str,int):
        x = 0
        y = int
        for letter in str:
                if(keyboard.is_pressed('space')):
                    myfont = pygame.font.SysFont("monospace", 15)
                    label = myfont.render(letter, 1, (1,1,1))
                    self.screen.blit(label, (20 + x, 200 + y))
                    x = x+10
                    time.sleep(.005)
                    pygame.display.update()
                else:
                    myfont = pygame.font.SysFont("monospace", 15)
                    label = myfont.render(letter, 1, (1,1,1))
                    self.screen.blit(label, (20 + x, 200 + y))
                    x = x+10
                    time.sleep(.1)
                    pygame.display.update()

    def text1(self,word,x,y):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(word, 1, (1,1,1))
        return self.screen.blit(label,(x,y))

    def inpt(self,text, number):
        word=""
        self.print_slow(text, 0)
        pygame.display.flip()
        done = True
        while done:
            for letter in word:
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(word, 1, (1,1,1))
                self.screen.blit(label,(230,220))
                pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        word+=str(chr(event.key))
                    if event.key == pygame.K_b:
                        word+=chr(event.key)
                    if event.key == pygame.K_c:
                        word+=chr(event.key)
                    if event.key == pygame.K_d:
                        word+=chr(event.key)
                    if event.key == pygame.K_e:
                        word+=chr(event.key)
                    if event.key == pygame.K_f:
                        word+=chr(event.key)
                    if event.key == pygame.K_g:
                        word+=chr(event.key)
                    if event.key == pygame.K_h:
                        word+=chr(event.key)
                    if event.key == pygame.K_i:
                        word+=chr(event.key)
                    if event.key == pygame.K_j:
                        word+=chr(event.key)
                    if event.key == pygame.K_k:
                        word+=chr(event.key)
                    if event.key == pygame.K_l:
                        word+=chr(event.key)
                    if event.key == pygame.K_m:
                        word+=chr(event.key)
                    if event.key == pygame.K_n:
                        word+=chr(event.key)
                    if event.key == pygame.K_o:
                        word+=chr(event.key)
                    if event.key == pygame.K_p:
                        word+=chr(event.key)
                    if event.key == pygame.K_q:
                        word+=chr(event.key)
                    if event.key == pygame.K_r:
                        word+=chr(event.key)
                    if event.key == pygame.K_s:
                        word+=chr(event.key)
                    if event.key == pygame.K_t:
                        word+=chr(event.key)
                    if event.key == pygame.K_u:
                        word+=chr(event.key)
                    if event.key == pygame.K_v:
                        word+=chr(event.key)
                    if event.key == pygame.K_w:
                        word+=chr(event.key)
                    if event.key == pygame.K_x:
                        word+=chr(event.key)
                    if event.key == pygame.K_y:
                        word+=chr(event.key)
                    if event.key == pygame.K_z:
                        word+=chr(event.key)
                    if event.key == pygame.K_1:
                        word+=chr(event.key)
                    if event.key == pygame.K_2:
                        word+=chr(event.key)
                    if event.key == pygame.K_3:
                        word+=chr(event.key)
                    if event.key == pygame.K_4:
                        word+=chr(event.key)
                    if event.key == pygame.K_5:
                        word+=chr(event.key)
                    if event.key == pygame.K_6:
                        word+=chr(event.key)
                    if event.key == pygame.K_7:
                        word+=chr(event.key)
                    if event.key == pygame.K_8:
                        word+=chr(event.key)
                    if event.key == pygame.K_9:
                        word+=chr(event.key)
                    if event.key == pygame.K_BACKSPACE and number == True:
                        x_1 = 0
                        word = word[:-1]
                        self.screen.fill(pygame.Color("white"))
                        self.textbox()
                        self.text1("I.. I.. forgot my name", 20+x_1 ,220)
                        x_1 = x_1 + 10
                        nindorino = pygame.image.load("block.png")
                        self.screen.blit(nindorino,(140,25))
                    if event.key == pygame.K_BACKSPACE and number == False:
                        x = 0
                        nindorino = pygame.image.load("block.png")
                        word = word[:-1]
                        self.screen.fill(pygame.Color("white"))
                        self.textbox()
                        self.text1("...Erm, what is his name again?", 20+x ,220)
                        x = x + 10
                        self.screen.blit(nindorino,(140,25))
                    if event.key == pygame.K_RETURN:
                        done=False
                    if event.key == pygame.K_RETURN and word == "" and number == True:
                        word = "Red"
                        done = False
                    if event.key == pygame.K_RETURN and word == "" and number == False:
                        word = "Blue"
                        done = False
                    if word == "blockknight1":
                            x_2 = 0
                            nindorino = pygame.image.load("block.png")
                            word = word[:-1]
                            self.screen.fill(pygame.Color("white"))
                            self.textbox()
                            nindorino = pygame.image.load("block.png")
                            x_2 = x_2 + 10
                            self.screen.blit(nindorino,(140,25))
                            self.text1("The True One", 20+x_2 ,220)
                            pygame.display.update()
        aiden = word
        return aiden
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break
        pygame.init()
        speed=[1,1]
        color=244,244,244
        nindorino = pygame.image.load("block.png")
        while True:
            pygame.mixer.init()
            sound = pygame.mixer.music.load("promise.mp3")
            pygame.mixer.music.play(-1)
            self.screen.fill(pygame.Color("white"))
            pygame.display.update()
            self.screen.blit(nindorino,(140,25))
            self.textbox()
            self.print_slow("There was once a block who wanted" , 0)
            self.print_slow("to be a knight" , 30)
            pygame.display.update()
            while not keyboard.is_pressed("."):
                time.sleep(1)
            self.screen.fill(pygame.Color("white"))
            self.textbox()
            self.screen.blit(nindorino,(140,25))
            self.print_slow("He went to the block king",0)
            self.print_slow("and asked for a position", 30)
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            self.screen.fill(pygame.Color("white"))
            self.screen.blit(nindorino,(140,25))
            self.textbox()
            self.print_slow("Here I am now, clothed in shame", 0 )
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            self.screen.fill(pygame.Color("white"))
            self.screen.blit(nindorino,(140,25))
            self.textbox()
            self.print_slow( "The king had exiled me to the darklands" , 0)
            self.print_slow("and forced me to wear this clothing", 30)
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            self.screen.fill(pygame.Color("white"))
            self.screen.blit(nindorino,(140,25))
            self.textbox()
            self.print_slow("I need to get back, I need to",0)
            self.print_slow("fuffill my dream" , 30)
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            self.screen.fill(pygame.Color("white"))
            self.textbox()
            self.screen.blit(nindorino,(140,25))
            aiden = self.inpt("I.. I.. forgot my name", True)
            pygame.display.update()
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            self.screen.fill(pygame.Color("white"))
            self.textbox()
            pygame.display.update()
            self.print_slow("I remember now! It's " + aiden , 0)
            pygame.display.update()
            while not keyboard.is_pressed("."):
                time.sleep(1)
            pygame.display.update()
            i = 0
            while i < 10:
                self.screen.fill(pygame.Color("black"))
                pygame.display.update()
                time.sleep(1)
                self.screen.fill(pygame.Color("white"))
                time.sleep(1)
                i = i+1
                pygame.display.update()
            pygame.display.update()
            self.textbox()
            self.screen.fill(pygame.Color("white"))
            self.print_slow( " I'm waking uppp!!!" , 0 )
            while not keyboard.is_pressed("."):
                time.sleep(1)

            pygame.quit()
            break
