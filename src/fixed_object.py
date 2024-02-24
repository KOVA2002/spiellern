import pygame


class FixedObject:

    def __init__(self, game, type):
        """A class for immovable objects"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.supported_types = ['rock', 'water']
        try:
            if type == 'rock':
                self.image = pygame.image.load('img/fixed_objects/rock1.png')
            else:
                raise ValueError(f"Type should be in {self.supported_types}")
        except ValueError as e:
            print('Error: ', e)
        self.rect = self.image.get_rect()
        # Every new hero starts from the specified coordinates
        print(dir(self.screen_rect))
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.left = self.screen_rect.x

    def blitme(self):
        """Draw object"""

        self.screen.blit(self.image, self.rect)
