from random import randint
from cloud import Cloud


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

    placeholders = [("Bild\npicture", (("der", False), ("das", True), ("die", False))),
                    ("Fisch\nfish", (("der", True), ("das", False), ("die", False))),
                    ("Banane\nbanana", (("der", False), ("das", False), ("die", True))),
                    ("Wein\nwine", (("der", True), ("das", False), ("die", False))),
                    ("Zucker\nsugar", (("der", True), ("das", False), ("die", False))),
                    ("Fenster\nwindow", (("der", False), ("das", True), ("die", False))),
                    ("Kartoffel\npotato", (("der", False), ("das", False), ("die", True))),
                    ("Wurst\nsausage", (("der", False), ("das", False), ("die", True))),
                    ("Milch\nmilk", (("der", False), ("das", False), ("die", True))),
                    ("Butter\nbutter", (("der", False), ("das", False), ("die", True))),
                    ("Zitrone\nlemon", (("der", False), ("das", False), ("die", True))),
                    ("Tasse\ncup", (("der", False), ("das", False), ("die", True))),
                    ("Suppe\nsoup", (("der", False), ("das", False), ("die", True))),
                    ("Brot\nbread", (("der", False), ("das", True), ("die", False))),
                    ("Bier\nbeer", (("der", False), ("das", True), ("die", False))),
                    ("Mineralwasser\nMineral water", (("der", False), ("das", True), ("die", False))),
                    ("Kaffee\ncoffee", (("der", True), ("das", False), ("die", False))),
                    ("Fleisch\nmeat", (("der", False), ("das", True), ("die", False))),
                    ("Saft\njuice", (("der", True), ("das", False), ("die", False))),
                    ("Teller\nplate", (("der", True), ("das", False), ("die", False))),
                    ]
    placeholder = placeholders[randint(0, len(placeholders)-1)]
    # TODO: Implement getting the task from the yaml file.
    return placeholder
