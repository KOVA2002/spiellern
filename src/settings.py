import pygame
from pygame.color import THECOLORS


class Settings:
    """A class for storing settings for the game"""
    def __init__(self):
        """"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('img/bg_images/bg_mountains.jpg')
        self.bg_color = THECOLORS['skyblue']
        self.caption = "Spiellern"

        # hero settings
        self.hero_img_upd_rate = 8
        self.hero_running_speed = 3
        self.hero_falling_speed = 3.0
        self.hero_falling_acceleration_rate = 0.15
        self.hero_fallen_waiting_frames = 12
        self.hero_platform_fall_margin = 25
        self.hero_jumping_frames_default = 30
        self.hero_jumping_vertical_velocity = 5
        self.hero_left_right_shift_in_air = 3
        self.hero_falling_middle_speed_from = 4
        self.hero_falling_high_speed_from = 8
        self.hero_fallen_middle_waiting_from = 8
        self.hero_fallen_long_waiting_from = 10
