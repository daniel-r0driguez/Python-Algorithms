# Very easy topological sort. Instead of performing DFS on a graph (like the default topological sort algo),
# you first get the degree of each node (the number of times the node is pointed at).
# Any nodes with a degree of 0, will first be added to the queue. Read the comments in the while loop to understand clearer.
# I think Kahn's Topological Sort is BFS???
from graph import Graph
from graph import Vertex
def kahnsTop(graph):
    # nodeDegree holds the number of dependencies a node has. (The number of nodes currently pointing to it.)
    nodeDegree = [0] * graph.num_vertices
    for i in graph.edgeWeight:
        nodeDegree[i[2]] += 1
    
    queue = []
    for j in range(0, graph.num_vertices, 1):
        if (nodeDegree[j] == 0):
            queue.append(j)

    index = 0
    order = [''] * graph.num_vertices
    while (queue):
        # Pop the first node id.
        cur = queue.pop(0)
        # Add the node's name to the ordering array.
        order[index] = graph.get_vertex_name_by_id(cur)
        # Increment the index for the next node.
        index += 1
        # Create a list named adjacents which holds Vertex type objects.
        adjacents = list(graph.find_node_by_id(cur).adjacent.keys())
        # For the items in cur's adjacents...
        for k in adjacents:
            # Decrease the adjacent node's degree by 1.
            nodeDegree[k.id] -= 1
            # If the adajacent node's degree is 0, add it to the queue.
            if nodeDegree[k.id] == 0:
                queue.append(k.id)
    # If index does not equal the number of nodes in the graph, that means there is a cycle, since there
    # is repetition of dependencies in the graph.
    if index != graph.num_vertices:
        print("There is a cycle in the graph!")
        return -1
    # Return the topological sort of the graph.
    return order


def main():
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
    print(kahnsTop(g))
main()
