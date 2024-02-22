from pygame.color import THECOLORS

def update_screen(game):

    game.screen.fill(game.settings.bg_color)
    game.hero.blitme()
