#
# Garrett Olsen
# garrettolsen333@gmail.com
#

import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print 'Warning! Fonts disabled'


# Color Constants
GREY = (128,128,128)
LIGHT_GREY = (224,224,224)
DARK_GREY = (64,64,64)
FIRE_RED = (255,85,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

# loads an image for a Sprite
def loadImage(name, colorKey=None):
    
    # get image's full name to load
    fullName = os.path.join('images', name)
    
    try:
        img = pygame.image.load(fullName)
    except pygame.error, msg:
        print 'Unable to load image: ', name
        raise SystemExit, msg
    
    img = img.convert()
    
    if colorKey is not None:
        # grab the top-left pixel in image and use its color
        if colorKey is -1:
            colorKey = img.get_at((0,0))
            
        img.set_colorkey(colorKey, RLEACCEL)
        
    return img, img.get_rect()

# Stage Building Blocks and other classes needed
class StandardBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_coord, y_coord):
        super(StandardBlock, self).__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False
        self.rect.x = x_coord
        self.rect.y = y_coord


class PassableBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_coord, y_coord):
        super(PassableBlock, self).__init__()
        self.image = pygame.Surface([50,15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = True
        self.rect.x = x_coord
        self.rect.y = y_coord


class SpringBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_coord, y_coord):
        super(SpringBlock, self).__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False
        self.rect.x = x_coord
        self.rect.y = y_coord


class FireBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_coord, y_coord):
        super(FireBlock, self).__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False
        self.rect.x = x_coord
        self.rect.y = y_coord
        

class BuilderTarget(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage('block_target.bmp', -1)
        self.block_color = DARK_GREY
        self.rect.x = 0
        self.rect.y = 100
        self.selected_block = ""

    def moveDown(self):
        if self.rect.y != 550:
            self.rect.y += 50

    def moveUp(self):
        if self.rect.y != 100:
            self.rect.y -= 50

    def moveRight(self):
        if self.rect.x != 950:
            self.rect.x += 50

    def moveLeft(self):
        if self.rect.x != 0:
            self.rect.x -= 50

    def checkSelectedBlock(self):
        if self.selected_block == "":
            return False
        else:
            return True



def main():

    pygame.init()
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('BuildWars')

    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill(LIGHT_GREY)

    # Put text on background
    if pygame.font:
        font = pygame.font.Font(None,20)
        text_std = font.render("(Press b)", 1, (10,10,10))
        text_std_pos = text_std.get_rect(center=(65,30))
        background.blit(text_std, text_std_pos)

        font = pygame.font.Font(None,20)
        text_pass = font.render("(Press p)", 1, (10,10,10))
        text_pass_pos = text_pass.get_rect(center=(325,30))
        background.blit(text_pass, text_pass_pos)

        font = pygame.font.Font(None,20)
        text_spring = font.render("(Press s)", 1, (10,10,10))
        text_spring_pos = text_spring.get_rect(center=(575,30))
        background.blit(text_spring, text_spring_pos)

        font = pygame.font.Font(None,20)
        text_fire = font.render("(Press f)", 1, (10,10,10))
        text_fire_pos = text_fire.get_rect(center=(775,30))
        background.blit(text_fire, text_fire_pos)

        

    # Display Background
    screen.blit(background, (0,0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    standard_block_list = pygame.sprite.Group()
    passable_block_list = pygame.sprite.Group()
    spring_block_list = pygame.sprite.Group()
    fire_block_list = pygame.sprite.Group()
    build_spot_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Build Specifier Objects
    build_bar_std = StandardBlock(DARK_GREY, 50, 50)
    pygame.draw.rect(background, DARK_GREY, (165, 5, 50, 50))
    pygame.draw.rect(background, DARK_GREY, (425, 25, 50, 15))
    pygame.draw.rect(background, GREEN, (675, 5, 50, 50))
    pygame.draw.rect(background, FIRE_RED, (875, 5, 50, 50))
    pygame.draw.lines(background, False, BLACK, ([0, 100],[1000,100]))
    pygame.display.update()


    
    

    running = True
    in_building_phase = True
    new_block = None

    target_block_spot = BuilderTarget()
    
    while running:
        clock.tick(60)

        # building phase first
        if in_building_phase:
            
            all_sprites.add(target_block_spot)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == KEYDOWN and event.key == K_b:
                    target_block_spot.selected_block = "standard"
                    
                if event.type == KEYDOWN and event.key == K_p:
                    target_block_spot.selected_block = "passable"
                    
                if event.type == KEYDOWN and event.key == K_s:
                    target_block_spot.selected_block = "spring"
                    
                if event.type == KEYDOWN and event.key == K_f:
                    target_block_spot.selected_block = "fire"
                    
                if event.type == KEYDOWN and event.key == K_DOWN:
                    target_block_spot.moveDown()

                if event.type == KEYDOWN and event.key == K_UP:
                    target_block_spot.moveUp()

                if event.type == KEYDOWN and event.key == K_RIGHT:
                    target_block_spot.moveRight()

                if event.type == KEYDOWN and event.key == K_LEFT:
                    target_block_spot.moveLeft()

                if event.type == KEYDOWN and event.key == K_RETURN:
                    if target_block_spot.selected_block == "standard":
                        new_block = StandardBlock(DARK_GREY, target_block_spot.rect.x, target_block_spot.rect.y)
                    elif target_block_spot.selected_block == "passable":
                        new_block = PassableBlock(DARK_GREY, target_block_spot.rect.x, target_block_spot.rect.y)
                        print "pass"
                    elif target_block_spot.selected_block == "spring":
                        new_block = SpringBlock(GREEN, target_block_spot.rect.x, target_block_spot.rect.y)
                        print "spring"
                    elif target_block_spot.selected_block == "fire":
                        new_block = FireBlock(FIRE_RED, target_block_spot.rect.x, target_block_spot.rect.y)
                        print "fire"
                    else:
                        print "nada"

                    all_sprites.add(new_block)
                    
                    

            all_sprites.update()

            screen.blit(background, (0,0))
            all_sprites.draw(screen)
            pygame.display.flip()
                
main()
