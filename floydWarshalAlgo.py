# This one does not work with the graph object since python treats matrices all weird.
# You have to manually create the vertices and their adjacents.
# The graph is directed.
# What this algorithm does is use one vertex as the source. From that SOURCE A it tries to find a shorter path to NODE B
# using bridges created with other nodes.

# For example, say you wanted to connect Node A to Node D with a shorter path.
# To find this, you would want need to check Node A's adjacents to see if the adjacent node contains a shorter path to Node D.
# Say A -> D cost 10, but A -> B is 2 and B -> D is  3. To take a shorter path from A -> D, we can take A -> B -> D with a total cost of 5.
# This is what the algorthim does, checking every possible "bridge" from Node A to Node B and from there, Node B to every other possible Node.
# If a shorter path or "bridge" is found between these nodes to another node, then the matrix is updated.
INF = 999

# TODO go over this one
def main():
    graphMatrix = [[0, INF, 2, INF],
                  [4, 0, 3, INF],
                  [INF, INF, 0, 2],
                  [INF, 1, INF, 0]]
    graph = [[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0,  1],
        [1, INF, INF, 0]]
    floydWarshall(graph, 4)

def floydWarshall(graphMatrix, V):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graphMatrix))
    for k in range(V):
        # pick all vertices as source one by one
        for i in range(V):
            print()
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                print(f"[i][j]: {i} {j}")
                print(f"Current Node [i][k]: {i} {k}")
                print(f"[k][j]: {k} {j}")
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print()
    print()
    printSolution(dist, V)

def printSolution(dist, V):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
        print()
main()