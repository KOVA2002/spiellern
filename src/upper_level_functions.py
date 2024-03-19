import pygame
from task import Task

def update_task_list(game):
    """"""

    #TODO: remove resolved tasks once hero moves up
    #TODO: start from the first line if hero falls
    #TODO: restrict number of possible tasks to 6
    task_list = game.task_list
    if task_list[-1].resolved:
        prev_number = task_list[-1].line_number
        task_list.append(Task(game, prev_number+1))
    for t in task_list:
        t.update()

# general
def update_screen(game) -> None:

    game.screen.blit(game.settings.bg_image, (0, 0))
    game.board.blitme()
    game.rock.blitme()
    game.floating_rock.blitme()
    game.finish_flag.blitme()
    update_task_list(game)
    game.hero.blitme()
