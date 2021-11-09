from math import sqrt
import networkx as nx
import matplotlib.pyplot as plt


# import numpy as np
# import matplotlib

def square_num_determination(N=32):  # step_1
    squares = [i ** 2 for i in range(2, int(sqrt(2 * N - 1)) + 1)]  # 2*N-1 == k^2
    print(squares)

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):  # 1+2 = 3, (N-1) + N = 2N -1 == k^2
            if (i + j) in squares:
                print(i, j)  # edge set


def createGraph(N=32):  # step_2
    squares = [i ** 2 for i in range(2, int(sqrt(2 * N - 1)) + 1)]  # 2*N-1 == k^2

    graph = {i: [] for i in range(1, N + 1)}  # key:value -> list

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i + j) in squares:  # Is this a square number?
                graph[i].append(j)  # min + max = k^2: Undirected Graph
                graph[j].append(i)
    return graph


def draw_Graph(N=32):  # step_3
    graph = createGraph(N)

    plt.subplot(40, 40, 1)
    nxgraph = nx.Graph()
    nxgraph.add_nodes_from([i for i in range(1, N + 1)])  # Making nodes for each number
    for vertex in graph.keys():
        for edge in graph[vertex]:
            nxgraph.add_edge(vertex, edge)  # add edge for each vertex(node)
    pos = nx.spectral_layout(nxgraph)
    nx.draw_networkx(nxgraph, pos=pos, with_labels=True)


def hamiltonCycle(graph, vertex, path, draw_graph=0):  # step_4
    global count
    if len(path) == len(graph) and vertex in graph[path[0]]:
        print(path)
        count += 1
        plt.subplot(40, 40, 1 + count)
        if draw_graph == 1:
            nxgraph = nx.Graph()
            nxgraph.add_nodes_from([i for i in range(1, N + 1)])  # Making nodes for each number
            for i in range(len(path)):
                nxgraph.add_edge(path[i - 1], path[i])  # Making edge for circle
            pos = nx.spectral_layout(nxgraph)
            nx.draw_networkx(nxgraph, pos=pos, with_labels=True)
        else:
            pass

    else:
        for neighbor in graph[vertex]:
            if neighbor not in path:
                path.append(neighbor)
                hamiltonCycle(graph, neighbor, path, draw_graph)
                path.pop()


if __name__ == '__main__':
    plt.figure(figsize=(250, 250))
    plt.plot()

    N = 32

    square_num_determination(N)

    graph = createGraph(N)
    # show vertex and edge
    for vertex in graph.keys():
        print("{0}: {1}".format(vertex, graph[vertex]))

    # draw connected graph
    draw_Graph()

    # hamiltonCycle
    count = 0

    # N = 32
    graph = createGraph(N)
    path = [1]
    hamiltonCycle(graph, path[0], path, 1)
    print("총 갯수: {0}".format(count))



