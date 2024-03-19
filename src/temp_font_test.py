import pygame, sys
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode((1200, 800))
screen.fill(THECOLORS['white'])
font = pygame.font.SysFont('couriernew', 40, italic=True)
text = font.render(str('HELLO'), True, THECOLORS['purple4'])
#print(THECOLORS.keys())
print(text.get_width())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(text, (50, 50))
    pygame.display.flip()


# https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/18-pygame.html

# TODO: !!! Remove this file after adding fonts
