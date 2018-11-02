class Settings():
    '''store all setting classes of Alien Invasion'''

    def __init__(self):
        '''initialize game setting'''

        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed_factor = 1.5

        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # fleet_direction = 1 indicates the right move, -1 indicates left move