# TODO: Refactor the Cloud and Task classes
# TODO: Add statistics, i.e. the number of correctly identified items vs the number of mistakes; output color-coded items
# TODO: Finish the level once the hero reaches the flag; then display stats
# TODO: Implement start menu with options where the user can choose a topic to learn; start the game when the user presses a specific key
# TODO: Add more learning data

import pygame
import sys
from upper_level_functions import update_screen
from settings import Settings
from hero import Hero
from fixed_object import FixedObject
from surface import Surface
from task import Task
from board import Board


class Spiellern:
    """Game class"""

    def __init__(self):
        """Create game resources"""
        pygame.init()
        pygame.mixer.init()

        # add screen and setting objects
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings = Settings()
        pygame.display.set_caption(self.settings.caption)

        # adjust settings
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.bg_image = pygame.transform.scale(self.settings.bg_image, (self.settings.screen_width, self.settings.screen_height))

        # adjust background music; play it in unlimited loop
        self.bg_music = pygame.mixer.Sound('sound/Rosamunde.mp3')
        self.bg_music.set_volume(0.05)
        self.bg_music.play(loops=-1)

        # introducing a list for storing all surfaces in the game
        self.all_surfaces = []

        # add bottom surface
        self.surface = Surface((0, 0+self.settings.screen_height-10), (self.settings.screen_width, 10), self)
        self.all_surfaces.append(self.surface)

        # add hero and fixed objects
        self.hero = Hero(self)
        self.board = Board(self)
        self.rock = FixedObject(self, 'rock')
        self.floating_rock = FixedObject(self, 'floating_rock')
        self.finish_flag = FixedObject(self, 'flag')
        self.task_list = [Task(self, 1),]

        # add clock to maintain the number of frames per second
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start main game loop"""

        while True:
            # Checking mouse/keyboard events
            self._check_events()

            # Displaying last drawn screen
            update_screen(self)
            pygame.display.flip()
            self.clock.tick(100)

    def _check_events(self):
        """Checking mouse/keyboard events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
             (event.type == pygame.KEYDOWN and event.key in (pygame.K_q, pygame.K_ESCAPE)):
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move hero to the right
                    self.hero.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move hero to the left
                    self.hero.moving_left = True
                elif event.key == pygame.K_UP:
                    if self.hero.platform:
                        self.hero.jumping = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # stop moving right
                    self.hero.moving_right = False
                    self.hero.stop_moving_right = True
                elif event.key == pygame.K_LEFT:
                    # stop moving left
                    self.hero.moving_left = False
                    self.hero.stop_moving_left = True


if __name__ == '__main__':
    pass
    # Create game instance and start the game
    sl = Spiellern()
    sl.run_game()
