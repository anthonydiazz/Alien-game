
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
              self.sb.prep_level()
              self.sb.prep_ships()

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

              #increase level
              self.stats.level += 1 
              self.sb.prep_level()
         
    
        
    
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
            self.sb.prep_ships()

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

            




        








        