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

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = {}

    def insert_edge(self, v1, v2, edge=None):
        self.insert_vertex(v1)
        self.insert_vertex(v2)
        self.nodes[v1][v2] = edge
        self.nodes[v2][v1] = edge

    def neighbors(self, vertex_id):
        if vertex_id in self.nodes:
            for neighbor, edge in self.nodes[vertex_id].items():
                yield (neighbor, edge)

    def vertices(self):
        for vertex in self.nodes.keys():
            yield vertex


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, v):
        if self.p[v] == v:
            return v
        return self.find(self.p[v])

    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        
        if root1 == root2:
            return
        
        if self.size[root1] < self.size[root2]:
            self.p[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.p[root2] = root1
            self.size[root1] += self.size[root2]

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)


def test_union_find():
    uf = UnionFind(6)
    
    uf.union_sets(1, 2)
    uf.union_sets(4, 5)
    
    print(f"1, 2 {uf.same_component(1, 2)}")
    print(f"2, 3 {uf.same_component(2, 3)}")
    print(f"4, 5 {uf.same_component(4, 5)}")
    

    uf.union_sets(3, 1)
    print(f"2, 3 {uf.same_component(2, 3)}")


def char_to_idx(char):
    return ord(char) - ord('A')

def kruskal(raw_edges):
    sorted_edges = sorted(raw_edges, key=lambda edge: edge[2])
    
    unique_vertices = set()
    for v1, v2, _ in raw_edges:
        unique_vertices.add(v1)
        unique_vertices.add(v2)
    
    
    max_idx = max(char_to_idx(v) for v in unique_vertices)
    uf = UnionFind(max_idx + 1)
    
    mst = GraphDictDict()
    v_objects = {key: Vertex(key) for key in unique_vertices}
    
    total_weight = 0 

    for v1_key, v2_key, weight in sorted_edges:
        idx1 = char_to_idx(v1_key)
        idx2 = char_to_idx(v2_key)
        
        if not uf.same_component(idx1, idx2):
            uf.union_sets(idx1, idx2)
            
            mst.insert_edge(v_objects[v1_key], v_objects[v2_key], weight)
            total_weight += weight
            
    return mst, total_weight


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for n, w in g.neighbors(v):
            print(f"{n} {w}", end="; ")
        print()
    print("-------------------")


def Main():
    test_union_find()
    
    raw_graph_data = graf_mst.graf
    
    wynik_mst, laczna_waga = kruskal(raw_graph_data)
    
    printGraph(wynik_mst)
    print(laczna_waga)


if __name__ == "__main__":
    Main()