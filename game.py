#
# Garrett Olsen
# garrettolsen333@gmail.com
#

# pygame imports
import os, sys
import pygame
from pygame.locals import *


# check for important modules
if not pygame.font: print 'WARNING! Fonts disabled'
if not pygame.mixer: print 'WARNING! Sound disbaled'


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


def loadSound(name):
    # subclass zero sound if sound could not be found
    class ZeroSound:
        def play(self): pass
        
    if not pygame.mixer:
        return ZeroSound()
    
    fullName = os.path.join('sounds', name)
    
    try:
        sound = pygame.mixer.Sound(fullName)
    except pygame.error, msg:
        print 'Unable to load sound:', name
        raise SystemExit, msg
    
    return sound


# class for the player controlled unit (a blue tank)
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage('blue_tank.bmp', -1)
        self.x = 200
        self.y = 200

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x += 10
        elif key[pygame.K_LEFT]:
            self.x -= 10

    def punch(self, target):
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5,-5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punching = 0


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadImage('red_enemy.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.dizzy += 12
        if(self.dizzy >= 360):
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image


def main():
    
    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('BuildWars')

    #Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((205, 205, 201))

    #Put Text On The Background
    if pygame.font:
        font = pygame.font.Font(None, 36)
        
        textTimeLeft = font.render("Time Left: ", 1, (10, 10, 10))
        textTimeLeftPos = textTimeLeft.get_rect(center=(65, 30))
        background.blit(textTimeLeft, textTimeLeftPos)

        textScore = font.render("Score: ", 1, (10, 10, 10))
        textScorePos = textScore.get_rect(center=(87, 60))
        background.blit(textScore, textScorePos)

    #Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Prepare Game Objects
    clock = pygame.time.Clock()
    enemy = Enemy()
    player = Player()
    allsprites = pygame.sprite.RenderPlain((player, enemy))

    #Main Loop
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                running = False

        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()



#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()




