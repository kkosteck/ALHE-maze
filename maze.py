import random

from anytree import AnyNode

from Visual import *

# Randomized Kruskal's algorithm implementation

class Maze:
    # n - height, m - width
    # visualsation - showing real time generation
    def __init__(self, n, m, visualisation=False, init=True):
        self.n = int(n / 2) # size of walkable tiles is two times smaller, because of edge spacing
        self.m = int(m / 2)
        if visualisation:
            self.visual = Visual(n+1,m+1)
        else:
            self.visual = None

        self.nodes = self.__create_nodes() # generate tree nodes for every walkable tile
        self.edges = self.__create_edges() # generate edges of nodes
        if init:
            self.generate() # generate maze data
        else:
            self.data = []

    def __create_nodes(self):
        nodes = []
        for i in range(self.n):
            for j in range(self.m):
                nodes.append(AnyNode(id=i*self.m+j)) # id is assigned numerically: 0,1,2,3,..., n*m - 1
        return nodes

    def __create_edges(self):
        edges = []
        for i in range(self.n):
            for j in range(self.m):
                if j != self.m-1:
                    edges.append((i*self.m+j, i*self.m+j+1)) # vertical edge
                if i != self.n-1:
                    edges.append((i*self.m+j, (i+1)*self.m+j)) # horizontal edge 
        # random.shuffle(edges) # randomized list of edges
        return edges

    # maze generation
    def generate(self):
        self.data = [[0]*(2*self.m+1) for x in range(2*self.n+1)] # generate maze array with zeros
        if self.visual is not None:
            self.visual.draw_maze(self.data)

        edges_temp = self.edges.copy() # copy edge list - edges are popped from list so we have to copy it to have it saved
        random.shuffle(edges_temp)
        while(edges_temp):

            id_1 = edges_temp[-1][0] # id of first node
            id_2 = edges_temp[-1][1] # id of second node
            node_1 = next(x for x in self.nodes if x.id==id_1) # search for first node variable
            node_2 = next(x for x in self.nodes if x.id==id_2) # search for second node variable

            if not node_1.is_root:
                node_1 = node_1.ancestors[0] # root of first node
            if not node_2.is_root:
                node_2 = node_2.ancestors[0] # root of second node
            if node_1.id == node_2.id: # check if nodes are in same tree
                x, y = self.__getCords(id_1, id_2)
                self.data[y+1][x+1] = 1 # nodes are connected, so we save this edge
                self.__update_visual([(x+1,y+1)])
            else: # nodes are not connected, because we assigned 0 values before we do not change any maze value
                self.__update_visual(self.__fillCorners(id_1, id_2))
                temp = list(node_1.children) # save first node children
                temp.append(node_2) # add second node as first node's child
                node_1.children = temp 
            edges_temp.pop() # remove checked edge
        
        for i in range(2*self.n+1): # fill bouding box and corners
            for j in range(2*self.m+1):
                if i == 0 or i == 2*self.n or j == 0 or j == 2*self.m or (i%2 == 0 and j%2 == 0):
                    self.data[i][j] = 1

    # finding cordinates of edge between two nodes in maze array
    def __getCords(self, id_1, id_2):
        if id_2 - id_1 == 1: # vertical edge
            x = (id_1%self.m)*2+1
            y = int(id_1/self.m) * 2
        else: # horizontal edge
            x = (id_1%self.m) * 2
            y = int(id_1/self.m)*2 + 1
        return x, y

    # fill corners - only for visualisation
    def __fillCorners(self,id_1, id_2):
        x = lambda a: a%self.m*2 + 1
        y = lambda a: int(a/self.m)*2 + 1
        coords = []
        coords.append((x(id_1)-1,y(id_1)-1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((y(id_1)+1,y(id_1)-1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((y(id_1)-1,y(id_1)+1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((y(id_1)+1,y(id_1)+1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        
        coords.append((x(id_2)-1,y(id_2)-1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((x(id_2)+1,y(id_2)-1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((x(id_2)-1,y(id_2)+1))
        self.data[coords[-1][1]][coords[-1][0]] = 1
        coords.append((x(id_2)+1,y(id_2)+1))
        self.data[coords[-1][1]][coords[-1][0]] = 1

        return coords


    def __update_visual(self, coords):
        if self.visual is not None: # for some action in visualisation
            for i in coords:
                self.visual.draw_cell(i[0],i[1],BLACK)

    def show(self):
        if self.visual is not None:
            self.visual.show(self.data)
        else:
            self.visual = Visual(2*self.n+1, 2*self.m+1)
            self.visual.show(self.data)
            self.visual = None

    def clean_nodes(self):
        for i in range(self.n):
            for j in range(self.m):
                self.nodes[i*self.m+j].parent = None