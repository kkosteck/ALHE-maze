import time, random, csv, os

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from Maze import *
from Path import *
from Visual import *

def create_folder(name):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, name)
    os.makedirs(path, exist_ok=True) 

def test_h(n, m, iterations, heuristic=0):
    folder_name = 'results'
    create_folder(folder_name)
    filename = str(n) + "x" + str(m) + "_" + str(iterations) + "_" + "_" + str(heuristic) + ".csv"
    filename = os.path.join(folder_name, filename)
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
            for i in range(4):
                path.h_type = i
                start = time.time()
                path.search()
                end = time.time()

            data = path.calculate_data()

            csvwriter.writerow([i+1, round((end-start)*1000,2), data[4], round(100 * (data[2]+data[3]+data[4]) / (data[0]+data[2]+data[3]+data[4]),2)])
            
            print(chr(27) + "[2J")

def testing(n, m, visualisation):
    maze = Maze(n, m, visualisation=visualisation)
    # maze.show()

    start = (1, len(maze.data)-2)
    end = (len(maze.data[0])-2, 1)

    path = Path(maze.data, start, end, visualisation=visualisation)
    path.show()

def main():
    iterations = 1000
    for i in range(4):
        test_h(10, 10, iterations, heuristic=i)


    # fig, axs = plt.subplots(1,3, tight_layout=True)
    # axs[0].hist(t, density=True, bins=n_bins)
    # axs[0].title.set_text("Path search time")
    # axs[1].hist(p, density=True, bins=n_bins)
    # axs[1].title.set_text("Path length")
    # axs[2].hist(v, density=True, bins=n_bins)
    # axs[2].title.set_text("% Visited tiles")
    # plt.show()



if __name__ == "__main__":
    random.seed(0)
    testing(100, 100, True)
    # main()