import polska
import Matrix_structure

class Vertex:
    def __init__(self, key):
        self.key = key
    def __eq__(self, other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    def __repr__(self):
        return self.key

class Graph2D:
    def __init__(self):
        self.matrix = Matrix_structure.Matrix((0,0))
        self.vertex_list = []

    def is_empty(self):
        return len(self.vertex_list) == 0
    
    def get_vertex(self, vertex_id):
        return self.vertex_list[vertex_id]
    
    def get_vertex_id(self, vertex):
        return self.vertex_list.index(vertex)
    
    def insert_vertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            for row in self.matrix:
                row.append(0)
            new_size = len(self.vertex_list)
            new_row = [0] * new_size
            self.matrix._Matrix__matrix.append(new_row)

    def delete_vertex(self, vertex):
        if vertex in self.vertex_list:
            idx = self.get_vertex_id(vertex)
            for row in self.matrix:
                row.pop(idx)
            self.matrix._Matrix__matrix.pop(idx)
            self.vertex_list.pop(idx)    

    def insert_edge(self, v1, v2, edge=1):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_edge(self, v1, v2):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        self.matrix[idx1][idx2] = 0
        self.matrix[idx2][idx1] = 0

    def get_edge(self, v1, v2):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        return self.matrix[idx1][idx2]

    def neighbours(self, vertex_id):
        for i in range(len(self.vertex_list)):
            edge = self.matrix[vertex_id][i]
            if edge != 0:
                yield (i, edge)
    
    def vertices(self):
        for idx in range(len(self.vertex_list)):
            yield idx

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


def Main():
    for graph_impl in [Graph2D, GraphDictDict]:
        g = graph_impl()
        v_objects = {}

        for v1_key, v2_key in polska.graf:
            if v1_key not in v_objects:
                v_objects[v1_key] = Vertex(v1_key)
                g.insert_vertex(v_objects[v1_key])
            if v2_key not in v_objects:
                v_objects[v2_key] = Vertex(v2_key)
                g.insert_vertex(v_objects[v2_key])
            
            e_val = 1 if isinstance(g, Graph2D) else None
            g.insert_edge(v_objects[v1_key], v_objects[v2_key], e_val)

        if 'K' in v_objects:
            g.delete_vertex(v_objects['K'])

        if 'W' in v_objects and 'E' in v_objects:
            g.delete_edge(v_objects['W'], v_objects['E'])

        polska.draw_map(g)

if __name__ == "__main__":
    Main()