import pygame, sys
from pygame.color import THECOLORS
"""
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
"""


# Define the decorator function
def log_arguments_and_return(func):
    def wrapper(*args, **kwargs):
        # Log the function name
        print(f"Calling function: {func.__name__}")

        # Log the arguments
        print("Arguments:", args, kwargs)

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        print("Return value:", result)

        return result

    return wrapper

# Apply the decorator to a function
@log_arguments_and_return
def add(x, y):
    return x + y





# Call the decorated function
result = add(3, 5)

add(5,7)

# https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/18-pygame.html

# TODO: !!! Remove this file after adding fonts
