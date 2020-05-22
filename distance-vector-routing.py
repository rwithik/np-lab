#!/bin/python

router_matrix = []
nodes = []
distances = {}
num_nodes = 0
edges = []


def process_file(fname):

    global router_matrix
    router_matrix = []

    with open(fname) as f:

        router_matrix = [list(map(int, x.split(" "))) for x in f]

    print("\nInput:\n")

    for line in router_matrix:
        for item in line:
            print(item, end=" ")
        print()

    print()
    set_distances(router_matrix)


def set_distances(router_matrix):
    global distances
    global nodes
    distances = {}
    nodes = []

    num_nodes = len(router_matrix)
    print("Creating Distance Tables... ")

    for i in range(num_nodes):
        tempdict = {}
        for j in range(num_nodes):
            if i != j and router_matrix[i][j] != -1:
                tempdict[j + 1] = router_matrix[i][j]

        distances[i + 1] = tempdict
        nodes.append(i + 1)
    set_edges()


def set_edges():
    print("--------------------")
    print("U", "V", "W")
    for key, value in distances.items():
        u = key
        value = dict(value)
        for v, wt in value.items():
            print(u, v, wt)
            edges.append([u, v, wt])

    print("---------------------")


def bellman_ford(src):
    global nodes
    nextHop = {}
    nextHop = {node: None for node in nodes}
    num_of_nodes = len(router_matrix)
    dist = [float("Inf")] * (num_of_nodes + 1)
    dist[src] = 0

    for i in range(num_of_nodes - 1):
        for u, v, wt in edges:
            if dist[u] != float("Inf") and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
                if not nextHop[v]:
                    nextHop[v] = v
                else:
                    nextHop[v] = nextHop[u]

    print("Table for Router : ", src)
    print("Destination \t Next Hop \t Distance")

    destination_list = list()
    nextHop_list = list()
    destination_list.append(999)
    nextHop_list.append(999)

    for k, v in nextHop.items():
        if v is None:
            v = src
        destination_list.append(k)
        nextHop_list.append(v)

    for i in range(1, num_of_nodes + 1):
        print(
            "%d \t\t\t %d \t\t\t %d" % (destination_list[i], nextHop_list[i], dist[i])
        )


process_file("input.txt")

numof_nodes = len(router_matrix)

for i in range(1, numof_nodes + 1):
    bellman_ford(i)
