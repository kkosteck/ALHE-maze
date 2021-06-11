from Maze import *
from Path import *
from Visual import *
from plots import analysis_received_data


def testing(n, m, visualisation):
    maze = Maze(n, m, visualisation=visualisation)
    # maze.show()

    start = (1, len(maze.data) - 2)
    end = (len(maze.data[0]) - 2, 1)

    path = Path(maze.data, start, end, visualisation=visualisation)
    path.show()


if __name__ == "__main__":
    random.seed(578)
    # testing(10, 10, True)
    analysis_received_data(20, 20, 1000)
    analysis_received_data(50, 50, 1000)
    analysis_received_data(100, 100, 1000)
