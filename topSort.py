from graph import Vertex
from graph import Graph

def topSort(graph = Graph):
    n = graph.num_vertices
    visited = [False] * n
    ordering = [0] * n
    i = n - 1
    for j in graph.vert_dict:
        curNode = graph.vert_dict[j]
        if visited[curNode.id] == False:
            print("DFS on node: " + str(curNode.name))
            i = DFS(i, curNode, visited, ordering)
    return ordering

def DFS(j = int, node = Vertex, visited = list, ordering = list) -> int:
    visited[node.id] = True
    for next in node.adjacent:
        print("Adjacent of " + str(node.name) + " is " + str(next.name))
        if visited[next.id] == False:
            j = DFS(j, next, visited, ordering)
    print("ordering[" + str(j) + "] is " + str(node.name))
    ordering[j] = node.name
    return j - 1

def main1():
    g = Graph(True)
    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_vertex("f")
    g.add_vertex("g")
    g.add_vertex("h")
    g.add_vertex("i")

    g.add_edge("a", "b")
    g.add_edge("b", "g")
    g.add_edge("b", "c")
    g.add_edge("g", "h")
    g.add_edge("c", "d")
    g.add_edge("d", "e")
    g.add_edge("h", "i")
    g.add_edge("i", "f")
    g.add_edge("e", "f")
    print(topSort(g))

def main2():
    g = Graph()
    for i in range(0, 100, 1):
        g.add_vertex(i)

    print(g.get_vertex_by_name(17))
    print()
    print(g.get_vertex_name_by_id(99))
    print()
    print(g.get_vertices())
    print()
    print(g.find_node_by_id(3))
main1()
