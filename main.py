from Maze import *
from Path import *
from Visual import *

import time
import matplotlib.pyplot as plt
import numpy as np
import csv

from tqdm import tqdm

def test_h(n, m, iterations, heuristic=0):
    filename = str(n) + "x" + str(m) + "_" + str(iterations) + "_" + "_" + str(heuristic) + ".csv"
    with open(filename, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")

        csvwriter.writerow(['iteration', 'time [ms]', 'path length', 'visited tiles [%]'])

        maze = Maze(n, m)
        path = Path(maze.data, (1, len(maze.data)-2), (len(maze.data[0])-2, 1), init=False, heuristic_type=heuristic)
        for i in tqdm(range(iterations)):
            maze.clean_nodes()
            maze.generate()

            path.maze = maze.data
            path.path = None

            start = time.time()
            path.search()
            end = time.time()

            data = path.calculate_data()

            csvwriter.writerow([i+1, round((end-start)*1000,2), data[4], round(100 * (data[2]+data[3]) / (data[0]+data[2]+data[3]),2)])
            
            print(chr(27) + "[2J")

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
    iterations = 1000
    test_h(50, 50, iterations)
    n_bins = int(iterations / 10)


    # fig, axs = plt.subplots(1,3, tight_layout=True)
    # axs[0].hist(t, density=True, bins=n_bins)
    # axs[0].title.set_text("Path search time")
    # axs[1].hist(p, density=True, bins=n_bins)
    # axs[1].title.set_text("Path length")
    # axs[2].hist(v, density=True, bins=n_bins)
    # axs[2].title.set_text("% Visited tiles")
    # plt.show()




if __name__ == "__main__":
    main()