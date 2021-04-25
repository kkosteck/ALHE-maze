import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

# Plotting with chosen colors in rgb
# needs performance optimalisation

def show_plot(maze, rt=False, values=None):
    colors = ["lightgray", "black", "g", "r","b"]

    if values == 4:
        colors[3], colors[4] = colors[4], colors[3]

    norm =plt.Normalize(0,4)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

    plt.imshow(maze, cmap=cmap, norm=norm)
    if rt:
        plt.pause(1e-4)
    else:
        plt.show()