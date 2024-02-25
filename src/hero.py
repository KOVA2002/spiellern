import pygame
from math import floor
from sl_functions import find_surface_below


class Hero:
    """A class for controlling main character"""
    def __init__(self, game):
        """Create a hero and set their position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # Load hero image and make a rectangular out of it
        self.img_run_r = [pygame.image.load(f'img/hero/hero_runs_r{i}.png') for i in range(6)]
        self.img_run_l = [pygame.image.load(f'img/hero/hero_runs_l{i}.png') for i in range(6)]

        # Load hero image and make a rectangular out of it
        self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'stands_r0')
        self.rect = self.image[0].get_rect()

        # Every new hero starts from the specified coordinates
        self.rect.left = self.screen_rect.left
        self.rect.y = 300

        # adjust image update
        self.img_upd_counter = 0
        self.img_upd_rate = game.settings.hero_img_upd_rate

        self.running_speed = game.settings.hero_running_speed

        # Flags of left/right movement
        self.moving_right = False
        self.moving_left = False
        self.stop_moving_right = False
        self.stop_moving_left = False

        # falling
        self.falling = False
        self.falling_speed = game.settings.hero_falling_speed
        self.falling_acceleration_rate = game.settings.hero_falling_acceleration_rate
        self.fallen_waiting_frames = game.settings.hero_fallen_waiting_frames
        self.fallen_wait = 0
        self.platform = None

    def _update_image(self):

        img_type = self.image[1][0:-1]
        img_number = int(self.image[1][-1])

        # first, check if if hero has already fallen
        if self.fallen_wait > 0:
            self.image = (pygame.image.load('img/hero/hero_falls_r3.png'), 'falls_r3')
            self.fallen_wait -= 1
        # check if hero is falling
        elif self.falling:
            if img_type.endswith('r'):
                self.image = (pygame.image.load('img/hero/hero_falls_r1.png'), 'falls_r1')
            else:
                self.image = (pygame.image.load('img/hero/hero_falls_l1.png'), 'falls_l1')
        # then, check if the hero stops moving left or right
        elif self.stop_moving_right:
            self.image = (pygame.image.load('img/hero/hero_stands_r1.png'), 'stands_r0')
            self.stop_moving_right = False
        elif self.stop_moving_left:
            self.image = (pygame.image.load('img/hero/hero_stands_l1.png'), 'stands_l0')
            self.stop_moving_left = False

        # update image for running right
        elif self.moving_right:
            if img_type == 'runs_r' and img_number < 5:
                self.image = (self.img_run_r[img_number+1], 'runs_r'+str(img_number+1))
            else:
                self.image = (self.img_run_r[0], 'runs_r0')

        # update image for running left
        elif self.moving_left:
            if img_type == 'runs_l' and img_number < 5:
                self.image = (self.img_run_l[img_number + 1], 'runs_l' + str(img_number + 1))
            else:
                self.image = (self.img_run_l[0], 'runs_l0')

    def update(self):
        """Update hero's position"""
        # updating falling
        if not self.platform and self.rect.bottom > self.screen_rect.bottom - 6:
            self.platform = 'screen_bottom'
            self.falling = False
            self.fallen_wait = self.fallen_waiting_frames
            self.falling_speed = 3
        elif not self.platform:
            surface = find_surface_below(self)
            if surface:
                self.platform = surface
                self.fallen_wait = self.fallen_waiting_frames
                self.falling_speed = 3
        if not self.platform:
            self.falling = True
            self.rect.y += floor(self.falling_speed)
            self.falling_speed += self.falling_acceleration_rate
        # updating left/right movement flags
        elif self.moving_left and self.moving_right:
            self.stop_moving_right = True
        elif self.moving_right:
            self.rect.x += self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        elif self.moving_left:
            self.rect.x -= self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        # updating image
        if self.img_upd_counter == self.img_upd_rate-1 \
                or self.stop_moving_right or self.stop_moving_left or self.falling or self.fallen_wait > 0:
            self._update_image()

    def blitme(self):
        """Draw hero in the current position"""

        self.update()
        self.screen.blit(self.image[0], self.rect)
