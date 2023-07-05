import sys
from graph import Graph
from graph import Vertex

def printSolution(graph, srcName, dist):
    if graph.directed == True:
        print("Graph is directed.")
    else:
        print("Graph is undirected")
    print(f"The shortest path from source \"{srcName}\" is:")
    for i, value in enumerate(dist):
        if value == sys.maxsize:
            value = "INF"
        print(str(srcName) + " ---> " + str(graph.vert_dict[i].name) + " = " + str(value))
    print("\n=======================")

def minDistance(dist, sptSet):
    min = sys.maxsize
    min_index = -1
    for u in range(0, len(dist), 1):
        if dist[u] < min and sptSet[u] == False:
            min = dist[u]
            min_index = u
    return min_index

def dijsktras(graph, src):
    srcName = src
    try:
        src = graph.vert_names[src]
    except(KeyError):
        print("Key Error: Vertex does not exist.")
        print("=======================")
        return 0
    dist = [sys.maxsize] * graph.num_vertices
    dist[src] = 0
    sptSet = [False] * graph.num_vertices
    # From here, the two steps for Dijsktra's Algorithm will be repeated.
    for k in range(0, graph.num_vertices, 1):
        print(str(k + 1) + " Step")
        # Step 1. Find the shortest path node that hasn't been visited and mark it as visited.
        x = minDistance(dist, sptSet)
        print("Minimum Distance = " + str(x))
        # Error catching if a directed graph is used and a node is not connected. But the graph here in this file is undirected.
        if x == -1:
            printSolution(graph, srcName, dist)
            return 0
        sptSet[x] = True
        print("sptSet = ", end="")
        print(sptSet)
        # Get the node object by it's id.
        nodeX = graph.find_node_by_id(x)
        print("nodeX = " + str(nodeX))
        # Loop through the connections of nodeX.
        for y in nodeX.get_connections():
            print(str(y.name) + ": " + str(nodeX.adjacent[y]))
            if nodeX.adjacent[y] > 0 and sptSet[y.id] == False and dist[y.id] > dist[x] + nodeX.adjacent[y]:
                # Step 2. Update the lowest path
                dist[y.id] = dist[x] + nodeX.adjacent[y]
                print("dist = ", end="")
                print(dist)
        print()
    printSolution(graph, srcName, dist)

def main():
    g1 = Graph(False)
    g1.add_vertex("a")
    g1.add_vertex("b")
    g1.add_vertex("c")
    g1.add_vertex("d")
    g1.add_vertex("e")
    g1.add_vertex("f")
    g1.add_vertex("g")
    g1.add_edge("a", "f", 10)
    g1.add_edge("a", "g", 25)
    g1.add_edge("a", "b", 20)
    g1.add_edge("f", "c", 20)
    g1.add_edge("f", "e", 30)
    g1.add_edge("f", "d", 2)
    g1.add_edge("d", "e", 4)
    g1.add_edge("d", "g", 10)
    g1.add_edge("c", "d", 3)
    g1.add_edge("b", "c", 15)
    g1.add_edge("b", "g", 3)
    g1.add_edge("g", "c", 2)
    g1.add_edge("g", "f", 3)
    #Perform the algorithm
    print("G1 Dijsktra's")
    dijsktras(g1, "f")
    # Another Graph Object
    # g2 = Graph(False)
    # g2.add_vertex("a")
    # g2.add_vertex("b")
    # g2.add_vertex("c")
    # g2.add_vertex("d")
    # g2.add_vertex("e")
    # g2.add_edge("a", "b", 3)
    # g2.add_edge("a", "c", 2)
    # g2.add_edge("a", "e", 4)
    # g2.add_edge("e", "d", 7)
    # g2.add_edge("b", "d", 4)
    # g2.add_edge("b", "c", 1)
    # g2.add_edge("c", "e", 1)
    # dijsktras(g2, "")

main()