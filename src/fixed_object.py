import pygame
from surface import Surface


class FixedObject:

    def __init__(self, game, type):
        """A class for immovable objects"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.type = type
        self.supported_types = ['rock', 'water']

        try:
            if type == 'rock':
                self.image = pygame.image.load('img/fixed_objects/rock1.png')
                self.surface_depth = 50
            else:
                raise ValueError(f"Type should be in {self.supported_types}")
        except ValueError as e:
            print('Error: ', e)

        self.rect = self.image.get_rect()

        # Every new hero starts from the specified coordinates
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.left = self.screen_rect.x

        # Adding surface object
        self.surface = Surface((self.rect.x, self.rect.y+self.surface_depth), (self.rect.width, 10), self)
        # adding the newly created object to the list containing all surfaces of the game
        game.all_surfaces.append(self.surface)

    def blitme(self):
        """Draw object"""

        self.screen.blit(self.image, self.rect)
        self.surface.update_position(self.rect.x, self.rect.y+self.surface_depth)
        # TODO: Remove this line after jumping and landing on surface is implemented
        pygame.draw.rect(self.screen, (255, 0, 250), self.surface.rect, 0)
