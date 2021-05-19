import math
from collections import Counter

from anytree import AnyNode

from Visual import *

class Path:
    def __init__(self, maze, start, end, visualisation=False, init=True, heuristic_type=0):
        self.maze = maze # data with walkable tiles and walls maze[n][m] <-> maze[y][x]
        self.n = len(maze) # height of maze
        self.m = len(maze[0]) # width of maze
        self.start = start # starting point coordinates (x,y) 
        self.end = end # end point coordinates (x,y)
        self.h_type = heuristic_type # choose which heuristic to use
        if visualisation:
            self.visual = Visual(self.n, self.m)
            self.visual.draw_maze(self.maze)
        else:
            self.visual = None
        if init:
            self.search()
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
            self.__update_visual(current_n.x, current_n.y, 2)

            if(current_n.x == self.end[0] and current_n.y == self.end[1]): # check if we reached end of path
                self.path = current_n
                self.__update_visual_path(current_n)
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
                        self.__update_visual(n.x,n.y,3)
                    open_n[index].parent = current_n # make current parent of this neighbour
                    open_n[index].f_c = n.f_c # update cost function

    def __heuristic(self, x, y): # calculate heuristic value
        if self.h_type == 0:
            return abs(x - self.end[0]) + abs(y - self.end[1])
        elif self.h_type == 1:
            return math.sqrt((x - self.end[0])**2 + (y - self.end[1])**2)
        elif self.h_type == 2:
            if self.n > self.m:
                return abs(y - self.end[1])
            else:
                return abs(x - self.end[0])
        return 0 

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

    def __update_visual_path(self, node):
        self.maze[node.y][node.x] = 4
        if self.visual is not None:
            self.visual.draw_cell(node.x,node.y,BLUE)
        while(not node.is_root):
            self.maze[node.y][node.x] = 4
            node = node.parent
            if self.visual is not None:
                self.visual.draw_cell(node.x,node.y,BLUE)
        self.maze[node.y][node.x] = 4 # root value


    def __update_visual(self, x, y, value):
        if value == 2:
            color = GREEN
        elif value == 3:
            color = RED
        self.maze[y][x] = value
        if self.visual is not None:
            self.visual.draw_cell(x,y,color)

    def show(self):
        if self.visual is not None:
            self.visual.show(self.maze)
        else:
            self.visual = Visual(self.n, self.m)
            self.visual.show(self.maze)
            self.visual = None


    def clean(self):
        for i, _ in enumerate(self.maze):
            for j, _ in enumerate(self.maze[i]):
                if self.maze[i][j] == 2 or self.maze[i][j] == 3:
                    self.maze[i][j] = 0
        self.maze[self.start[1]][self.start[0]] = 0
        self.maze[self.end[1]][self.end[0]] = 0

    def calculate_data(self):
        temp = [cell for row in self.maze for cell in row]
        return Counter(temp)
