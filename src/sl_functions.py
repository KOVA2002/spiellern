from pygame.color import THECOLORS
import pygame


# Hero auxiliary functions
def find_surface_below(hero) -> None:

    for surface in hero.all_surfaces:
        if hero.rect.colliderect(surface.rect) and hero.rect.right-hero.fall_margin >= surface.rect.left and hero.rect.left+hero.fall_margin <= surface.rect.right:
            hero.platform = surface
            hero.falling = False
            hero.fallen_wait = hero.fallen_waiting_frames
            hero.reached_falling_speed = hero.falling_speed
            hero.falling_speed = 3
            break


def check_platform(hero) -> None:

    if hero.rect.right-hero.fall_margin < hero.platform.rect.left \
            or hero.rect.left+hero.fall_margin > hero.platform.rect.right:
        hero.platform = None


def update_screen(game) -> None:

    game.screen.blit(game.settings.bg_image, (0, 0))
    pygame.draw.rect(game.screen, (255, 0, 250), game.surface.rect, 0)
    game.rock.blitme()
    game.hero.blitme()
