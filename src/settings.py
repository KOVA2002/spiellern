from pygame.color import THECOLORS


class Settings:
    """A class for storing settings for the game"""
    def __init__(self):
        """"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = THECOLORS['aquamarine']
        self.caption = "Spiellern"
