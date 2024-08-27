
import pygame 
from pygame.sprite import Sprite

class UFO(Sprite):

    """A class to represent a single alien fleet """

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attributes 
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()


        #Start each new alien near the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizonatal postion 
        self.x = float(self.rect.x)


    def check_edges(self):
        """return true if ufo is at edge of screen"""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        


    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.ufo_speed * self.settings.fleet_direction)
        self.rect.x = self.x