from graph import Graph
from graph import Vertex

def main():
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_edge('d', 'a', 4)
    g.add_edge('d', 'c', 3)
    g.add_edge('a', 'c', 2)
    g.add_edge('c', 'e', 1)
    g.add_edge('c', 'b', 6)
    g.add_edge('a', 'e', 7)
    g.add_edge('a', 'b', 5)
    g.add_edge('b', 'e', 2)
    KruskalMST(g)
    g1 = Graph()
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
    g1.add_edge("f", "d", 25)
    g1.add_edge("d", "e", 4)
    g1.add_edge("d", "g", 10)
    g1.add_edge("c", "d", 3)
    g1.add_edge("b", "c", 15)
    g1.add_edge("b", "g", 3)
    g1.add_edge("g", "c", 2)
    g1.add_edge("g", "f", 3)
    # KruskalMST(g1)

def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

def apply_union(graph, x, y):
    xroot = find(graph.parent, x)
    yroot = find(graph.parent, y)
    if graph.rank[xroot] < graph.rank[yroot]:
        graph.parent[xroot] = yroot
    elif graph.rank[xroot] > graph.rank[yroot]:
        graph.parent[yroot] = xroot
    else:
        graph.parent[yroot] = xroot
        graph.rank[xroot] += 1

def KruskalMST(graph):
            result = []  # This will store the resultant MST
            cost = 0
            # An index variable, used for sorted edges
            i = 0

            # An index variable, used for result[]
            e = 0

            # Step 1:  Sort all the edges in
            # non-decreasing order of their
            # weight.  If we are not allowed to change the
            # given graph, we can create a copy of graph
            # IMPORTANT: graph.edgeWeight is going to be an array that houses E amount of tuples. In these tuples...
            # ...three indexes are available. [0] = weight, [1] = vertice 1 id, [2] = vertice 2 id.
            # Example: self.edgeWeight = [(1, 3, 1), (7, 2, 3), (3, 1, 2)]
            edgeWeight = sorted(graph.edgeWeight, key=lambda item:item[0])
            # Repeat until we get (Total Amount of Vertices) - 1 edges.
            while e < len(graph.vert_dict) - 1:
                # We get the weight, id of vertice 1(x) and 2(y) from index i of the array self.edgeWeight.
                weight, verticeX, verticeY = edgeWeight[i]
                i += 1
                verticeXRoot = find(graph.parent, verticeX)
                verticeYRoot = find(graph.parent, verticeY)
                if verticeXRoot != verticeYRoot:
                    e += 1
                    cost += weight
                    result.append([weight, graph.get_vertex_name_by_id(verticeX), graph.get_vertex_name_by_id(verticeY)])
                    apply_union(graph, verticeX, verticeY)
            for k in range(0, e, 1):
                print(f"Edge {k + 1}: {result[k][1]} --- {result[k][2]} with a weight of {result[k][0]}")
            print()
            print(f"Minimum Cost: {cost}")
main()