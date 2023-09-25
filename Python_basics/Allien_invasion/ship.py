import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
          
        # Load the ship image and and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at the bottom center of the screen
        self.screen_rect = ai_game.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of ship based on the movement Flag"""
        # update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        # using if for left movement also rather than elif because that will right movement
        # when both keys are placed together

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,self.rect)
