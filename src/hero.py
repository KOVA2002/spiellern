import pygame


class Hero:
    """A class for controlling main character"""
    def __init__(self, game):
        """Create a hero and set their position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # Load hero image and make a rectangular out of it
        self.run_right = [pygame.image.load(f'img/hero/hero_runs_r{i}.png') for i in range(6)]
        self.run_left = [pygame.image.load(f'img/hero/hero_runs_l{i}.png') for i in range(6)]

        #print(len(self.run_right))
        #print(len(self.run_left))
        # Load hero image and make a rectangular out of it
        self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'r0')
        self.rect = self.image[0].get_rect()

        # Every new hero starts from the specified coordinates
        self.rect.midbottom = self.screen_rect.midbottom

        self.image_update_counter = 0

        # Flag of movement
        self.moving_right = False
        self.moving_left = False
        self.stop_moving_right = False
        self.stop_moving_left = False

    def _update_image(self):

        # update image for running right
        if self.moving_right:
            if self.image[1] == 'r0':
                self.image = (self.run_right[1], 'r1')
            elif self.image[1] == 'r1':
                self.image = (self.run_right[2], 'r2')
            elif self.image[1] == 'r2':
                self.image = (self.run_right[3], 'r3')
            elif self.image[1] == 'r3':
                self.image = (self.run_right[4], 'r4')
            elif self.image[1] == 'r4':
                self.image = (self.run_right[5], 'r5')
            else:
                self.image = (self.run_right[0], 'r0')

        # update image for running left
        elif self.moving_left:
            if self.image[1] == 'l0':
                self.image = (self.run_left[1], 'l1')
            elif self.image[1] == 'l1':
                self.image = (self.run_left[2], 'l2')
            elif self.image[1] == 'l2':
                self.image = (self.run_left[3], 'l3')
            elif self.image[1] == 'l3':
                self.image = (self.run_left[4], 'l4')
            elif self.image[1] == 'l4':
                self.image = (self.run_left[5], 'l5')
            else:
                self.image = (self.run_left[0], 'l0')
        elif self.stop_moving_right:
            self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'r0')
            self.stop_moving_right = False
        elif self.stop_moving_left:
            self.image = (pygame.image.load('img/hero/hero_stands_l1.png'), 'l0')
            self.stop_moving_left = False

    def update(self):
        """Update hero's position"""
        if self.moving_right:
            self.rect.x += 3
            self.image_update_counter = (self.image_update_counter + 1) % 8
        if self.moving_left:
            self.rect.x -= 3
            self.image_update_counter = (self.image_update_counter + 1) % 8
        if self.image_update_counter == 7 or self.stop_moving_right or self.stop_moving_left:
            self._update_image()

    def blitme(self):
        """Draw hero in the current position"""

        self.update()
        self.screen.blit(self.image[0], self.rect)
