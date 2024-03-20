import pygame
from pygame.color import THECOLORS


class Board:

    def __init__(self, game):

        self.screen = game.screen
        self.image = pygame.image.load('img/boards/board1.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.font_orig_color = THECOLORS['darkgreen']
        self.font_translation_color = THECOLORS['grey50']
        self.font = pygame.font.SysFont('couriernew', 40, bold=True, italic=True)
        self.font_text_orig = self.font.render('original', True, self.font_orig_color)
        self.font_position_orig = (self.rect.centerx - self.font_text_orig.get_width() / 2,
                                   self.rect.centery - self.font_text_orig.get_height() / 2)
        self.font_text_translation = self.font.render('translation', True, self.font_translation_color)
        self.font_position_translation = (self.rect.centerx - self.font_text_translation.get_width() / 2,
                                          self.rect.centery + self.font_text_orig.get_height() / 2)

    def update_text(self, text, translation=''):

        self.font_text_orig = self.font.render(text, True, self.font_orig_color)
        self.font_position_orig = (self.rect.centerx - self.font_text_orig.get_width() / 2,
                                   self.rect.centery - self.font_text_orig.get_height() / (1 if translation else 2))
        self.font_text_translation = self.font.render(translation, True, self.font_translation_color)
        self.font_position_translation = (self.rect.centerx - self.font_text_translation.get_width() / 2,
                                          self.rect.centery + (0 if translation else self.font_text_orig.get_height() / 2))

    def blitme(self):

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.font_text_orig, self.font_position_orig)
        self.screen.blit(self.font_text_translation, self.font_position_translation)
