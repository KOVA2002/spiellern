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

    placeholders = [("Bild", (("der", False), ("das", True), ("die", False)), "picture", 'sound/das_Bild.mp3'),
                    ("Fisch", (("der", True), ("das", False), ("die", False)), "fish", 'sound/der_Fisch.mp3'),
                    ("Banane", (("der", False), ("das", False), ("die", True)), "banana", 'sound/die_Banane.mp3'),
                    ("Wein", (("der", True), ("das", False), ("die", False)), "wine", 'sound/der_Wein.mp3'),
                    ("Zucker", (("der", True), ("das", False), ("die", False)), "sugar", 'sound/der_Zucker.mp3'),
                    ("Fenster", (("der", False), ("das", True), ("die", False)), "window", 'sound/das_Fenster.mp3'),
                    ("Kartoffel", (("der", False), ("das", False), ("die", True)), "potato", 'sound/die_Kartoffel.mp3'),
                    ("Wurst", (("der", False), ("das", False), ("die", True)), "sausage", 'sound/die_Wurst.mp3'),
                    ("Milch", (("der", False), ("das", False), ("die", True)), "milk", 'sound/die_Milch.mp3'),
                    ("Butter", (("der", False), ("das", False), ("die", True)), "butter", 'sound/die_Butter.mp3'),
                    ("Zitrone", (("der", False), ("das", False), ("die", True)), "lemon", 'sound/die_Zitrone.mp3'),
                    ("Tasse", (("der", False), ("das", False), ("die", True)), "cup", 'sound/die_Tasse.mp3'),
                    ("Suppe", (("der", False), ("das", False), ("die", True)), "soup", 'sound/die_Suppe.mp3'),
                    ("Brot", (("der", False), ("das", True), ("die", False)), "bread", 'sound/das_Brot.mp3'),
                    ("Bier", (("der", False), ("das", True), ("die", False)), "beer", 'sound/das_Bier.mp3'),
                    ("Mineralwasser", (("der", False), ("das", True), ("die", False)), "Mineral water", 'sound/das_Mineralwasser.mp3'),
                    ("Kaffee", (("der", True), ("das", False), ("die", False)), "coffee", 'sound/der_Kaffee.mp3'),
                    ("Fleisch", (("der", False), ("das", True), ("die", False)), "meat", 'sound/das_Fleisch.mp3'),
                    ("Saft", (("der", True), ("das", False), ("die", False)), "juice", 'sound/der_Saft.mp3'),
                    ("Teller", (("der", True), ("das", False), ("die", False)), "plate", 'sound/der_Teller.mp3'),
                    ]
    placeholder = placeholders[randint(0, len(placeholders)-1)]
    # TODO: Implement getting the task from the yaml file.
    return placeholder
