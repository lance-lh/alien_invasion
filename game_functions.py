import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen, ship,bullets):
    if event.key == pygame.K_RIGHT:
        # move ship to right
        # ship.rect.centerx += 1
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
        # if len(bullets) < ai_settings.bullets_allowed:
        #     # create a bullet and add it into group
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    '''response events like keyboard and mouse'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)

            # if event.key == pygame.K_RIGHT:
            #     # move ship to right
            #     # ship.rect.centerx += 1
            #     ship.moving_right = True
            #
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True


        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            #
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_buttons(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_buttons(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''click play button to start the game'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
    # if play_button.rect.collidepoint(mouse_x,mouse_y):
        # reset game setting
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # empty aliens and bullets list
        aliens.empty()
        bullets.empty()

        # create a bunch of aliens and put ship in the center of screen
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats,sb,ship, aliens, bullets,play_button):
    '''update image in screen and switch to new screen'''
    # recreate screen once loop
    screen.fill(ai_settings.bg_color)

    # repaint all bullets after ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    # display the score on the screen
    sb.show_score()

    # if game is not active, then draw play button
    if not stats.game_active:
        play_button.draw_button()

    # let the newest created screen visible
    pygame.display.flip()  # update the screen state

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''update the bullet location and delete vanished bullet'''
    # update bullet location
    bullets.update()

    # check the bullet hit alien or not
    # if so, delete the bullet and alien

    # delete vanished bullet
    for bullet in bullets.copy():  # not delete bullet in Group but its copy group
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))          # to check the left bullets in Group

    check_bullet_alien_collisons(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisons(ai_settings,screen,stats,sb,ship,aliens,bullets):
    '''respond to collision between aliens and bullets'''
    # delete crashed bullets and aliens
    collissions = pygame.sprite.groupcollide(bullets,aliens,True, True)  # return a dict , key is a bullet and value is an alien

    if collissions:
        for aliens in collissions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        # delete existing bullets and create new aliens
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def fire_bullet(ai_settings,screen,ship,bullets):
    '''if not reach the bullet number limit, then fire a bullet'''
    if len(bullets) < ai_settings.bullets_allowed:
        # create a bullet and add it into group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''calculate the  screen can contain how many lines of alien'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen,ship,aliens):
    '''create aliens'''
    # create an alien and calculate how many aliens contain in one line
    # the width between two aliens is the twice of alien width
    alien = Alien(ai_settings,screen)
    # alien_width = alien.rect.width
    # available_space_x = ai_settings.screen_width - 2 * alien_width
    # number_aliens_x = int(available_space_x / (2 * alien_width))

    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the fitst line alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # create an alien and add it to the current line
            # alien = Alien(ai_settings, screen)
            # alien_x = alien_width + 2 * alien_width * alien_number
            # alien.rect.x = alien_x
            # aliens.add(alien)
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
    '''when alien appears at the screen edge, take some measures'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''move aliens down and change their direction'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''collision response'''
    if stats.ships_left > 0:
        # ships_left - 1
        stats.ships_left -= 1


        # empty alien list and bullet list
        aliens.empty()
        bullets.empty()

        # create a bunch of new aliens and put ship in the center and bottom of screen
        create_fleet(ai_settings, screen, ship,aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''check whether aliens arrive at the bottom of screen or not'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            '''deal with this situation just like ship collision'''
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(ai_settings, stats, screen,ship, aliens, bullets):
    '''check alien appears at the screen edge or not, and update aliens location'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    '''check collissions　between aliens and ship'''
    if pygame.sprite.spritecollideany(ship,aliens):
        # print("Ship hit!!!")
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)