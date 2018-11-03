import sys
import pygame
from settings import Settings   # screen size and bg_color
from ship import Ship           # ship location in the screen
from alien import Alien
import game_functions as gf     # event check and screen update
from pygame.sprite import Group


def run_game():
    # initialize the game, screen object,setting
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))  # define a tuple which indicates screen size, width:1200, height:800.
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings,screen)                    # screen is the second location parameter

    # create a group to contain bullets
    bullets = Group()

    aliens = Group()

    # create aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # set background color
    # bg_color = (230,230,230)

    # start the main loop of game

    # create an alien
    alien = Alien(ai_settings, screen)

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        # # monitor the keyboard and mouse
        # for event in pygame.event.get():   # event loop
        #     if event.type == pygame.QUIT:  # to capture keyboard or mouse state, use method pygame.event.get()
        #         sys.exit()                 # if the state is active, then it indicates the while loop is true.
        #                                    # use sys module to quit the game
        ship.update()

        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        # bullets.update()
        #
        # # delete vanished bulletq
        # for bullet in bullets.copy():  # not delete bullet in Group but its copy group
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # # print(len(bullets))          # to check the left bullets in Group

        gf.update_aliens(ai_settings, ship, aliens)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        # # recreate screen once loop
        # screen.fill(ai_settings.bg_color)
        #
        # ship.blitme()
        #
        # # let the newest created screen visible
        # pygame.display.flip()              # update the screen state

run_game()