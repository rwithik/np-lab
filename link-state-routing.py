router_matrix = []
nodes = []
distances = {}
unvisited = {}
previous = {}
visited = {}
interface = {}
start = 0


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

    print("Creating Distance Tables...")
    for i in range(num_nodes):
        tempdict = {}
        for j in range(num_nodes):
            if i != j and router_matrix[i][j] != -1:
                tempdict[j + 1] = router_matrix[i][j]

        distances[i + 1] = tempdict
        nodes.append(i + 1)
        print("--------------------")
        for key, value in distances.items():
            print(key, value)
        print("---------------------")


def dijkstra(start):

    global distances
    global nodes
    global unvisited
    global previous
    global visited
    global interface

    unvisited = {node: None for node in nodes}
    previous = {node: None for node in nodes}
    interface = {node: None for node in nodes}
    visited = {node: None for node in nodes}
    current = start
    currentDist = 0
    unvisited[current] = currentDist
    print("Building the Router Table for Router:", start)

    while True:
        for next, distance in distances[current].items():
            if next not in unvisited:
                continue

            newDist = currentDist + distance
            if not unvisited[next] or unvisited[next] > newDist:
                unvisited[next] = newDist
                previous[next] = current
                if not interface[current]:
                    interface[next] = next
                else:
                    interface[next] = interface[current]

        visited[current] = currentDist
        del unvisited[current]
        isOver = 1

        for x in unvisited:
            if unvisited[x]:
                isOver = 0
                break

        if not unvisited or isOver:
            break

        elements = [node for node in unvisited.items() if node[1]]
        current, currentDist = sorted(elements, key=lambda x: x[1])[0]


process_file("input.txt")
start = 0


for i in range(1, len(nodes) + 1):
    start = i
    dijkstra(start)
    print("---------------------------------")
    print("Routing Table For:", start)
    print("\nDestination\tInterface")
    for key in interface:
        print(key, "\t\t\t", interface[key])
    print("---------------------------------")
