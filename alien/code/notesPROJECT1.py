#PART 1
#starting the game project

import sys 
#we are importing the sys module to exit out the game when the player quits 
import pygame
#the pygame module has functionality to make the game 

class AlienInvasion:

    """Overall class to mangage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        #this code above creates a display window, where we will draw all the games graphical elemts 
        #the argument of (1200,800) is a tuple that defines the dimesnions fo the game window, which will be 
        #1200 pixels wide and 800 pixels high(you can adjust thse values depnading on the size)
        #we assign the display window to the variabel self.screen

        #the object we assinged to self,screen is called a surface 
        #a surface in pygame is oart of the screen where a game elment can be displayed

        pygame.display.set_caption("Alien Invasion")



        #Set the backgound color.
        #colors in pygame are specified as RGB colors: a mix of red,green, and blue
                    #each color value ranges from 0 to 255
                    #red is (255,0,0) (0,255,0)is green and (0,0,255)is blue 
                    #(230,230,230) mixes a little of everything and makes grey 
                    #we assigned this to self.bg_color
        self.bg_color = (230,230,230)

    #the game is controlled by the method down below 
        #this method contains a while loop
    def run_game(self):
        """Start the main loop for the game"""

        while True:
            """Watch for keyboard and mouse events"""
            #the while loop contains an event loop and code that manages screen updates 
            #an event is an action that the user performs while playing the gmae, such as 
            #pressing a key or moving the mouse 
            #to make our program respond to events we write this eent loop to listen for events and perform appropriate tasks

            for event in pygame.event.get():
                #this is an event loop
                #to access the events that pygame detects, we will use the pygame.event.get()fucntion
                #this fucntion returns a list of events that have taken place since the last time this fucntion was called
                if event.type == pygame.QUIT:
                    #for example when the player clicks the game windows close buttom, a pygame.QUIT event is detected and we call sys.exti() to exit the game
                    sys.exit()


            #Redrawn the screen durin each pass through the loop 
            #the code below we fill the screen with the background color using the fill() method, which acts on a surface and takes only one arguemtn a color
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible 
                    #the code below tells pyhton to make the most recently drawn screen visible, in this case it simply draws an empyt screen 
                    #on each pass through the while loop, erasing the old screen so only the new screen is visible 
                    #when we move the game elemts around , pygame.display.flip() continually ipdates the display to show the new positions of game elemts 
                    #and hides the old ones creating the illusion of smooth movement 
            pygame.display.flip()

if __name__ == '__main__':
    """Make a game instance, and run the game"""
# creating an instance of the game 
    ai = AlienInvasion()
    #then calling run_game() method
    #we place run_game() in an if block only becasue we only want it to run if the file is called directly 
    ai.run_game()


#PART 2
#Creating another module that contains all the settings and then importing them inot this file
    #settings.py
class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initilaize the game's setting"""
        #Screen setting 

        self.screen_width = 1200
        self.screen_length = 800
        self.bg_color = (200,200,200)


#aliens.py
        #the file that will be using the attributes above
import sys  
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to mangage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        #creating an instance to settings which is assing to self.settings 
        self.settings = Settings()
        #the code below we use the screen_width and screen_height attributes of self.settigns 
        #and then we use self.settings to access the background color when fillin the screen 
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_length))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            """Watch for keyboard and mouse events"""


            for event in pygame.event.get():
                #this is an event loop
                if event.type == pygame.QUIT:
                    #for example when the player clicks the game windows close buttom, a pygame.QUIT event is detected and we call sys.exti() to exit the game
                    sys.exit()

            #Redrawn the screen durin each pass through the loop 
            #the code below we fill the screen with the background color using the fill() method, which acts on a surface and takes only one arguemtn a color
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible 
            pygame.display.flip()

if __name__ == '__main__':
    """Make a game instance, and run the game"""
    ai = AlienInvasion()
    ai.run_game()


    
    #PART 3 
