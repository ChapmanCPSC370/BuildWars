#
# Garrett Olsen
# garrettolsen333@gmail.com
#

import os, sys
import pygame
from pygame.locals import *

if not pygame.font:
    print 'Warning! Fonts disabled'


GREY = (128,128,128)
LIGHT_GREY = (224,224,224)
DARK_GREY = (64,64,64)
FIRE_RED = (255,85,0)
GREEN = (0,255,0)
BLACK = (0,0,0)



class StandardBlock(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(StandardBlock, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False


class PassableBlock(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(PassableBlock, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = True


class SpringBlock(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(SpringBlock, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False


class FireBlock(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(FireBlock, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.passable = False


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
    new_block = None
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_b:
                new_block = StandardBlock(DARK_GREY,50,50)
                
            if event.type == KEYDOWN and event.key == K_p:
                new_block = PassableBlock(DARK_GREY,50,15)
                
            if event.type == KEYDOWN and event.key == K_s:
                new_block = SpringBlock(GREEN,50,50)
                
            if event.type == KEYDOWN and event.key == K_f:
                new_block = FireBlock(FIRE_RED,50,50)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_block != None:
                    x, y = pygame.mouse.get_pos()
                    new_block.rect.x = x
                    new_block.rect.y = y
                    all_sprites.add(new_block)
                

        all_sprites.update()

        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        pygame.display.flip()
                
main()
