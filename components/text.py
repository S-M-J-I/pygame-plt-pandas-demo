import pygame
from constants import *


class Text:

    def __init__(self, header_type, position) -> None:
        """
            - We will set the font size accoring to the header label. 
            - Note that this can be done using a Factory design pattern: https://refactoring.guru/design-patterns/factory-method
            - But for simplicity's sake, and to not mess with y'all heads, I'll keep it short and simple!
        """
        self.font_size = 0

        if (header_type == "h1"):
            self.font_size = FONT_SIZE_XL
        elif (header_type == "h2"):
            self.font_size = FONT_SIZE_L
        elif (header_type == "h3"):
            self.font_size = FONT_SIZE_M
        elif (header_type == "h4"):
            self.font_size = FONT_SIZE_S
        elif (header_type == "body"):
            self.font_size = FONT_SIZE_XS

        if (position == "center top"):
            self.render_x = SCREEN_WIDTH/2
            self.render_y = TOP_SCALE
        elif (header_type == "center middle"):
            self.render_x = SCREEN_WIDTH/2
            self.render_y = SCREEN_HEIGHT/2
        elif (header_type == "center bottom"):
            self.render_x = SCREEN_WIDTH/2
            self.render_y = SCREEN_HEIGHT - TOP_SCALE
        elif (header_type == "center left"):
            self.render_x = TOP_SCALE
            self.render_y = SCREEN_HEIGHT/2
        elif (header_type == "center right"):
            self.render_x = SCREEN_WIDTH - TOP_SCALE
            self.render_y = SCREEN_HEIGHT/2
        else:
            self.render_x = position[0]
            self.render_y = position[1]

    @classmethod
    def center_title(cls):
        """
            If we call Header.title() instead of Header() when creating an object, then this will call Header('h1')
        """
        return Text("h1", "center top")

    def render(self, text_to_render: str):
        font = pygame.font.Font(EXTRA_BOLD, self.font_size)

        if type(text_to_render) != str:
            text_to_render = str(text_to_render)

        text = font.render(text_to_render, True, FONT_COLOR)
        text_rect = text.get_rect(center=(self.render_x, self.render_y))
        return text, text_rect