"""Adding the ship Image"""
"""This class will mange most of the behavior of the players ship"""

import pygame
class Rocketship():

    def __init__(self,ai_game):
        """Initliazie the ship and its starting point"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        #Load the ships image and get its rect.
        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()
        """Start each new ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


#settings of the game 
class Settings():

    def __init__(self):
#the screen of the game
        self.screen_length = 900
        self.screen_width = 800
        self.bg_color = (200,200,200)





import sys
import pygame
from settings import Settings
from ship import Rocketship
class AlienInvasion():

    def __init__(self):
        """creating the screen of the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_length,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Rocketship(self)
    def run_game(self):

        while True:
#the actions of the game 
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            """drawing the ship on the screen"""
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()





#Now we are piloting the ship
#Introducting the keydown event 
#aliens.py
    
import sys
import pygame
from settings import Settings
from ship import Rocketship

class AlienInvasion():

    def __init__(self):
#Initializing the game down below 
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_length,self.settings.screen_height))
        pygame.display.set_caption("Soval will destroy")

        self.ship = Rocketship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._updates_screen()
            

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          #MOVE SHIP TO THE RIGHT 
                          self.ship.moving_right = True

                     elif event.type == pygame.KEYUP:
                          if event.key == pygame.K_RIGHT:
                               self.ship.moving_right = False
                    

                          #this only allows it to move right one pixel at a time 

    
    def _updates_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#ship.py
import pygame 

class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/sova.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        #if you are not moving it is false if you are moving right it is then set to true

    def update(self):

        """Update the ships postiion based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1


    def blit(self):

        self.screen.blit(self.image,self.rect)

#settings.py
class Settings():

    def __init__(self):

        self.screen_length = 1200
        self.screen_height = 800
        self.bg_color = (173,216,230)






###moving both left and right 
#creating two different methods with press down and press up 
#added information in settings.py and ship.py

import sys
import pygame
from settings import Settings
from ship import Rocketship

class AlienInvasion():

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Rocketship(self)

    def run_game(self):
        while True:
             self._check_events()
             self._updates_screen()
             self.ship.update()


    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                      self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                      self._check_keyup_events(event)

    def _check_keydown_events(self,event):
                #Respond to keypresses 
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.key == pygame.K_q:
                  sys.exit()

    def _check_keyup_events(self, event):
                    #Respond to key releases
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _updates_screen(self):
            self.screen.fill(self.settings.bg_color)
            
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()


#settings.py
class Settings():

    def __init__(self):

        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (173,216,230)

        # Ship settings 

        self.ship_speed = 1.5 

#ship.py
import pygame
class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
      

        self.image = pygame.image.load('images/sova.bmp')
        self.rect = self.image.get_rect()
#position the bottom center of the rocketship image at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image,self.rect)


#FINALES BEFORE ADDING ALIENS 
#aliens.py 
import sys
import pygame
from settings import Settings
from ship import Rocketship
from bullets import Bullet

class AlienInvasion():

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
             self._check_events()
             self.ship.update()
             self.bullets.update()

              #Get rid of bullets that have disapeared 
             for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)

             self._updates_screen()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                      self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                      self._check_keyup_events(event)

    def _check_keydown_events(self,event):
                #Respond to keypresses 
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            
            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()
            elif event.key == pygame.K_q:
                  sys.exit()

            

    def _check_keyup_events(self, event):
                    #Respond to key releases
            if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _updates_screen(self):
            self.screen.fill(self.settings.bg_color)
            
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            pygame.display.flip()

if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()

#settigns.py
class Settings():

    def __init__(self):

        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (173,216,230)

        # Ship settings 

        self.ship_speed = 1.5 

        #bullet settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        
#bullets.py 
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self,ai_game):

        """create a bullet object at the ships current postion """

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect at (0,0) and then set correct posision.

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet position as a decimal value 
        self.y = float(self.rect.y)
    
    def update(self):
        """move the bullet up the screen """
        #update the decimal postion of the bullet 

        self.y -= self.settings.bullet_speed
        #update the rect position.
        self.rect.y = self.y

