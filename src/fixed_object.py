import pygame
from surface import Surface


class FixedObject:

    def __init__(self, game, obj_type):
        """A class for immovable objects"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.obj_type = obj_type
        self.supported_types = ['rock', 'water', 'floating_rock', 'flag']

        try:
            if self.obj_type == 'rock':
                self.image = pygame.image.load('img/fixed_objects/rock1.png')
                self.surface_depth = 50
            elif self.obj_type == 'floating_rock':
                self.image = pygame.image.load('img/fixed_objects/floating_rock1.png')
                self.surface_depth = 20
            elif self.obj_type == 'flag':
                self.image = pygame.image.load('img/fixed_objects/flag.png')
            else:
                raise ValueError(f'Object type must be in {self.supported_types}')
        except ValueError as e:
            print('Error: ', e)

        self.rect = self.image.get_rect()

        # Every new object appears on specified coordinates
        if self.obj_type == 'rock':
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.left = self.screen_rect.x
        elif self.obj_type == 'floating_rock':
            self.rect.x = self.screen_rect.right-self.rect.width/2
            self.rect.y = 100
        elif self.obj_type == 'flag':
            self.rect.right = self.screen_rect.right-20
            self.rect.y = 20

        # Adding surface object
        if self.obj_type in ['rock', 'floating_rock']:
            self.surface = Surface((self.rect.x, self.rect.y+self.surface_depth), (self.rect.width, game.settings.surface_height), self)
            # adding the newly created object to the list containing all surfaces of the game
            game.all_surfaces.append(self.surface)
        else:
            self.surface = None

    def blitme(self):
        """Draw object"""

        self.screen.blit(self.image, self.rect)
        if self.surface:
            self.surface.update_position(self.rect.x, self.rect.y+self.surface_depth)
        # TODO: Remove this line after jumping and landing on surface is implemented
        #pygame.draw.rect(self.screen, (255, 0, 250), self.surface.rect, 0)
