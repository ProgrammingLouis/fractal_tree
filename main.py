import pygame
import json

from tree import *
import json_data_file_manager

default_tree_params = {
    "branches_nb": 2,
    "trunk_length": 200,
    "additional_trunk_length": 0,
    "length_dividor": 1.4,
    "branch_min_size": 5,
    "semi_angle": 25,
    "trunk_thickness": 20,
    "thickness_dividor": 1.28,
    "animate_generation": False
}
tree_json_manager = json_data_file_manager.manager("tree_params.json", default_tree_params)

default_win_params = {
    "width": 800,
    "height": 1000
}
win_json_manager = json_data_file_manager.manager("win_params.json", default_win_params)

pygame.init()
pygame.display.set_caption("fractal tree")
win_size = win_width, win_height = win_json_manager.datas["height"], win_json_manager.datas["width"]
win_surface = pygame.display.set_mode(win_size, pygame.RESIZABLE)

factral_tree1 = tree(tree_json_manager.datas)

# factral_tree1 = tree({"length_dividor": 1.4,
#                       "thickness_dividor": 1.5,
#                       "semi_angle": 30,
#                       "thickness": 6,
#                       "branches_nb": 32,
#                       "branc_min_size": 100})

run = True
while run:
    # *** EVENTS ***
    for event in pygame.event.get():
        event_type = event.type

        # end the loop if the game is closed
        if event_type == pygame.QUIT:
            run = False

        # keyboard events
        elif event_type == pygame.KEYDOWN:
            if event.key == 286:  # F5 key
                tree_json_manager.read_file()
                win_surface.fill((0, 0, 0))
                factral_tree1.options = tree_json_manager.datas
                factral_tree1.draw((win_size[0] / 2, win_size[1]), win_surface)
                pygame.display.flip()

        elif event_type == pygame.VIDEORESIZE:
            win_size = win_width, win_height = event.w, event.h
            win_surface = pygame.display.set_mode(win_size, pygame.RESIZABLE)
            win_surface.fill((0, 0, 0))
            factral_tree1.draw((win_size[0] / 2, win_size[1]), win_surface)
            pygame.display.flip()
            # while True:
            #     win_surface.fill((0, 0, 0))
            #     factral_tree2.draw((win_size[0]*(1/2), win_size[1]), win_surface)
            #     factral_tree2.branc_min_size -= 0.1
            #     pygame.display.flip()
