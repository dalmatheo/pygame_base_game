import pygame
from buttons.button import Button


class LabeledButton(Button):
    def __init__(
        self,
        name: str,
        pos: [int, int],
        width: int,
        height: int,
        color,
        color_hover,
        text: str,
        command,
        text_anchor: str = "center",
    ):
        self.name = name
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.color_hover = color_hover
        self.command = command
        self.is_hovered = False
        self.text = text
        self.text_anchor = text_anchor

    def draw(self, screen: pygame.Surface):
        mouse = pygame.mouse.get_pos()
        if (
            mouse[0] >= self.pos[0]
            and mouse[0] <= self.pos[0] + self.width
            and mouse[1] >= self.pos[0]
            and mouse[1] <= self.pos[0] + self.height
        ):
            self.is_hovered = True
            pygame.draw.rect(
                screen,
                self.color_hover,
                [self.pos[0], self.pos[1], self.width, self.height],
            )
        else:
            pygame.draw.rect(
                screen, self.color, [self.pos[0], self.pos[1], self.width, self.height]
            )
