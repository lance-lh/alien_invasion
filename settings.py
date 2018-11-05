class Settings():
    '''store all setting classes of Alien Invasion'''

    def __init__(self):
        '''initialize game setting'''
        # initialize all static settings
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ship setting
        self.ship_limit = 3

        # bullet setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # alien setting
        self.fleet_drop_speed = 10

        # acceleration
        self.speedup_scale = 1.1
        # alien score increasing speed
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize all changeable setting when game starts'''

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1  # fleet_direction = 1 indicates the right move, -1 indicates left move

        # point record
        self.alien_points = 50

    def increase_speed(self):
        '''increase speed setting'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points *= int(self.alien_points * self.score_scale)
        # print(self.alien_points)