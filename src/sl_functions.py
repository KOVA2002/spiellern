from pygame.color import THECOLORS
import pygame
from random import randint

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


def check_moving_lr_in_air(hero):
    if hero.moving_left and not hero.rect.x <= 0:
        hero.rect.x -= hero.left_right_shift_in_air
    if hero.moving_right and not hero.rect.right >= hero.screen_rect.right:
        hero.rect.x += hero.left_right_shift_in_air


# task related functions
def get_cloud_type(task):
    """"""
    # TODO: rerwrite this function in order not to get the same type immediately
    random_type = randint(0, len(task.cloud_types)-1)
    return task.cloud_types[random_type]


def get_random_task() -> tuple:
    """Get a random task from the existing data"""

    placeholder = ("Bild", (("der", False), ("das", True), ("die", False)))
    # TODO: Implement getting the task from the yaml file.
    return placeholder


# general
def update_screen(game) -> None:

    game.screen.blit(game.settings.bg_image, (0, 0))
    pygame.draw.rect(game.screen, (255, 0, 250), game.surface.rect, 0)
    game.rock.blitme()
    game.task.update()
    game.hero.blitme()
