
import pygame.font 
from pygame.sprite import Group

from ship import Rocketship

class Scoreboard:
    """A class to report scoring information. """

    def __init__(self,ai_game):

        """Initialize scorekeeping attritbutes """
        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font setting for scoring info 
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare the initial scroe image. 
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_high_score(self):
        """turn the high score into a rendered imaged """
        high_score = round(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #create the high score at the top of teh secreen 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_score(self):
        """turn the score into a rendered image."""
        rounded_score = round(self.stats.score, 1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20

    def prep_level(self):
        """trun the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #positon the level belowe the scroe 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """Show how many ships are left """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Rocketship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 
            self.ships.add(ship)

    def check_high_scores(self):
        """check to seee if there is a new high score """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score and levels, ships  to the screen"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
