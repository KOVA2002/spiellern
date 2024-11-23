import json
from random import randint
from cloud import Cloud

with open("learning_data.json", "r") as data_file:
    LEARNING_DATA = json.load(data_file)

# Hero auxiliary functions
def find_surface_below(hero) -> None:

    for surface in hero.all_surfaces:
        if hero.rect.colliderect(surface.rect) \
                and hero.rect.right-hero.fall_margin >= surface.rect.left \
                and hero.rect.left+hero.fall_margin <= surface.rect.right \
                and hero.rect.bottom <= surface.rect.bottom:
            hero.platform = surface
            hero.falling = False
            hero.fallen_wait = hero.fallen_waiting_frames
            hero.reached_falling_speed = hero.falling_speed
            hero.falling_speed = 3
            # if the found surface is a cloud, then mark the current task resolved
            if type(surface.owner_object) is Cloud:
                surface.owner_object.task.resolved = True
                surface.owner_object.task.answer_sound.play()
            break


def check_platform(hero) -> None:

    if hero.rect.right-hero.fall_margin < hero.platform.rect.left \
            or hero.rect.left+hero.fall_margin > hero.platform.rect.right:
        hero.platform = None


def check_approaching_surface(hero) -> int:
    """Return the distance to the closest surface below"""
    distances_to_below_surfaces = []
    for surface in hero.all_surfaces:
        if hero.rect.bottom <= surface.rect.y \
                and hero.rect.right-hero.fall_margin >= surface.rect.left \
                and hero.rect.left+hero.fall_margin <= surface.rect.right:
            distances_to_below_surfaces.append(surface.rect.y - hero.rect.bottom)
    return min(distances_to_below_surfaces)+1


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

    task = LEARNING_DATA[randint(0, len(LEARNING_DATA)-1)]
    return task
