import pygame
from pygame.sprite import Sprite

class Bulllets(Sprite):
    """Class to manage the bullets fired by Ship"""
    def __init__(self, ai_game):
        """Create a bullet at ships current location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color