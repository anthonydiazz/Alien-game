
class Gamestats:

    """track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize stats """
        #start ai in an active state
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()
        #high score should never be ressetted 
        self.high_score = 0


    def reset_stats(self):
        """Initialaize stats that can change durign the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1