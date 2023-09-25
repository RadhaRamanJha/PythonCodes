import sys
import pygame

from setting import Settings
from kid import Young_kid

class Kid:
    """Overall class to manage game asset and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Young Kid on foot")
        self.kid = Young_kid(self)

    def run_game(self):
        """starts the main loop of game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to movement of keyboard and mouse action"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    
    def _update_screen(self):
            """Update the images on screen and flip to the new screen"""
            self.screen.fill(self.settings.bg_colour)
            self.kid.blitme()
            pygame.display.flip()



if __name__ == "__main__":
    yg = Kid()
    yg.run_game()