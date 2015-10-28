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
        font = pygame.font.Font(None,36)
        text_build = font.render("To Build: b", 1, (10,10,10))
        text_build_pos = text_build.get_rect(center=(65,30))
        background.blit(text_build, text_build_pos)

    # Display Background
    screen.blit(background, (0,0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    standard_block_list = pygame.sprite.Group()
    passable_block_list = pygame.sprite.Group()
    spring_block_list = pygame.sprite.Group()
    fire_block_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_b:
                new_block = StandardBlock(DARK_GREY,50,50)
                new_block.rect.x = 300
                new_block.rect.y = 300
                standard_block_list.add(new_block)
                all_sprites.add(new_block)
            if event.type == KEYDOWN and event.key == K_p:
                new_block = PassableBlock(DARK_GREY,50,15)
                new_block.rect.x = 200
                new_block.rect.y = 200
                passable_block_list.add(new_block)
                all_sprites.add(new_block)
            if event.type == KEYDOWN and event.key == K_s:
                new_block = SpringBlock(GREEN,50,50)
                new_block.rect.x = 100
                new_block.rect.y = 100
                spring_block_list.add(new_block)
                all_sprites.add(new_block)
            if event.type == KEYDOWN and event.key == K_f:
                new_block = FireBlock(FIRE_RED,50,50)
                new_block.rect.x = 400
                new_block.rect.y = 400
                fire_block_list.add(new_block)
                all_sprites.add(new_block)
                

        all_sprites.update()

        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        pygame.display.flip()
                
main()
