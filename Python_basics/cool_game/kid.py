import pygame

class Young_kid:
    """A class to manage the young kid"""
    def __init__(self,yg_game):
        """Initialize young kid and get its starting position"""
        self.screen = yg_game.screen
        self.screen_rect = yg_game.screen.get_rect()

        """Load the young kid of game and get its rect"""
        self.image = pygame.image.load('images/tuk_tuk.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the Young kid at its current location"""
        self.screen.blit(self.image,self.rect)
