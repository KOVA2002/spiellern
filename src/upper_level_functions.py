import pygame
from task import Task

def update_task_list(game):
    """"""

    task_list = game.task_list
    if task_list[-1].resolved:
        prev_number = task_list[-1].line_number
        task_list.append(Task(game, prev_number+1))
    for t in task_list:
        t.update()

# general
def update_screen(game) -> None:

    game.screen.blit(game.settings.bg_image, (0, 0))
    #pygame.draw.rect(game.screen, (255, 0, 250), game.surface.rect, 0)
    game.rock.blitme()
    game.floating_rock.blitme()
    game.finish_flag.blitme()
    update_task_list(game)
    game.hero.blitme()
