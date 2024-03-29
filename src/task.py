import pygame
from cloud import Cloud
from sl_functions import get_cloud_type, get_random_task

class Task:

    def __init__(self, game, line_number):

        self.task_text, self.answers, self.translation, self.answer_sound_location = get_random_task()
        self.answer_clouds = pygame.sprite.Group()
        self.cloud_types = game.settings.cloud_types
        self.waiting_frames = 100
        self.prev_answer = 0
        self.answers_count = len(self.answers)
        self.line_number = line_number
        self.game = game
        self.game.board.update_text(self.task_text, f'({self.translation})')
        self.resolved = False
        self.answer_sound = pygame.mixer.Sound(self.answer_sound_location)

    def drop_false_clouds(self):
        """Drop all false clouds from the list"""

        for cloud in self.answer_clouds.copy():
            if not cloud.surface:
                self.answer_clouds.remove(cloud)

    def drop_all_clouds(self):

        for cloud in self.answer_clouds.copy():
            if cloud.surface:
                self.game.all_surfaces.remove(cloud.surface)
            self.answer_clouds.remove(cloud)
            self.answer_sound.stop()

    def update(self):

        if self.resolved:
            self.drop_false_clouds()
        else:
            if self.waiting_frames == 0:

                answer = self.answers[self.prev_answer]
                if self.prev_answer + 1 == self.answers_count:
                    self.prev_answer = 0
                else:
                    self.prev_answer += 1

                cloud_type = get_cloud_type(self)
                self.answer_clouds.add(Cloud(self.game, self, cloud_type, self.line_number, answer[0], answer[1]))
                self.waiting_frames = 300
                for cloud in self.answer_clouds.copy():
                    if cloud.rect.x <= 0:
                        self.answer_clouds.remove(cloud)
            else:
                self.waiting_frames -= 1
        self.answer_clouds.update()
