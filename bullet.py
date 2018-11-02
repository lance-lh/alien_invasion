import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''manage bullet class'''

    def __init__(self,ai_settings, screen, ship):
        '''create a bullet object at the ship location'''
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rectangular at (0,0) and then move it to proper location
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store location of bullet in float type
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''move up bullet'''
        # update float location of bullet
        self.y -= self.speed_factor
        # uodate bullet rect
        self.rect.y = self.y

    def draw_bullet(self):
        '''paint bullet in the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)