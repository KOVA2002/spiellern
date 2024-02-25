from pygame.color import THECOLORS
import pygame


def find_surface_below(hero):
    pass


def update_screen(game):

    game.screen.blit(game.settings.bg_image, (0, 0))
    game.rock.blitme()
    game.hero.blitme()
    #pygame.draw.rect(game.screen, (255, 0, 0), game.rock.surface.rect, 0)