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

    placeholders = [("Bild", (("der", False), ("das", True), ("die", False)), "picture"),
                    ("Fisch", (("der", True), ("das", False), ("die", False)), "fish"),
                    ("Banane", (("der", False), ("das", False), ("die", True)), "banana"),
                    ("Wein", (("der", True), ("das", False), ("die", False)), "wine"),
                    ("Zucker", (("der", True), ("das", False), ("die", False)), "sugar"),
                    ("Fenster", (("der", False), ("das", True), ("die", False)), "window"),
                    ("Kartoffel", (("der", False), ("das", False), ("die", True)), "potato"),
                    ("Wurst", (("der", False), ("das", False), ("die", True)), "sausage"),
                    ("Milch", (("der", False), ("das", False), ("die", True)), "milk"),
                    ("Butter", (("der", False), ("das", False), ("die", True)), "butter"),
                    ("Zitrone", (("der", False), ("das", False), ("die", True)), "lemon"),
                    ("Tasse", (("der", False), ("das", False), ("die", True)), "cup"),
                    ("Suppe", (("der", False), ("das", False), ("die", True)), "soup"),
                    ("Brot", (("der", False), ("das", True), ("die", False)), "bread"),
                    ("Bier", (("der", False), ("das", True), ("die", False)), "beer"),
                    ("Mineralwasser", (("der", False), ("das", True), ("die", False)), "Mineral water"),
                    ("Kaffee", (("der", True), ("das", False), ("die", False)), "coffee"),
                    ("Fleisch", (("der", False), ("das", True), ("die", False)), "meat"),
                    ("Saft", (("der", True), ("das", False), ("die", False)), "juice"),
                    ("Teller", (("der", True), ("das", False), ("die", False)), "plate"),
                    ]
    placeholder = placeholders[randint(0, len(placeholders)-1)]
    # TODO: Implement getting the task from the yaml file.
    return placeholder
