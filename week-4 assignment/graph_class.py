
class Graph:
    def __init__(self):
        self.nodes = set()
        self.adj = {}
        self.node_features = {}
        self.edge_features = {}

    def add_node(self, u, features=None):
        self.nodes.add(u)
        self.adj.setdefault(u, [])
        if features is not None:
            self.node_features[u] = features

    def add_edge(self, u, v, features=None, undirected=True):
        self.add_node(u)
        self.add_node(v)

        self.adj[u].append(v)
        if undirected:
            self.adj[v].append(u)

        if features is not None:
            self.edge_features[(u, v)] = features
            if undirected:
                self.edge_features[(v, u)] = features

    def get_neighbors(self, u):
        return self.adj.get(u, [])

    def __repr__(self):
        return f"Graph(num_nodes={len(self.nodes)})"
