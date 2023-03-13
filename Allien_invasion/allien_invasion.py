import sys 
# tools avialable in sys module will be used to exit game when user quits

import pygame 
# pygame contains the functionality we need to make a game

from settings import Settings
from ship import Ship

class AllienInvasion:
    """Overall class to manage game asset and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        # pygame.init() initializes the background and settings that pygame needs to work properly
        self.settings = Settings()
    # pygame.display.set_mode() is used to create a display window, on which we draw all game graphical elements     
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Allien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()         

    def _check_events(self):
        """Respond to Keyboard and Mouse Events"""
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Respond to KEY press"""
        if event.key == pygame.K_RIGHT:
            # moving the ship to right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # moving the ship to left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Respond to KEY release"""
        if event.key == pygame.K_RIGHT:
            # restricting ship movement to right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # restricting ship movement to left
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()   
        pygame.display.flip()
         

if __name__ == "__main__":
    """Makes a game instance and run the game"""
    ai = AllienInvasion()
    ai.run_game()