#ship.py
import pygame
class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
      

        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed



        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)



###FIANLE BEFORE INCLUDING ALIENS INTO THE GAEM to shoot down 
        
#aliens.py main file 
import sys
import pygame 
from settings import Settings
from ship import Rocketship
from bullets import Bullet

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#settigns.py 

class Settings():

    def __init__(self):

        self.screen_height = 1200
        self.screen_width = 800
        self.bg_color = (173,216,230)
        

        self.ship_speed = 1.5

         #bullet settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

#ship.py 

import pygame

class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

#bullets.py
        
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)



    def update(self):
        """move the bullet up the screen """
        #update the decimal postion of the bullet 

        self.y -= self.settings.bullet_speed
        #update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)

#chapter 13 aliens 
import sys
import pygame 
from settings import Settings
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

#ufo.py 

import pygame 
from pygame.sprite import Sprite

class UFO(Sprite):

    """A class to represent a single alien fleet """

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attributes 
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()


        #Start each new alien near the top left of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizonatal postion 
        self.x = float(self.rect.x)

#in the code above the only thing that has been changed is the new file we created 
#which is the ufo file that introduces the aline image and then on the main file puts the image there
#it then takes the image and adds it into the screen and manipulates the amount of time it shows up in each row 


#PART 2 Moving the fleet 
#the only files that have been altered are the settings file, ufo file, and the main file aliens.py 

#aliens.py 
        
import sys
import pygame 
from settings import Settings
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()


    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#settings.py 

class Settings():

    def __init__(self):

        self.screen_height = 800
        self.screen_width = 800
        self.bg_color = (173,216,230)
        

        self.ship_speed = 1.5

         #bullet settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


        #Ufo settings 
        self.ufo_speed = .5
        self.fleet_drop_speed = 1
        #fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1


#ufo.py 

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


#for the code above in the main file the _update_bullets method was missing 

#next part is eliminating aliens 
#introduction to sprite.groupcollide() this helps look for collisions between objects 
#for example the bullets and ufo ships 
        
#the only thing that was altered to do this was the alien.py file 

import sys
import pygame 
from settings import Settings
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
    
        
    


    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()


    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#altering the main file to check colliosn and to repopulate the alines 
import sys
import pygame 
from settings import Settings
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
         
    
        
    


    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              print("Ship hit!!!")


    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#next step is finding a way to mkae the players lose 
#finding a way to end the game 
#new file Gamestats
import sys
from time import sleep

import pygame 

from settings import Settings
from gamestats import Gamestats
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #create an instance that stores game stats 

        self.stats = Gamestats(self)
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons()




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
         
    
        
    
    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              self._ship_hit()



    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


    def _ship_hit(self):
         """respond to the ship being hit by an alien"""

         #decrement ships_left
         self.stats.ships_left -= 1

         #get rid of any remaining alienas and bullets 
         self.ufo.empty()
         self.bullets.empty()

         #create a new fleet and center the ship
         self._create_fleet()
         self.ship._center_ship()

         #pause 
         sleep(0.5)
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

#gamestats.py 
class Gamestats:

    """track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize stats """
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialaize stats that can change durign the game """
        self.ships_left = self.settings.ship_limit

#ship.py 
import pygame

class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def _center_ship(self):
        """center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



#settings.py 
class Settings():

    def __init__(self):

        self.screen_height = 800
        self.screen_width = 800
        self.bg_color = (173,216,230)
        
        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

         #bullet settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 30
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


        #Ufo settings 
        self.ufo_speed = .5
        self.fleet_drop_speed = 50
        #fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = .5



#now to solve the problem of what happens when an aliena reaches the bottom fo the screen 
#all the files before the final part 
import sys
from time import sleep

