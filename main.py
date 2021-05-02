from Maze import *
from Path import *
from Visual import *

def main():
    visualisation = True
    n = 100
    m = 100
    maze = Maze(n, m, visualisation=visualisation)
    maze.show()


    start = (1, len(maze.data)-2)
    end = (len(maze.data[0])-2, 1)

    path = Path(maze.data, start, end, visualisation=visualisation)
    path.show()

if __name__ == "__main__":
    main()