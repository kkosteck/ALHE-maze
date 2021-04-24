import matplotlib.pyplot as plt
import random

import numpy as np
from timeit import default_timer as timer
from anytree import AnyNode, RenderTree

N = 5
M = 10

def getCords(id_1, id_2):
    if id_2 - id_1 == 1: # vertical edge
        x = (id_1%M)*2+1
        y = int(id_1/M) * 2
    else: # horizontal edge
        x = (id_1%M) * 2
        y = int(id_1/M)*2 + 1
    return x, y

def fillCorners(area, direction):
    area[1][1] = 1
    if direction:
        if area[0][1] == 1:
            area[2][1] = 1
        else:
            area[0][1] = 1
    else:
        if area[1][0] == 1:
            area[1][2] = 1
        else:
            area[1][0] = 1
    return area

def generateData():
    nodes = []
    for i in range(N):
        for j in range(M):
            nodes.append(AnyNode(id=i*M+j))

    edges = []
    for i in range(N):
        for j in range(M):
            if j != M-1:
                edges.append((i*M+j, i*M+j+1))
            if i != N-1:
                edges.append((i*M+j, (i+1)*M+j))

    random.shuffle(edges)
    return nodes, edges

def generateMaze(nodes, edges):
    maze = [[0]*(2*M+1) for x in range(2*N+1)]

    while(edges):
        plt.cla()
        plt.imshow(maze)
        plt.pause(0.01)

        id_1 = edges[-1][0]
        id_2 = edges[-1][1]
        node_1 = next(x for x in nodes if x.id==id_1)
        node_2 = next(x for x in nodes if x.id==id_2)

        for node in node_1.iter_path_reverse():
            if node.is_root:
                node_1 = node
                break
        for node in node_2.iter_path_reverse():
            if node.is_root:
                node_2 = node
                break

        if node_1.id == node_2.id:
            x, y = getCords(id_1, id_2)

            area = fillCorners([row[x:x+3] for row in maze[y:y+3]], id_2 - id_1 == 1)
            for i in range(3):
                for j in range(3):
                    maze[y+i][x+j] = area[i][j]
        else:
            temp = list(node_1.children)
            temp.append(node_2)
            node_1.children = temp
        edges.pop()
    
    for i in range(2*N+1):
        for j in range(2*M+1):
            if i == 0 or i == 2*N or j == 0 or j == 2*M:
                maze[i][j] = 1

    return maze

if __name__ == "__main__":
    nodes, edges = generateData()

    maze = generateMaze(nodes, edges)
    plt.imshow(maze)
    plt.show()