import pygame 

from settings import Settings
from gamestats import Gamestats
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #create an instance that stores game stats 

        self.stats = Gamestats(self)
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                  self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons()




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
         
    
        
    
    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              self._ship_hit()

        #look for alines hitting the bottom of the screen 
         self._check_aliens_bottom()



    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


    def _ship_hit(self):
         """respond to the ship being hit by an alien"""
         if self.stats.ships_left > 0:

         #decrement ships_left
            self.stats.ships_left -= 1

         #get rid of any remaining alienas and bullets 
            self.ufo.empty()
            self.bullets.empty()

         #create a new fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()

         #pause 
            sleep(0.5)

         else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen"""
         screen_rect = self.screen.get_rect()

         for ufo in self.ufo.sprites():
              if ufo.rect.bottom >= screen_rect.bottom:
                   #treat this the same as if the ship got hit 
                   self._ship_hit()
                   break
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

#settings.py 
class Settings():

    def __init__(self):

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
        self.fleet_direction = .5

#ship.py 

import pygame

class Rocketship():

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def _center_ship(self):
        """center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

#BULLETS.py 

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)



    def update(self):
        """move the bullet up the screen """
        #update the decimal postion of the bullet 

        self.y -= self.settings.bullet_speed
        #update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        
        pygame.draw.rect(self.screen, self.color, self.rect)


#ufo.py 

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

#gamestats.py 

class Gamestats:

    """track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize stats """
        #start ai in an active state
        self.game_active = True
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialaize stats that can change durign the game """
        self.ships_left = self.settings.ship_limit

#in this final part we will try to add a play button, so that the player can choose when to start the game
#speeding up the game 
#adding a scoring system
#in the code below we have so far added a play button and got rid of the cursor 
#and have created the button with the button class 
import sys
from time import sleep

import pygame 

from settings import Settings
from gamestats import Gamestats
from button import Playbutton
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #create an instance that stores game stats 

        self.stats = Gamestats(self)
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

        #make play button 
        self.play_button = Playbutton(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos()
                     self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
         """Start the new game when the player clicks Play"""
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.stats.game_active:
              #reset the game stats 
              self.stats.reset_stats()
              self.stats.game_active = True

              #get rid of any remaining aliens and bullets 
              self.ufo.empty()
              self.bullets.empty()

              #create a new fleet 
              self._create_fleet()
              self.ship._center_ship()

              #hide the mouse cursor 
              pygame.mouse.set_visible(False)

         

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons()




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
         
    
        
    
    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              self._ship_hit()

        #look for alines hitting the bottom of the screen 
         self._check_aliens_bottom()



    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


    def _ship_hit(self):
         """respond to the ship being hit by an alien"""
         if self.stats.ships_left > 0:

         #decrement ships_left
            self.stats.ships_left -= 1

         #get rid of any remaining alienas and bullets 
            self.ufo.empty()
            self.bullets.empty()

         #create a new fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()

         #pause 
            sleep(0.5)

         else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen"""
         screen_rect = self.screen.get_rect()

         for ufo in self.ufo.sprites():
              if ufo.rect.bottom >= screen_rect.bottom:
                   #treat this the same as if the ship got hit 
                   self._ship_hit()
                   break
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)
            #draw the play button if the game is inactive 
            if not self.stats.game_active:
                 self.play_button.draw_button()


            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#ships.py 
class Gamestats:

    """track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initialize stats """
        #start ai in an active state
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialaize stats that can change durign the game """
        self.ships_left = self.settings.ship_limit

#button.py 
import pygame.font 
#lets python render text into the screen 


class Playbutton:

    def __init__(self,ai_game, msg):
        """Initialize these button attritbutes """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and propertires of the button 

        self.width, self.height = 200, 50 
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #build the button's rect pbject and center it 
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #the button message needs to be prepped only onece
        self._prep_msg(msg)

    def _prep_msg(self, msg):

        """turn msg into a renderderd image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

