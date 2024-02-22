import pygame


class Hero:
    """A class for controlling main character"""
    def __init__(self, game):
        """Create a hero and set their position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # Load hero image and make a rectangular out of it
        self.image = pygame.image.load('img/hero/hero_stands_r1.png')
        self.rect = self.image.get_rect()
        # Every new hero starts from the specified coordinates

        self.rect.midbottom = (100, 200)

        # Flag of movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update hero's position"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw hero in the current position"""
        self.update()
        self.screen.blit(self.image, self.rect)