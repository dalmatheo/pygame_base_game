import pygame

from buttons.button import Button
from buttons.button_label import LabeledButton

pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)

color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()

smallfont = pygame.font.SysFont("Corbel", 35)

text = smallfont.render("quit", True, color)


def test():
    pass


button = LabeledButton(
    "exit_button",
    [width / 2 - 20, height / 2 - 20],
    40,
    40,
    color_dark,
    color_light,
    pygame.quit,
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkClicked()

    screen.fill((60, 25, 60))

    button.draw(screen)

    pygame.display.update()
