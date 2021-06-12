from Maze import *
from Path import *
from Visual import *
import sys


def testing(n, m, maze_visualisation=True, path_visualisation=True):
    maze = Maze(n, m, visualisation=maze_visualisation)
    # maze.show()

    start = (1, len(maze.data) - 2)
    end = (len(maze.data[0]) - 2, 1)

    path = Path(maze.data, start, end, visualisation=path_visualisation)
    path.show()


if __name__ == "__main__":
    # random.seed(578)
    # testing(50, 50, path_visualisation=True)
    if (len(sys.argv) > 2):
        testing(int(sys.argv[1]), int(sys.argv[2]))


