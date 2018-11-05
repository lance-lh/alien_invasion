import pygame.font

class Button():

    def __init__(self,ai_settings,screen,msg):  # msg indicates messages to be displayed in the screen
        '''initialize the property of button'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set button size and other properties
        self.width, self.height = 200,50
        self.button_color = (0,255,0)               # green
        self.text_color = (255,255,255)             # white
        self.font = pygame.font.SysFont(None,48)

        # create button rect object and align it to center
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # button label (only one time created enough)
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''msg --> image, in the center of button'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''draw a button filled with color, and text on it'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)