class Edge:
    def __init__(self, cap, is_res):
        self.cap = cap
        self.is_res = is_res
        self.current_flow = 0
        if is_res:
            self.res_cap = 0
        else:
            self.res_cap = cap

    def __repr__(self):
        return f"{self.cap} {self.current_flow} {self.res_cap} {self.is_res}"


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def insert_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {}

    def insert_edge(self, src, dst, cap):
        self.insert_node(src)
        self.insert_node(dst)
        self.adjacency_list[src][dst] = Edge(cap, False)
        self.adjacency_list[dst][src] = Edge(cap, True)

    def fetch_edge(self, v1, v2):
        return self.adjacency_list[v1][v2]

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def get_neighbors(self, node):
        return [(n, self.adjacency_list[node][n]) for n in self.adjacency_list[node]]


def bfs(g, start, end):
    seen_nodes = set()
    came_from = {}
    q = [start]
    seen_nodes.add(start)

    while q:
        current_node = q.pop(0)
        if current_node == end:
            break
        
        for nxt_node, link in g.get_neighbors(current_node):
            if nxt_node not in seen_nodes and link.res_cap > 0:
                seen_nodes.add(nxt_node)
                came_from[nxt_node] = current_node
                q.append(nxt_node)
                
    return came_from


def find_min_capacity(g, start, end, came_from):
    if end not in came_from:
        return 0
    
    current = end
    bottleneck = float('inf')
    
    while current != start:
        prev_node = came_from[current]
        link = g.fetch_edge(prev_node, current)
        if link.res_cap < bottleneck:
            bottleneck = link.res_cap
        current = prev_node
        
    return bottleneck


def augment_path(g, start, end, came_from, bottleneck):
    current = end
    while current != start:
        prev_node = came_from[current]
        fwd_edge = g.fetch_edge(prev_node, current)
        back_edge = g.fetch_edge(current, prev_node)

        fwd_edge.res_cap -= bottleneck
        back_edge.res_cap += bottleneck

        if not fwd_edge.is_res:
            fwd_edge.current_flow += bottleneck
        else:
            back_edge.current_flow -= bottleneck

        current = prev_node


def edmonds_karp(g, start, end):
    while True:
        came_from = bfs(g, start, end)
        bottleneck = find_min_capacity(g, start, end, came_from)
        
        if bottleneck == 0:
            break
            
        augment_path(g, start, end, came_from, bottleneck)
        
    total_flow = 0
    for node in g.get_nodes():
        if end in g.adjacency_list[node]:
            link = g.fetch_edge(node, end)
            if not link.is_res:
                total_flow += link.current_flow
                
    return total_flow


def printGraph(g):
    for node in g.get_nodes():
        print(node, end=" -> ")
        for (neighbor_node, weight_data) in g.get_neighbors(node):
            print(neighbor_node, weight_data, end="; ")
        print()


def calculate_out_flow(g, target_node):
    total_out = 0
    if target_node in g.get_nodes():
        for nxt_node, link in g.get_neighbors(target_node):
            if not link.is_res:
                total_out += link.current_flow
    return total_out


def build_graph_from_list(edges_data):
    g = Graph()
    for src, dst, cap in edges_data:
        g.insert_edge(src, dst, cap)
    return g


if __name__ == "__main__":
    graf_0_data = [('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1_data = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2_data = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3_data = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3), ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]

    test_cases = [
        (graf_0_data, 'u'),
        (graf_1_data, 'a'),
        (graf_2_data, 'a'),
        (graf_3_data, 'a')
    ]

    for idx, (data, query_node) in enumerate(test_cases):
        print(f"{idx} graf")
        g = build_graph_from_list(data)
        
        total_flow = edmonds_karp(g, 's', 't')
        node_flow = calculate_out_flow(g, query_node)
        
        print(total_flow)
        printGraph(g)
        print(f"'{query_node}': {node_flow}")