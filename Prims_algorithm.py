import graf_mst

class Vertex:
    def __init__(self, key):
        self.key = key
    def __eq__(self, other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return self.key
    
class GraphDictDict:
    def __init__(self):
        self.nodes = {}

    def is_empty(self):
        return not self.nodes

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}

    def insert_edge(self, v1, v2, edge=None):
        self.insert_vertex(v1)
        self.insert_vertex(v2)
        self.nodes[v1][v2] = edge
        self.nodes[v2][v1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.nodes:
            for neighbor in list(self.nodes[vertex].keys()):
                del self.nodes[neighbor][vertex]
            del self.nodes[vertex]

    def delete_edge(self, v1, v2):
        if v1 in self.nodes and v2 in self.nodes[v1]:
            del self.nodes[v1][v2]
            del self.nodes[v2][v1]

    def get_edge(self, v1, v2):
        return self.nodes.get(v1, {}).get(v2)

    def get_vertex(self, vertex_id):
        return vertex_id

    def neighbours(self, vertex_id):
        if vertex_id in self.nodes:
            for neighbor, edge in self.nodes[vertex_id].items():
                yield (neighbor, edge)

    def vertices(self):
        for vertex in self.nodes.keys():
            yield vertex

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for n, w in g.neighbours(v):
            print(n, w, end="; ")
        print()
    print("-------------------")

def prims(graph):
    intree = {}
    distance = {}
    parent = {}

    for key in graph.nodes:
        intree[key] = False
        distance[key] = float('inf')
        parent[key] = None

    start_node = list(graph.nodes.keys())[0]

    distance[start_node] = 0
    
    mst = GraphDictDict()

    v = start_node

    while not intree[v]:
        intree[v] = True
        for n, w in graph.neighbours(v):
            if w < distance[n] and not intree[n]:
                distance[n] = w
                parent[n] = v
        
        min_dist = float('inf')
        next_v = None
        
        for node in graph.nodes:
            if not intree[node]:
                if distance[node] < min_dist:
                    min_dist = distance[node]
                    next_v = node
        
        if next_v is None:
            break
            
        p = parent[next_v]
        
        weight = distance[next_v]
        
        mst.insert_edge(p, next_v, weight)
        
        v = next_v
    
    return mst

def Main():
    g = GraphDictDict()

    v_objects = {}

    for v1_key, v2_key, weight in graf_mst.graf:
        if v1_key not in v_objects:
            v_objects[v1_key] = Vertex(v1_key)
        if v2_key not in v_objects:
            v_objects[v2_key] = Vertex(v2_key)

        g.insert_edge(v_objects[v1_key], v_objects[v2_key], weight)

    wynik_mst = prims(g)

    printGraph(wynik_mst)


if __name__ == "__main__":
    Main()