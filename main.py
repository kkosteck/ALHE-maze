import matplotlib.pyplot as plt
import random
from timeit import default_timer as timer

from anytree import AnyNode, RenderTree

N = 10


if __name__ == "__main__":
    nodes = []
    for i in range(N):
        for j in range(N):
            nodes.append(AnyNode(id=i*N+j+1))

    edges = []
    for i in range(N):
        for j in range(1, N+1):
            if j != N:
                edges.append((i*N+j, i*N+j+1))
            if i != N-1:
                edges.append((i*N+j, (i+1)*N+j))

    random.shuffle(edges)

    maze = []
    start = timer()
    while(edges):
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
            maze.append(edges[-1])
        else:
            temp = list(node_1.children)
            temp.append(node_2)
            node_1.children = temp
        edges.pop()
    end = timer()
    print(end - start)

    maze.sort()
    print(maze)

    # plt.imshow(nodes)
    # plt.show()