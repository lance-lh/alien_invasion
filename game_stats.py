class GameStats():
    '''track statistical information'''

    def __init__(self,ai_settings):
        '''initialize statistical information'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # when game starts, flag inactive
        self.game_active = False

    def reset_stats(self):
        '''initialize all changeable statistical information'''
        self.ships_left = self.ai_settings.ship_limit