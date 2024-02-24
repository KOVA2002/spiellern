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
