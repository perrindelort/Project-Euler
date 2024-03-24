# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:36:30 2024

@author: Antoine
"""

import colored
from colored import stylize, fore, style

def display_colors(color_name = "all"):
    colors = colored.Colored('a')._COLORS
    if color_name != "all":
        colors = {name: value for name, value in colors.items() if color_name.lower() in name.lower()}
    
    columns = 7
    rows = (len(colors) + columns - 1) // columns
    max_width = max(len(name) for name in colors)

    for row in range(rows):
        for col in range(columns):
            index = row * columns + col
            if index < len(colors):
                color_name, color_value = list(colors.items())[index]
                print(stylize(f"{color_name:<{max_width}} ", fore(color_value)), end="")
            else:
                print("", end="")
        print()