#now we want to focus on leveling up 
#making the game more difficult 
#what has changed is the main file and settings file 
#main.py 
import sys
from time import sleep

import pygame 

from settings import Settings
from gamestats import Gamestats
from button import Playbutton
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #create an instance that stores game stats 

        self.stats = Gamestats(self)
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

        #make play button 
        self.play_button = Playbutton(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos()
                     self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
         """Start the new game when the player clicks Play"""
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.stats.game_active:
              
              #reset the game settings 
              self.settings.initialize_dynamic_settings()
              
              #reset the game stats 
              self.stats.reset_stats()
              self.stats.game_active = True

              #get rid of any remaining aliens and bullets 
              self.ufo.empty()
              self.bullets.empty()

              #create a new fleet 
              self._create_fleet()
              self.ship._center_ship()

              #hide the mouse cursor 
              pygame.mouse.set_visible(False)

         

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons()




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
              self.settings.increase_speed()
         
    
        
    
    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              self._ship_hit()

        #look for alines hitting the bottom of the screen 
         self._check_aliens_bottom()



    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


    def _ship_hit(self):
         """respond to the ship being hit by an alien"""
         if self.stats.ships_left > 0:

         #decrement ships_left
            self.stats.ships_left -= 1

         #get rid of any remaining alienas and bullets 
            self.ufo.empty()
            self.bullets.empty()

         #create a new fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()

         #pause 
            sleep(0.5)

         else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen"""
         screen_rect = self.screen.get_rect()

         for ufo in self.ufo.sprites():
              if ufo.rect.bottom >= screen_rect.bottom:
                   #treat this the same as if the ship got hit 
                   self._ship_hit()
                   break
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)
            #draw the play button if the game is inactive 
            if not self.stats.game_active:
                 self.play_button.draw_button()


            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

            

#settigns.py 
    
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
        self.fleet_direction = .5


        #how quickly the game speeds up 
        self.speedup_scale = 1.01

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throguhout the game """

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet direction of 1 represent right, -1 represent left 
        self.fleet_direction = 1 



    def increase_speed(self):
        """Increase speed settimgs"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


#next part is displaying the score 
#for this part we only altered the stats file scoreboard and settings and main 
#we added plenty of things 
#like high score and then resetting the score as well in these files 
import sys
from time import sleep

import pygame 

from settings import Settings
from gamestats import Gamestats
from scoreboard import Scoreboard
from button import Playbutton
from ship import Rocketship
from bullets import Bullet
from ufo import UFO

class AlienInvasion():

    def __init__(self): 

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        #create an instance that stores game stats 
        #and create a scoreboard 

        self.stats = Gamestats(self)
        self.sb = Scoreboard(self)
        self.ship = Rocketship(self)
        self.bullets = pygame.sprite.Group()
        self.ufo = pygame.sprite.Group()

        self._create_fleet()

        #make play button 
        self.play_button = Playbutton(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_ufo()

            for bullet in self.bullets.copy():
                   if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            self._updates_screen()

    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos()
                     self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):

            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
                    
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
         """Start the new game when the player clicks Play"""
         button_clicked = self.play_button.rect.collidepoint(mouse_pos)
         if button_clicked and not self.stats.game_active:
              
              #reset the game settings 
              self.settings.initialize_dynamic_settings()

              #reset the game stats 
              self.stats.reset_stats()
              self.stats.game_active = True
              self.sb.prep_score()

              #get rid of any remaining aliens and bullets 
              self.ufo.empty()
              self.bullets.empty()

              #create a new fleet 
              self._create_fleet()
              self.ship._center_ship()

              #hide the mouse cursor 
              pygame.mouse.set_visible(False)

         

    def _fire_bullet(self):
          """Create a new bullet and add it to the bullets group."""
          if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


    def _update_bullets(self):
         """Update the position of bullets and get rid of old bullets"""
         #update bullet positions.
         self.bullets.update()

         #get rid of bullets that have disaapeasred 
         for bullet in self.bullets.copy():
              if bullet.rect.bottom <= 0:
                   self.bullets.remove(bullet)

         self._check_bullet_alien_collisons()




    def _check_bullet_alien_collisons(self):
         """respond to bullet alien collisions"""

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien
         collisions = pygame.sprite.groupcollide(
             self.bullets, self.ufo, True, True)
         
         if collisions: 
              for ufo in collisions.values():
                   self.stats.score += self.settings.alien_points * len(ufo)                        
              self.sb.prep_score()
              self.sb.check_high_scores()
         
         if not self.ufo:
              #destroy existing bullets and create new fleet.
              self.bullets.empty()
              self._create_fleet()
              self.settings.increase_speed()
         
    
        
    
    def _update_ufo(self):
         """Update the postions of all ufo in the fleet"""
         """Check if the fleet is at the edge, then update the positon of all aliens in the fleet """
         self._check_fleet_edges()
         self.ufo.update()

         #look for alien ship collinsions 
         if pygame.sprite.spritecollideany(self.ship, self.ufo):
              self._ship_hit()

        #look for alines hitting the bottom of the screen 
         self._check_aliens_bottom()



    def _create_fleet(self):
         """Create the fleet of alines """
         #create an aline and find the number of aliens in a row 
         #spacing between each alien is equal to one alien width 

         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         available_spcae_x = self.settings.screen_width - (2 * ufo_width)
         number_aliens_x = available_spcae_x // (2 * ufo_width)

         #Determine the number of rows of aliens that fit on the screen
         ship_height = self.ship.rect.height
         available_spcae_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)

         number_rows = available_spcae_y // (2 * ufo_height)

        #create the full fleet of alines
         #create the first row of aliens 
         for row_number in range(number_rows):
            for ufo_number in range(number_aliens_x):
              self._create_alien(ufo_number, row_number)
    
    def _create_alien(self, ufo_number, row_number):     
         
              #create an alien and place it in the row 
         ufo = UFO(self)
         ufo_width, ufo_height = ufo.rect.size
         
         ufo.x = ufo_width + 2 * ufo_width * ufo_number
         ufo.rect.x = ufo.x
         ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
         self.ufo.add(ufo)


    def _check_fleet_edges(self):
         """respond appropriately if any ufos have reached an edge"""

         for ufo in self.ufo.sprites():
              if ufo.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
         """Drop the entire fleet and change the fleets direction"""
         for ufo in self.ufo.sprites():
              ufo.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1


    def _ship_hit(self):
         """respond to the ship being hit by an alien"""
         if self.stats.ships_left > 0:

         #decrement ships_left
            self.stats.ships_left -= 1

         #get rid of any remaining alienas and bullets 
            self.ufo.empty()
            self.bullets.empty()

         #create a new fleet and center the ship
            self._create_fleet()
            self.ship._center_ship()

         #pause 
            sleep(0.5)

         else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen"""
         screen_rect = self.screen.get_rect()

         for ufo in self.ufo.sprites():
              if ufo.rect.bottom >= screen_rect.bottom:
                   #treat this the same as if the ship got hit 
                   self._ship_hit()
                   break
         
                

    def _updates_screen(self):

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ufo.draw(self.screen)

            #draw the score info
            self.sb.show_score()
            #draw the play button if the game is inactive 
            if not self.stats.game_active:
                 self.play_button.draw_button()


            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


#settings.py 
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
        self.bullet_speed = 3.0
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
        


#gamestats.py 
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

#scoreboards
import pygame.font 

class Scoreboard:
    """A class to report scoring information. """

    def __init__(self,ai_game):

        """Initialize scorekeeping attritbutes """
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
    def check_high_scores(self):
        """check to seee if there is a new high score """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score to the screen"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)


#next part is displaying the levels 




