
import networkx as nx
import numpy as np

G = nx.karate_club_graph()

A = nx.to_numpy_array(G)
edge_list = list(G.edges())

print("Adjacency Matrix shape:", A.shape)
print(A)

print("\nEdge List:")
print(edge_list)
