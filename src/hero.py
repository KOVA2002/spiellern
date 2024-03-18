import pygame
from math import floor
from sl_functions import check_moving_lr_in_air, check_platform, find_surface_below
from cloud import Cloud


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
        self.reached_falling_speed = 0
        self.falling_acceleration_rate = game.settings.hero_falling_acceleration_rate
        self.fallen_waiting_frames = game.settings.hero_fallen_waiting_frames
        self.fallen_wait = 0
        self.all_surfaces = game.all_surfaces
        self.platform = None
        self.fall_margin = game.settings.hero_platform_fall_margin
        self.left_right_shift_in_air = game.settings.hero_left_right_shift_in_air
        self.falling_middle_speed_from = game.settings.hero_falling_middle_speed_from
        self.falling_high_speed_from = game.settings.hero_falling_high_speed_from
        self.fallen_middle_waiting_from = game.settings.hero_fallen_middle_waiting_from
        self.fallen_long_waiting_from = game.settings.hero_fallen_long_waiting_from

        # jumping
        self.jumping = False
        self.jumping_frames = 0
        self.jumping_frames_default = game.settings.hero_jumping_frames_default
        self.jumping_vertical_velocity = game.settings.hero_jumping_vertical_velocity

    def _get_image_type(self, img_direction, base, number) -> str:
        """Returns image type of proper direction"""

        image_type = ''
        if self.moving_right:
            image_type = base+'_r'+number
        elif self.moving_left:
            image_type = base+'_l'+number
        elif img_direction == 'r':
            image_type = base+'_r'+number
        else:
            image_type = base+'_l'+number
        return image_type

    def _update_image(self):

        img_type = self.image[1][0:-1]
        img_number = int(self.image[1][-1])
        img_direction = img_type[-1]
        new_img_type = None

        # first, check if hero has already fallen
        if self.fallen_wait > 0:
            if img_direction == 'r':
                if self.reached_falling_speed > self.fallen_long_waiting_from:
                    new_img_type = 'falls_r3'
                elif self.reached_falling_speed > self.fallen_middle_waiting_from:
                    new_img_type = 'falls_r2'
                else:
                    new_img_type = 'jumps_r3'
            else:
                if self.reached_falling_speed > self.fallen_long_waiting_from:
                    new_img_type = 'falls_l3'
                elif self.reached_falling_speed > self.fallen_middle_waiting_from:
                    new_img_type = 'falls_l2'
                else:
                    new_img_type = 'jumps_l3'
            self.fallen_wait -= 1
        # check if hero is falling
        elif self.falling:
            if self.falling_speed > self.falling_high_speed_from:
                new_img_type = self._get_image_type(img_direction, 'falls', '1')
            elif self.falling_speed > self.falling_middle_speed_from:
                new_img_type = self._get_image_type(img_direction, 'jumps', '3')
            else:
                new_img_type = self._get_image_type(img_direction, 'jumps', '2')

        # jumping
        elif self.jumping:
            new_img_type = self._get_image_type(img_direction, 'jumps', '1')

        # then, check if the hero stops moving left or right
        elif self.stop_moving_right:
            new_img_type = 'stands_r1'
            self.stop_moving_right = False
        elif self.stop_moving_left:
            new_img_type = 'stands_l1'
            self.stop_moving_left = False

        # update image for running right
        elif self.moving_right:
            if img_type == 'runs_r' and img_number < 5:
                new_img_type = 'runs_r'+str(img_number+1)
            else:
                new_img_type = 'runs_r0'

        # update image for running left
        elif self.moving_left:
            if img_type == 'runs_l' and img_number < 5:
                new_img_type = 'runs_l' + str(img_number + 1)
            else:
                new_img_type = 'runs_l0'
        if new_img_type:
            self.image = (pygame.image.load(f'img/hero/hero_{new_img_type}.png'), new_img_type)

    def update(self):
        """Update hero's position"""
        # update platform information
        if not self.jumping:
            if not self.platform:
                find_surface_below(self)
            else:
                check_platform(self)
        # falling
        if not self.platform and not self.jumping:
            self.falling = True
            self.rect.y += floor(self.falling_speed)
            self.falling_speed += self.falling_acceleration_rate
            # moving left-right while in air
            check_moving_lr_in_air(self)

        # jumping
        elif self.jumping:
            if self.jumping_frames == 0:
                self.jumping_frames = self.jumping_frames_default
                self.platform = None
            self.rect.y -= self.jumping_vertical_velocity
            self.jumping_frames -= 1
            if self.jumping_frames == 0:
                self.jumping = None
            # moving left-right while in air
            check_moving_lr_in_air(self)

        # updating left/right movement flags
        elif self.moving_left and self.moving_right:
            self.stop_moving_right = True
        #TODO: Implement running being on moving platform
        elif self.moving_right and not self.rect.right >= self.screen_rect.right:
            self.rect.x += self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        elif self.moving_left and not self.rect.x <= 0:
            self.rect.x -= self.running_speed
            self.img_upd_counter = (self.img_upd_counter + 1) % self.img_upd_rate
        # standing on moving platform
        elif self.platform and type(self.platform.owner_object) is Cloud:
            if self.platform.owner_object.moving_direction == 'left' and not self.rect.x <= 0:
                self.rect.x -= self.platform.owner_object.cloud_speed
            elif self.platform.owner_object.moving_direction == 'right' and not self.rect.right >= self.screen_rect.right:
                self.rect.x += self.platform.owner_object.cloud_speed
        # updating image
        if self.img_upd_counter == self.img_upd_rate-1 \
                or self.stop_moving_right or self.stop_moving_left \
                or self.falling or self.fallen_wait > 0 or self.jumping:
            self._update_image()

    def blitme(self):
        """Draw hero in the current position"""

        self.update()
        self.screen.blit(self.image[0], self.rect)
