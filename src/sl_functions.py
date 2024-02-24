from pygame.color import THECOLORS

def update_screen(game):

    game.screen.blit(game.settings.bg_image, (0, 0))
    game.rock.blitme()
    game.hero.blitme()
