from anytree import AnyNode, RenderTree
import matplotlib.pyplot as plt

class Path:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.n = len(maze)
        self.m = len(maze[0])
        self.start = start
        self.end = end

    def search(self):
        open_n = []
        closed_n = []

        open_n.append(AnyNode(x=self.start[0], y=self.start[1], f_c=0, f_h=self.__heuristic(self.start[0], self.start[1])))
        while(1):
            if open_n is None:
                print('halo')
            current_n = open_n[self.__find_min(open_n)]
            del open_n[self.__get_id(current_n, open_n)]
            closed_n.append(current_n)
            self.__update_visualisation(current_n, 2)

            if(current_n.x == self.end[0] and current_n.y == self.end[1]):
                self.__path_visualisation(current_n)
                return current_n
            
            neighbors = self.__find_neighbors(current_n)

            for n in neighbors:
                if self.__check_inside(n, closed_n):
                    continue
                if self.__check_better_path(n, open_n) or not self.__check_inside(n, open_n):
                    index = self.__get_id(n, open_n)
                    if index is None:
                        open_n.append(n)
                        self.__update_visualisation(n, 3)
                    else:
                        open_n[index].parent = current_n
                        open_n[index].f_c = n.f_c

    def __heuristic(self, x, y):
        return abs(x - self.end[0]) + abs(y - self.end[1])

    def __find_min(self, data):
        f_min = self.n + self.m + 1
        i_min = 0
        for i, n in enumerate(data):
            f = n.f_c + n.f_h
            if f < f_min:
                f_min = f
                i_min = i
        return i_min

    def __find_neighbors(self, node):
        neighbors = []
        if node.x+1 < self.m and self.maze[node.y][node.x+1] != 1:
            neighbors.append(AnyNode(x=node.x+1, y=node.y, f_c=node.f_c+1, f_h=self.__heuristic(node.x+1, node.y)))
        if node.x-1 >= 0 and self.maze[node.y][node.x-1] != 1:
            neighbors.append(AnyNode(x=node.x-1, y=node.y, f_c=node.f_c+1, f_h=self.__heuristic(node.x-1, node.y)))
        if node.y+1 < self.n and self.maze[node.y+1][node.x] != 1:
            neighbors.append(AnyNode(x=node.x, y=node.y+1, f_c=node.f_c+1, f_h=self.__heuristic(node.x, node.y+1)))
        if node.y-1 >= 0 and self.maze[node.y-1][node.x] != 1:
            neighbors.append(AnyNode(x=node.x, y=node.y-1, f_c=node.f_c+1, f_h=self.__heuristic(node.x, node.y-1)))

        return neighbors

    def __check_better_path(self, node, data):
        s = next((s for s in data if s.x == node.x and s.y == node.y), None) # nodes in open of this cell
        if s is None:
            return False
        if node.f_c + node.f_h < s.f_c + s.f_h:
            return True
        elif node.f_c + node.f_h == s.f_c + s.f_h:
            if node.f_h < s.f_h:
                return True
        return False

    def __check_inside(self, node, data):
        for n in data:
            if node.x == n.x and node.y == n.y:
                return True
        return False

    def __get_id(self, node, data):
        for i, n in enumerate(data):
            if n.x == node.x and n.y == node.y:
                return i
        return None

    def __update_visualisation(self, node, value):
        self.maze[node.y][node.x] = value
        plt.cla()
        plt.imshow(self.maze)
        plt.pause(1e-2)

    def __path_visualisation(self, node):
        while(not node.is_root):
            self.maze[node.y][node.y] = 4
            node = node.parent
        plt.cla()
        plt.imshow(self.maze)
        plt.show()