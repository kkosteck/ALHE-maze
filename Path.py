from anytree import AnyNode, RenderTree
import matplotlib.pyplot as plt
import visualisation

class Path:
    def __init__(self, maze, start, end, visualisation=False, init=True):
        self.maze = maze # data with walkable tiles and walls maze[n][m] <-> maze[y][x]
        self.n = len(maze) # height of maze
        self.m = len(maze[0]) # width of maze
        self.start = start # starting point coordinates (x,y) 
        self.end = end # end point coordinates (x,y)
        self.vis = visualisation
        if init:
            self.search()
            if self.vis:
                self.__update_visual()
                self.__clean()
        else:
            self.path = None

    def search(self):
        open_n = [] # waiting list - tiles adjusted to already visited tiles 
        closed_n = [] # checked list - tiles already visited

        # add first tile
        open_n.append(AnyNode(x=self.start[0], y=self.start[1], f_c=0, f_h=self.__heuristic(self.start[0], self.start[1])))
        while(1):
            current_n = open_n[self.__find_min(open_n)] # current visited tile
            del open_n[self.__get_id(current_n, open_n)] # delete current tile from waiting list
            closed_n.append(current_n) # add current tile to already checked
            self.__update_visual(rt=True,value=[current_n,2])

            if(current_n.x == self.end[0] and current_n.y == self.end[1]): # check if we reached end of path
                self.path = current_n
                self.__update_visual(rt=True,value=[current_n,4], found=True)
                break
            
            neighbours = self.__find_neighbours(current_n) # find all neighbours of current tile

            for n in neighbours: # check all walkable neighbours
                if self.__check_inside(n, closed_n): # check if neighbour is inside of already checked tiles
                    continue
                # calculate f_c for tile only if we found better path with it or if it is not on waiting list
                if self.__check_better_path(n, open_n) or not self.__check_inside(n, open_n):
                    index = self.__get_id(n, open_n)
                    if index is None: # tile is not in open list
                        open_n.append(n) # add to open list
                        index = -1 # set index for this tile
                        self.__update_visual(rt=True,value=[n,3])
                    open_n[index].parent = current_n # make current parent of this neighbour
                    open_n[index].f_c = n.f_c # update cost function

    def __heuristic(self, x, y): # calculate heuristic value
        return abs(x - self.end[0]) + abs(y - self.end[1])

    def __find_min(self, data): # find minimum function value in open list
        f_min = self.n + self.m + 1
        i_min = 0
        for i, n in enumerate(data):
            f = n.f_c + n.f_h
            if f < f_min:
                f_min = f
                i_min = i
        return i_min # return index of the best tile

    def __find_neighbours(self, node):
        neighbours = []
        # check all for neighbours if they are walkable
        if node.x+1 < self.m-1 and self.maze[node.y][node.x+1] != 1: 
            neighbours.append(AnyNode(x=node.x+1, y=node.y, f_c=node.f_c+1, f_h=self.__heuristic(node.x+1, node.y)))
        if node.x-1 >= 0 and self.maze[node.y][node.x-1] != 1:
            neighbours.append(AnyNode(x=node.x-1, y=node.y, f_c=node.f_c+1, f_h=self.__heuristic(node.x-1, node.y)))
        if node.y+1 < self.n-1 and self.maze[node.y+1][node.x] != 1:
            neighbours.append(AnyNode(x=node.x, y=node.y+1, f_c=node.f_c+1, f_h=self.__heuristic(node.x, node.y+1)))
        if node.y-1 >= 0 and self.maze[node.y-1][node.x] != 1:
            neighbours.append(AnyNode(x=node.x, y=node.y-1, f_c=node.f_c+1, f_h=self.__heuristic(node.x, node.y-1)))

        return neighbours

    def __check_better_path(self, node, data): # check if this path is better
        s = next((s for s in data if s.x == node.x and s.y == node.y), None) # search open list for this tile
        if s is None: # tile is not in open list
            return False
        if node.f_c + node.f_h < s.f_c + s.f_h: # function is better
            return True
        elif node.f_c + node.f_h == s.f_c + s.f_h: # cost function equal -> check heuristic function
            if node.f_h < s.f_h:
                return True
        return False

    def __check_inside(self, node, data): # check if tile is inside open/closed list
        for n in data:
            if node.x == n.x and node.y == n.y:
                return True
        return False

    def __get_id(self, node, data): # get id of tile from open list
        for i, n in enumerate(data):
            if n.x == node.x and n.y == node.y:
                return i
        return None

    def __update_visual(self, rt=False, value=None, found=False):
        if found:
            while(not value[0].is_root):
                self.maze[value[0].y][value[0].x] = value[1]
                value[0] = value[0].parent
            self.maze[value[0].y][value[0].x] = value[1] # root value
        if self.vis:
            if value is not None:
                self.maze[value[0].y][value[0].x] = value[1]
            visualisation.show_plot(self.maze, rt)

    def show(self):
        visualisation.show_plot(self.maze)

    def __clean(self):
        for i, _ in enumerate(self.maze):
            for j, _ in enumerate(self.maze[i]):
                if self.maze[i][j] == 2 or self.maze[i][j] == 3:
                    self.maze[i][j] = 0
        self.maze[self.start[1]][self.start[0]] = 3
        self.maze[self.end[1]][self.end[0]] = 3