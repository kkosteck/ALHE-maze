from Maze import *
from Path import *

def main():
    n = 5
    m = 10
    maze = Maze(n, m, False)
    # maze.show()

    path = Path(maze.data, (1, n-2),(m-2, 1))
    path.search()

if __name__ == "__main__":
    main()