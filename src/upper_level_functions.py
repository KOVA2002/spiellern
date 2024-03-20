import pygame
from task import Task

def update_task_list(game):
    """"""

    if game.task_list[-1].resolved:
        prev_number = game.task_list[-1].line_number
        if prev_number < 6:
            game.task_list.append(Task(game, prev_number+1))
        if len(game.task_list) > 2:
            game.task_list[-3].drop_all_clouds()
            del game.task_list[-3]
    if len(game.task_list) > 1 \
            and len(game.task_list[-2].answer_clouds.sprites()) > 0 \
            and game.hero.rect.bottom > game.task_list[-2].answer_clouds.sprites()[0].rect.bottom+10:
        for t in game.task_list:
            t.drop_all_clouds()
        game.task_list = [Task(game, 1),]
    for t in game.task_list:
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
