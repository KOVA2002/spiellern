# TODO: Add classes: Cloud, TaskBoard, Plank, LearningData
# TODO: Refactor classes: Hero
# TODO: Add jumping for Hero
# TODO: Update Settings
# TODO: Add statistics

import pygame
import sys
from sl_functions import update_screen
from settings import Settings
from hero import Hero


class Spiellern:
    """Game class"""

    def __init__(self):
        """Create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.hero = Hero(self)
        pygame.display.set_caption(self.settings.caption)
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
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move hero to the right
                    self.hero.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move hero to the left
                    self.hero.moving_left = True

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
