import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

# Plotting with chosen colors in rgb
# needs performance optimalisation

def show_plot(maze, rt=False, values=None):
    a = np.array(maze)
    ca = np.array([[0,140,140,140],
                [1,0,0,0],
                [2,0,255,0],
                [3,255,0,0],
                [4,0,0,255]])

    if values == 4:
        ca[[3,4]] = ca[[4,3]]

    u, ind = np.unique(a, return_inverse=True)
    b = ind.reshape((a.shape))

    colors = ca[ca[:,0].argsort()][:,1:]/255.
    cmap = matplotlib.colors.ListedColormap(colors)
    norm = matplotlib.colors.BoundaryNorm(np.arange(len(ca)+1)-0.5, len(ca))

    plt.imshow(b, cmap=cmap, norm=norm)
    if rt:
        plt.pause(1e-2)
    else:
        plt.show()