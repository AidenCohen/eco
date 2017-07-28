import pygame
from pygame.locals import *
from player import Player
from block import Block
from scroll import scroll
from npc import character
from enemy import enemy
import pygame
import random
import time
import intro
import keyboard
from sword import sword

class game:
    def __init__(self,debug):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.width=1400
        self.height=800
        self.playerQuit=False
        self.screen_width = 1400
        self.screen_height = 800
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.player_killed = False
    def ApplyGravity(self,all_sprites_list):
        for sprite in all_sprites_list:
            if(sprite.gravity==True):
                sprite.rect.y+=1
        time.sleep(0.01)

    def ClimbObsticle(self,player,block_list):
        blocks_hit = pygame.sprite.spritecollide(player, block_list,False)
        for hit_block in blocks_hit:
            if(player.rect.y+player.height < hit_block.rect.y or
                player.rect.y < hit_block.rect.y+player.height
                ):
                player.rect.y = hit_block.rect.y-player.height


    def print_slow(self,str,int):
        x = 0
        y = int
        for letter in str:
            if(keyboard.is_pressed('space')):
                myfont = pygame.font.SysFont("monospace", 18)
                label = myfont.render(letter, 1, (255,255,255))
                self.screen.blit(label, (200 + x, 600 + y))
                x = x+10
                time.sleep(.005)
                pygame.display.update()
            else:
                myfont = pygame.font.SysFont("monospace", 18)
                label = myfont.render(letter, 1, (255,255,255))
                self.screen.blit(label, (200 + x, 600 + y))
                x = x+10
                time.sleep(.1)
                pygame.display.update()

    def textbox(self):
        pygame.draw.rect(self.screen,pygame.Color("white"), (200,600,1000,100), 5)
    def run(self):

        BLACK = (  0,   0,   0)
        WHITE = (255, 255, 255)
        RED   = (255,   0,   0)
        GREEN = (0,255,0)
        BLUE = (0,0,255)
        ORANGE = (255,165,0)
        pygame.init()



        person = character(BLUE,10,15)
        person.rect.y= self.screen_height/4
        player = Player(RED, 10, 15,1,0)
        player.rect.y=self.screen_height  /4
        enemy1 = enemy(GREEN,20,15,1)
        enemy1.rect.y = self.screen_height/4
        sword1 = sword(ORANGE,1)
        subblocks_list = pygame.sprite.Group()

        block_list = pygame.sprite.Group()

        all_sprites_list = pygame.sprite.Group()
        sword_list = pygame.sprite.Group()

        lag = self.screen_height  /4
        for i in range(int(self.screen_width/(player.width))):
            # This represents a block
            block = Block(BLACK, 20, 15)

            # Set a random location for the block
            block.rect.x = i*block.width
            block.rect.y = (lag-15) + random.randrange(30)
            height=block.rect.y
            while(height < self.screen_height):
                subblock = Block(BLACK, 20, 15)
                subblock.rect.x=block.rect.x
                height = height + subblock.height
                subblock.rect.y= height
                subblocks_list.add(subblock)
                all_sprites_list.add(subblock)


            # Add the block to the list of objects
            lag = block.rect.y
            block_list.add(block)
            all_sprites_list.add(block)
        all_sprites_list.add(person)
        all_sprites_list.add(player)

        person.rect.x = 500
        person.rect.y = 0
        player.rect.y = 0
        done = False
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.ClimbObsticle(player,block_list)

            # Clear the screen
            self.screen.fill(WHITE)

            self.ApplyGravity(all_sprites_list)
            keys=pygame.key.get_pressed()
            player.flush()
            if keys[K_LEFT]:
                player.moveleft(self.screen_width)

            if keys[K_RIGHT]:
                player.moveright(self.screen_width)
            aiden = pygame.sprite.spritecollide(player, block_list, False)
            cohen = pygame.sprite.spritecollide(person, block_list, False)
            if len(cohen) == 0   :
                person.rect.y = person.rect.y +1
                pygame.display.update()
            if keys[K_UP] and len(aiden) > 0 :
                    player.jump(self.screen_height)
                    '''
            if(player.rect.x == 1390):
                    aiden = scroll()
                    aiden.scroll()
                    '''
            level = 1
            if(player.rect.x == 1400):
                level = level+1
            cohen = pygame.sprite.spritecollide(person, all_sprites_list, False)
            if level == 1 and keys[K_RETURN] and len(cohen) >  1 :
                all_sprites_list.draw(self.screen)
                self.textbox()
                self.print_slow("good sir, welcome! We need HELP! Our village has been taken by the Circles!!!", 0)
                self.print_slow("We have been at war with the other shapes for a long time",30)
                self.print_slow("We have been butchered, we need YOU to help us win aginst the invaders",60)
                self.screen.fill(WHITE)
                all_sprites_list.draw(self.screen)
                self.textbox()
                self.print_slow("here take this sword to defend yourself",0)
                all_sprites_list.add(enemy1)
                enemy1.rect.x = 1000
                enemy1.rect.y = 0
                while not keyboard.is_pressed("."):
                    time.sleep(1)
            ac = pygame.sprite.spritecollide(enemy1, block_list, False)
            if len(ac) == 0 :
                enemy1.rect.y = enemy1.rect.y +1
            if len(ac) != 0:
                enemy1.rect.y = enemy1.rect.y -30
                enemy1.attack(player)
            ceci = pygame.sprite.collide_rect(player,enemy1)
            if ceci :
                player.health = player.health - 1
            if player.health <= 0 :
                player.kill()
                self.player_killed = True
            gold = pygame.sprite.collide_rect(sword1,enemy1)
            if(keys[K_DOWN] and self.player_killed == False):
                sword_list.add(sword1)
                sword_list.draw(self.screen)
                sword1.attack(player)

                if gold:
                    enemy1.health = enemy1.health - sword1.damage
            if(not keys[K_DOWN]):
                sword1.kill()
            if(enemy1.health <= 0):
                enemy1.kill()
            if(keys[K_p]):
                    pygame.time.delay(1)


            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            '''pos = pygame.mouse.get_pos()

            # Fetch the x and y out of the list,
               # just like we'd fetch letters out of a string.
            # Set the player object to the mouse location

            player.rect.x = pos[0]
            player.rect.y = pos[1]
            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                score += 1
                print(score)
            '''
            # Draw all the spites that may need to be drawn
            all_sprites_list.draw(self.screen)



            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 60 frames per second
            clock.tick(120)

        pygame.quit()
#############################################
if __name__ == "__main__" :
    theApp = game(False)

#this is the game code containing the game loop and all apspects of controls
