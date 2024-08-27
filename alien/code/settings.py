

class Settings():

    def __init__(self):
#initialize the games static settings
        
        #screen settings
        self.screen_height = 800
        self.screen_width = 800
        self.bg_color = (173,216,230)
        
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

         #bullet settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 5
        self.bullet_height = 30
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3


        #Ufo settings 
        self.ufo_speed = .5
        self.fleet_drop_speed = .5
        #fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1


        #how quickly the game speeds up 
        self.speedup_scale = 1.001

        #how quikcly the ufo point value increases 
        self.score_scale = 1.5


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throguhout the game """

        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1.0

        #fleet direction of 1 represent right, -1 represent left 
        self.fleet_direction = 1 
        #scroing 
        self.alien_points = 50 





    def increase_speed(self):
        """Increase speed settimgs and alien point values """

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        


