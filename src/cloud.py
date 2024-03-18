import pygame
from pygame.sprite import Sprite
from surface import Surface


class Cloud(Sprite):

    def __init__(self, game, cloud_type: str, line_number: int, cloud_text: str, true_cloud: bool):

        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.cloud_speed = game.settings.cloud_speed
        self.cloud_type = cloud_type
        self.supported_types = game.settings.cloud_types
        self.text = cloud_text
        self.true_answer = true_cloud
        self.moving_direction = 'left'
        self.shift = game.settings.cloud_surface_shift
        try:
            if cloud_type in self.supported_types:
                self.image = pygame.image.load(f'img/clouds/{cloud_type}.png')
                # TODO: Adjust the depth of each cloud and move this parameter to settings
                self.surface_depth = 132
            else:
                raise ValueError(f'Cloud type must be in {self.supported_types}')
        except ValueError as e:
            print('Error:', e)

        self.rect = self.image.get_rect()

        # Every new object appears on specified coordinates
        self.rect.left = self.screen_rect.right - 50
        self.rect.y = game.settings.screen_height - 100 - (250*line_number)

        # TODO: Rewrite the code below
        if self.true_answer:
            # Adding surface object
            self.surface = Surface((self.rect.x+self.shift, self.rect.y + self.surface_depth), (game.settings.cloud_surface_width, game.settings.surface_height), self)
            # adding the newly created object to the list containing all surfaces of the game
            game.all_surfaces.append(self.surface)
        else:
            self.surface = None

    def update(self):
        """"""

        self.rect.x -= self.cloud_speed
        if self.surface:
            self.surface.update_position(self.rect.x+self.shift, self.rect.y + self.surface_depth)
        self.blitme()

    def blitme(self):
        """Draw object"""

        self.screen.blit(self.image, self.rect)
        if self.surface:
            # TODO: Remove this line after jumping and landing on surface is implemented
            pygame.draw.rect(self.screen, (255, 0, 250), self.surface.rect, 0)
