import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''initialize ship and set initial position'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and obtain its rectangular shape
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put each ship in the center and bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float value
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # adjust ship location according to moving flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object
        self.rect.centerx = self.center

    def blitme(self):
        '''paint ship at the specified location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''put ship in the center of screen'''
        self.center = self.screen_rect.centerx