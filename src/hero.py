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

        # Load hero image and make a rectangular out of it
        self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'stands_r0')
        self.rect = self.image[0].get_rect()

        # Every new hero starts from the specified coordinates
        self.rect.midbottom = self.screen_rect.midbottom

        # adjust image update
        self.img_upd_counter = 0
        self.img_upd_rate = game.settings.hero_img_upd_rate

        self.running_speed = game.settings.hero_running_speed

        # Flag of movement
        self.moving_right = False
        self.moving_left = False
        self.stop_moving_right = False
        self.stop_moving_left = False

    def _update_image(self):

        img_type = self.image[1][0:-1]
        img_number = int(self.image[1][-1])

        # first, check if the hero stops moving
        if self.stop_moving_right:
            self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'stands_r0')
            self.stop_moving_right = False
        elif self.stop_moving_left:
            self.image = (pygame.image.load('img/hero/hero_stands_l1.png'), 'stands_l0')
            self.stop_moving_left = False

        # update image for running right
        elif self.moving_right:
            if img_type == 'runs_r' and img_number < 5:
                self.image = (self.run_right[img_number+1], 'runs_r'+str(img_number+1))
            else:
                self.image = (self.run_right[0], 'runs_r0')

        # update image for running left
        elif self.moving_left:
            if img_type == 'runs_l' and img_number < 5:
                self.image = (self.run_left[img_number + 1], 'runs_l' + str(img_number + 1))
            else:
                self.image = (self.run_left[0], 'runs_l0')

    def update(self):
        """Update hero's position"""
        if self.moving_left and self.moving_right:
            self.stop_moving_right = True
        elif self.moving_right:
            self.rect.x += self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        elif self.moving_left:
            self.rect.x -= self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        if self.img_upd_counter == self.img_upd_rate-1 \
                or self.stop_moving_right or self.stop_moving_left:
            self._update_image()


    def blitme(self):
        """Draw hero in the current position"""

        self.update()
        self.screen.blit(self.image[0], self.rect)
