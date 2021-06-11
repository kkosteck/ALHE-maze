import pandas as pd
import matplotlib.pyplot as plt
import math, time, random, csv, os
from tqdm import tqdm
from Maze import *
from Path import *


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
        csvwriter = csv.writer(csvfile, delimiter=",")

        csvwriter.writerow(['iteration', 'time [ms]', 'path length', 'visited tiles [%]'])

        maze = Maze(n, m)
        path = Path(maze.data, (1, len(maze.data) - 2), (len(maze.data[0]) - 2, 1), init=False,
                    heuristic_type=heuristic)
        for i in tqdm(range(iterations)):
            maze.clean_nodes()
            maze.generate()

            path.maze = maze.data
            path.path = None
            for j in range(4):
                path.h_type = j
                start = time.time()
                path.search()
                end = time.time()

            data = path.calculate_data()

            csvwriter.writerow([i + 1, round((end - start) * 1000, 2), data[4],
                                round(100 * (data[2] + data[3] + data[4]) / (data[0] + data[2] + data[3] + data[4]),
                                      2)])

            print(chr(27) + "[2J")


def make_plots(n, m, iterations):
    folder_name = 'plots'
    create_folder(folder_name)
    file_name = str(n) + "x" + str(m) + "_" + str(iterations) + ".jpg"
    file_name = os.path.join(folder_name, file_name)

    column_names = ['time [ms]', 'path length', 'visited tiles [%]']

    fig, axs = plt.subplots(nrows=3, ncols=3, tight_layout=True, figsize=(10, 10))
    fig.suptitle('Data for a ' + str(n) + 'x' + str(m) + ' maze.', fontsize=25)

    for heuristic in range(3):
        data = pd.read_csv('results/' + str(n) + 'x' + str(m) + '_' + str(iterations) + '__' + str(heuristic) + '.csv')

        axs[heuristic, 0].set_ylabel('heuristic ' + str(heuristic), rotation=90, fontsize=15)

        for i in range(3):
            axs[heuristic][i].hist(data[column_names[i]], edgecolor='black')
            axs[heuristic][i].set_xlabel(column_names[i])

            column_data = data[column_names[i]]
            average = sum(column_data) / len(column_data)
            color = '#fc4f30'

            axs[heuristic][i].axvline(average, color=color, label='average ' + column_names[i])

            squared_sum = 0
            for row in column_data:
                squared_sum += row ** 2

            sigma = round(math.sqrt(squared_sum / len(column_data) - average ** 2), 2)

            axs[heuristic][i].plot([], [], ' ', label=r'$\sigma=$' + str(sigma))
            axs[heuristic][i].legend()
    # plt.show()
    plt.savefig(file_name)


def analysis_received_data(n, m, iterations):
    for i in range(3):
        test_h(n, m, iterations, heuristic=i)
    make_plots(n, m, iterations)

#
# if __name__ == "__main__":
#     make_plots(10, 10, 1000)
#     analysis_received_data(10, 10, 1000)
