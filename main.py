from Maze import *
from Path import *
from Visual import *

import time
import matplotlib.pyplot as plt
import numpy as np


def test_h(n, m, iterations):
    times = []
    paths = []
    visited = []
    maze = Maze(n, m)
    path = Path(maze.data, (1, len(maze.data)-2), (len(maze.data[0])-2, 1), init=False)
    for i in range(iterations):
        maze.clean_nodes()
        maze.generate()
        path.maze = maze.data
        path.path = None
        start = time.time()
        path.search()
        end = time.time()
        times.append(end-start)
        data = path.calculate_data()
        paths.append(data[4])
        visited.append(100 * (data[2]+data[3]) / (data[0]+data[2]+data[3]))

    return times, paths, visited

def testing():
    visualisation = False
    n = 100
    m = 100
    maze = Maze(n, m, visualisation=visualisation)
    # maze.show()


    start = (1, len(maze.data)-2)
    end = (len(maze.data[0])-2, 1)

    path = Path(maze.data, start, end, visualisation=visualisation)
    path.show()
    print(path.calculate_data()[4])

def main():
    t, p, v = test_h(20, 20, 100)
    plt.hist(p, density=True, bins=10, ec="k")
    plt.show()




if __name__ == "__main__":
    main()