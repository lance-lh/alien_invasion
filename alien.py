import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''single alien class'''

    def __init__(self,ai_settings,screen):
        '''initialize alien and set its initial location'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien image and set its rect prosperity
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # initially, each alien appears at (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate location of aliens
        self.x = float(self.rect.x)

    def check_edges(self):
        '''if alien appears at the edge of the screen, then return  True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''move alien to right'''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        '''paint alien at the specific location'''
        self.screen.blit(self.image, self.rect)