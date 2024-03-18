import pygame
from pygame.locals import *
from constants import *
from functions.visualizer import *
from components.text import Text
from components.dropdown import DropDown
import sys

import pandas as pd


pygame.init()
pygame.display.set_caption('Project 1 : Car Dealership Dashboard')

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

data = pd.read_csv("./files/input/car_prices.csv")
data.dropna(inplace=True)
cols = data.columns
display_cols = cols[:-2]


dropdown = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    DROPDOWN_X_COORD, DROPDOWN_Y_COORD, DROPDOWN_WIDTH, DROPDOWN_HEIGHT,
    pygame.font.Font(REGULAR, FONT_SIZE_XS),
    "Select Feature", display_cols
)

image = None

while running:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    screen.blit(*Text.center_title().render("Car Dealership Dashboard"))
    screen.blit(*Text("body", (LABEL_X_COORD, LABEL_Y_COORD)
                      ).render("Select feature to view: "))

    selected_option = dropdown.update(events)
    if selected_option >= 0:
        dropdown.main = dropdown.options[selected_option]
        groupby_col = cols[selected_option]
        groupby_data = data.filter(
            items=[groupby_col, "sellingprice"]).groupby(groupby_col, as_index=False).mean().reset_index()

        image_string = plot_graph(
            groupby_data, f"{groupby_col.title()} vs Selling Price", groupby_col)
        image = pygame.image.fromstring(image_string, GRAPH_RESOLUTION, "RGB")

    if image is not None:
        screen.blit(image, (SCREEN_WIDTH/2 - 300, 130))

    dropdown.draw(screen)

    pygame.display.flip()


pygame.quit()
sys.exit()
