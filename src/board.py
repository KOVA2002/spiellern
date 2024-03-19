import pygame
from pygame.color import THECOLORS


class Board:

    def __init__(self, game):

        self.screen = game.screen
        self.image = pygame.image.load('img/boards/board1.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.font_color = THECOLORS['darkgreen']
        self.font = pygame.font.SysFont('couriernew', 40, bold=True, italic=True)
        self.font_text = self.font.render('text', True, self.font_color)
        self.font_position = (self.rect.centerx - self.font_text.get_width() / 2,
                              self.rect.centery - self.font_text.get_height() / 2)

    def update_text(self, text):

        self.font_text = self.font.render(text, True, self.font_color)
        self.font_position = (self.rect.centerx - self.font_text.get_width() / 2,
                              self.rect.centery - self.font_text.get_height() / 2)

    def blitme(self):

        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.font_text, self.font_position)
