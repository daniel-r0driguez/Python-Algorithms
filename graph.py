class Vertex:
    def __init__(self, node, id):
        self.name = node
        self.id = id
        self.adjacent = {}
        # Mark all nodes unvisited        
        self.visited = False

    def get_name_by_id(self, id):
        if self.id == id:
            return self.name

    def get_id(self):
        return self.id

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.name) + ' adjacent: ' + str([x.name for x in self.adjacent])

class Graph:
    def __init__(self, bool=True):
        # vert_dict now uses ID's as the key rather than the name.
        self.vert_dict = {}
        # vert_names uses the names as key, whose value is it's ID.
        self.vert_names = {}
        # Whether the graph is directed or undirected.
        self.directed = bool
        # Array which keeps track of edges [cost, frm, to].
        self.edgeWeight = []
        # Union-Find data structures.
        self.parent = []
        self.rank = []
        # Essentially works as keeping track of the number of vertices in the graph as well as working as the ID of new vertices.
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())
    # Fixed. Now each new vertex can be accessde by its ID instead of its name.
    def add_vertex(self, node):
        if node not in self.vert_names:
            self.parent.append(self.num_vertices)
            self.rank.append(0)
            new_vertex = Vertex(node, self.num_vertices)
            self.vert_names[node] = self.num_vertices
            self.vert_dict[self.num_vertices] = new_vertex
            self.num_vertices = self.num_vertices + 1
            return new_vertex
        else:
            print("Node name already in use!")
    # FIXED. Very easy fix. Now I think it's O(1) rather than O(N) like before.
    def get_vertex_by_name(self, n):
        if n in self.vert_names:
            return self.vert_dict[self.vert_names[n]]
    # FIXED. Instead of linear search, it is now O(1) because of the hash map.
    def get_vertex_name_by_id(self, id):
        return self.vert_dict[id].name
    # FIXED. Now we use the vert_names dict in order to link the names to their correct IDs.
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_names:
            self.add_vertex(frm)
        if to not in self.vert_names:
            self.add_vertex(to)
        self.edgeWeight.append([cost, self.vert_names[frm], self.vert_names[to]])
        self.vert_dict[self.vert_names[frm]].add_neighbor(self.vert_dict[self.vert_names[to]], cost)
        if self.directed == False:
            self.vert_dict[self.vert_names[to]].add_neighbor(self.vert_dict[self.vert_names[frm]], cost)
    # No change. Simply returns all the keys to each vertex object.
    def get_vertices(self):
        return self.vert_names.keys()
    # FIXED. Similar to the get_vertex_name_by_id, but instead of returning only the name, it returns the vertex object.
    def find_node_by_id(self, id):
        return self.vert_dict[id]