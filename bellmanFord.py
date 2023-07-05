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

def bellmanFord(graph, src):
    srcName = src
    try:
        src = graph.vert_names[src]
    except(KeyError):
        print("Vertex does not exist!")
        return 0
    dist = [sys.maxsize] * graph.num_vertices
    predecessor = [None] * graph.num_vertices
    dist[src] = 0
    for e in range(0, graph.num_vertices, 1):
        for w, u, v in graph.edgeWeight:
            if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
            if graph.directed == False: 
                if dist[v] != sys.maxsize and dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    predecessor[u] = v
    for w, u, v in graph.edgeWeight:
        if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            print("=======================")
            return 0
    printSolution(graph, srcName, dist)

def main():
    # This graph has a negative weight cycle.
    g = Graph(False)
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_edge("a", "c", 3)
    g.add_edge("a", "d", 9)
    g.add_edge("c", "d", 4)
    g.add_edge("c", "b", 12)
    g.add_edge("d", "b", 7)
    print(g.edgeWeight)
    print("G Bellmanford's")
    bellmanFord(g, "a")
    # This graph does not have a negative weight cycle. And unlike Dijkstra's, Bellman Ford can handle negative edge weights.
    g1 = Graph(True)
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
    print("G1 Bellmanford's")
    print(g1.edgeWeight)
    bellmanFord(g1, "d")

main()